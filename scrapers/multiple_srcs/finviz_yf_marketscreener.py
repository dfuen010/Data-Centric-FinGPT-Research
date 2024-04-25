import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import json
import asyncio
import aiohttp
import os
import gspread
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import util
import random
from io import StringIO

pd.options.mode.chained_assignment = None

MAX_WORKERS = 10

years = util.get_years()
col_names = util.get_col_names()

def get_ticker_info(ticker):
    """
    Get detailed information about a ticker using Yahoo Finance API.

    Parameters:
        ticker (str): The ticker symbol of the stock.

    Returns:
        dict: Information about the stock.
    """
    ticker_info = yf.Ticker(ticker).info
    return {
        "Ticker": ticker,
        "Name": ticker_info.get("longName"),
        "Market Cap": ticker_info.get("marketCap"),
        "Sector": ticker_info.get("sector"),
        "Summary": ticker_info.get("longBusinessSummary"),
        "Industry": ticker_info.get("industry"),
        "Shares Outstanding": ticker_info.get("sharesOutstanding"),
        "Institution Ownership": ticker_info.get("heldPercentInstitutions"),
        "Price": ticker_info.get("currentPrice"),
        "52-Week High": ticker_info.get("fiftyTwoWeekHigh"),
        "52-Week Low": ticker_info.get("fiftyTwoWeekLow"),
        "Enterprise Value": ticker_info.get("enterpriseValue"),
        "Beta": ticker_info.get("beta"),
    }

def get_yahoo_data(tickers):
    """
    Get and parse data about multiple tickers from Yahoo Finance.

    Parameters:
        tickers (list): List of ticker symbols.

    Returns:
        pandas.DataFrame: DataFrame containing parsed data.
    """
    yahoo_data = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(get_ticker_info, tickers))

    for info in results:
        yahoo_data.append(list(info.values()))

    return pd.DataFrame(yahoo_data, columns=info.keys())


async def get_all_html(urls: list, max_workers: int = MAX_WORKERS) -> list:
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    sem = asyncio.Semaphore(max_workers)
    async with aiohttp.ClientSession(headers=header) as session:
        data = await visit_all_links(session, urls, sem)
        return data
    
async def get_page(session: aiohttp.ClientSession, url: str) -> str:
    """
    Fetch HTML content from a URL using aiohttp.

    Parameters:
        session (aiohttp.ClientSession): The aiohttp session object.
        url (str): The URL to fetch content from.

    Returns:
        str: HTML content of the page.
    """
    async with session.get(url) as response:
        return await response.text()

async def visit_all_links(
    session: aiohttp.ClientSession, urls: list, semaphore: asyncio.Semaphore
) -> list:
    """
    Visit multiple URLs asynchronously and fetch HTML content.

    Parameters:
        session (aiohttp.ClientSession): The aiohttp session object.
        urls (list): List of URLs to visit.
        semaphore (asyncio.Semaphore): Semaphore for controlling concurrent requests.

    Returns:
        list: List of HTML content fetched from the URLs.
    """
    tasks = []
    for url in urls:
        async with semaphore:
            task = asyncio.create_task(get_page(session, url))
            tasks.append(task)
    return await asyncio.gather(*tasks)

async def get_marketscreener_links(tickers, names, links):
    """
    Get MarketScreener links for tickers if not already stored in links dictionary.

    Parameters:
        tickers (list): List of ticker symbols.
        names (list): List of company names.
        links (dict): Dictionary containing ticker-symbol to MarketScreener links mapping.

    Returns:
        dict: Updated links dictionary.
    """
    tickers_to_process = [x for x in tickers if x not in links]
    urls_to_fetch = [
        "https://www.marketscreener.com/search/?q=" + "+".join(x.split())
        for x in names
        if x not in links
    ]
    html_list = await get_all_html(urls_to_fetch)

    for ticker, html in zip(tickers_to_process, html_list):
        soup = BeautifulSoup(html, features="lxml")
        rows = soup.find_all("tr")
        for row in rows:
            currency_tag = row.find("span", {"class": "txt-muted"})
            if currency_tag and currency_tag.text.strip() == "USD":
                link = row.find("a", href=True)["href"]
                links[ticker] = "https://www.marketscreener.com" + link + "finances/"
                break

    with open("datasets/marketscreener_yf/MarketScreener.json", "w") as file:
        json.dump(links, file)
        
    return links

