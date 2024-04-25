import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import json
import asyncio
import os
import gspread
import numpy as np
from concurrent.futures import ThreadPoolExecutor
import util

pd.options.mode.chained_assignment = None

MAX_WORKERS = 10

years = util.get_years()
col_names = util.get_col_names()

# Get ticker for yfinance
def get_ticker(x):
        ticker = yf.Ticker(x)
        return ticker.info

# Get data from Yahoo Finance
def get_and_parse_yahoo(tickers):
    

    yahoo = pd.DataFrame()
    with ThreadPoolExecutor(max_workers=10) as pool:
        results = list(pool.map(get_ticker, tickers))

    for idx, info in enumerate(results):
        data = [
            {"Ticker": tickers[idx]},
            {"Name": info.get("longName")},
            {"Market Cap": info.get("marketCap")},
            {"Sector": info.get("sector")},
            {"Summary": info.get("longBusinessSummary")},
            {"Industry": info.get("industry")},
            {"Shares Outstanding": info.get("sharesOutstanding")},
            {"Institution Ownership": info.get("heldPercentInstitutions")},
            {"Price": info.get("currentPrice")},
            {"52-Week High": info.get("fiftyTwoWeekHigh")},
            {"52-Week Low": info.get("fiftyTwoWeekLow")},
            {"Enterprise Value": info.get("enterpriseValue")},
            {"Beta": info.get("beta")},
        ]
        indiv = pd.DataFrame(
            [x.values() for x in data], index=[list(x.keys())[0] for x in data]
        ).T.reset_index(drop=True)
        yahoo = pd.concat([yahoo, indiv], axis=0)

    return yahoo.reset_index(drop=True)

if __name__ == "__main__":
    cred = json.loads(os.environ.get("GOOGLE_CREDS"))
    gc = gspread.service_account_from_dict(cred)
    wb = gc.open(os.environ.get("GOOGLE_SHEET_NAME"))
    data_sheet = wb.worksheet("Data")
    tickers = data_sheet.col_values(1)[1:]
    tickers = [x.upper() for x in tickers]

    yahoo = get_and_parse_yahoo(tickers)
    names = yahoo["Name"].tolist()

    