def parse_marketscreener(results):
    """
    Parse data from MarketScreener HTML content.
    
    Parameters:
        results (list): List of HTML content from MarketScreener.
        
    Returns:
        pandas.DataFrame: DataFrame containing parsed data."""
    ### HELPER FUNCTIONS
    def fix_names(x):
        for num in ["1", "2", "3"]:
            if num in x:
                return x.replace(num, "")
        return x

    def process_df(df):
        df = df.dropna(axis=1, how="all")
        df.iloc[:, 0] = df.iloc[:, 0].apply(fix_names)
        df.set_index(df.columns[0], inplace=True)
        df.index = df.index.str.strip()
        return df

    marketscreener = pd.DataFrame()
    for html in results:
        divs = BeautifulSoup(html, features="lxml").find_all(
            "div", {"class": "card card--collapsible mb-15"}
        )
        for div in divs:
            header_text = div.find("div", {"class": "card-header"}).text
            if ("income statement" in header_text.lower()) and (
                "annual" in header_text.lower()
            ):
                income_statement = div.find("table")
                with StringIO(str(income_statement)) as sio:
                    income_statement = pd.read_html(sio)[0]
                currency = (
                    div.find_all("sup")[0]
                    .attrs["title"]
                    .replace("\n", "")
                    .strip()
                    .split(" ")[0]
                )
                unit = (
                    div.find_all("sup")[0]
                    .attrs["title"]
                    .replace("\n", "")
                    .strip()
                    .split(" ")[-1]
                )
                break
        currency, unit = pd.Series(currency), pd.Series(unit)
        income_statement = process_df(income_statement)
        col_names_is = income_statement.columns.tolist()
        applicable = [col for col in col_names_is if col in years]
        remain = [col for col in years if col not in applicable]
        metrics = []
        filler = pd.Series([0] * len(remain), dtype="object")
        metrics_names = ["Net sales", "Net income", "EBITDA", "EBIT"]
        for metric in metrics_names:
            metrics.append(
                pd.Series(income_statement.loc[:, applicable].loc[metric])
                .T.reset_index(drop=True)
                .str.replace(" ", "")
            )
            metrics.append(filler)
        indiv = pd.DataFrame(pd.concat(metrics)).T
        indiv = pd.concat([indiv, currency, unit], axis=1)
        indiv.columns = list(
            range(len(indiv.columns.tolist()))
        )  # Net sales, Net income, EBITDA, EBIT for X years, currency, unit
        marketscreener = pd.concat([marketscreener, indiv], axis=0)
    return marketscreener.reset_index(drop=True).replace("-", 0)

def parse_finviz(results):
    """
    Parses data from FinViz HTML content.
    Parameters:
        results (list): List of HTML content from FinViz.
    Returns:
        pandas.DataFrame: DataFrame containing parsed data."""
        
    finviz = pd.DataFrame()
    perf_columns = [
        "Perf Week",
        "Perf Month",
        "Perf Quarter",
        "Perf Half Y",
        "Perf Year",
        "Perf YTD",
    ]

    for html in results:
        soup = BeautifulSoup(html, features="lxml")
        table = soup.find_all("table", {"class": "snapshot-table2"})
        try:
            df = pd.read_html(str(table))[0].iloc[:, -2:].set_index(10)
            df[11] = df[11].str.replace("%", "")
            perf_values = df.loc[perf_columns].astype(float).T.reset_index(drop=True)
            indiv = pd.DataFrame(perf_values, columns=perf_columns)
        except:
            indiv = pd.DataFrame([[0] * 6], columns=perf_columns)
        finviz = pd.concat([finviz, indiv], axis=0, ignore_index=True)
    return finviz

if __name__ == "__main__":
    all_tickers = []
    with open("scrapers/multiple_srcs/nasdaq_tickers.json", "r") as file:
        all_tickers = json.load(file)
        
    random_20_tickers = random.sample(all_tickers, 20)
    
    # Yahoo Finance
    yahoo = get_yahoo_data(random_20_tickers)
    names = yahoo["Name"].tolist()
    
    links= {}
    
    # MarketScreener
    links = asyncio.run(get_marketscreener_links(random_20_tickers, names, links))
    market_screener_urls = [links[x] for x in random_20_tickers if x in links]
    market_screener_htmls = asyncio.run(get_all_html(market_screener_urls))
    marketscreener = parse_marketscreener(market_screener_htmls)    
    
    # FinViz
    finviz_urls = ["https://finviz.com/quote.ashx?t=" + x for x in random_20_tickers]
    finviz_htmls = asyncio.run(get_all_html(finviz_urls))
    finviz = parse_finviz(finviz_htmls)
    
    final = pd.concat([yahoo, finviz, marketscreener], axis=1)
    final = final.apply(pd.to_numeric, errors="ignore")
    final = final.replace(np.nan, 0).fillna(0)
    
    final.to_csv("datasets/marketscreener_yf/finviz_yf_marketscreener.csv", index=False)
    
    