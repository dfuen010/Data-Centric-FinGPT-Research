import requests
import json
import re
from parsel import Selector

def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Error fetching HTML:", e)
        return None

def extract_market_trends(selector):
    top_results = selector.css(".gR2U6::text").getall()
    bottom_results = []
    for index, market_trend in enumerate(selector.css("[jscontroller=mBF9u]"), start=1):
        bottom_results.append({
            "index": index,
            "title": market_trend.css(".ZvmM7::text").get(),
            "quote": market_trend.css(".COaKTb::text").get(),
            "price": market_trend.css(".YMlKec::text").get(),
            "price_percent_change": get_percent_change(market_trend.css("[jsname=Fe7oBc]::attr(aria-label)").get())
        })
    return top_results, bottom_results

def extract_earning_calendar(selector):
    calendar_entries = []
    for calendar_quote in selector.css(".d3fRjc"):
        calendar_entries.append({
            "quote": calendar_quote.css(".yaubCc::text").get(),
            "quote_link": f'https://www.google.com/finance/quote{calendar_quote.css(".yaubCc::attr(href)").get().replace("./quote/", "/")}',
            "short_date": calendar_quote.css(".JiAI5b").xpath("normalize-space()").get(),
            "full_date": calendar_quote.css(".fVovwd::text").get()
        })
    return calendar_entries

def extract_most_followed(selector):
    followed_entries = []
    for google_most_followed in selector.css(".NaLFgc"):
        current_percent_change_raw_value = google_most_followed.css("[jsname=Fe7oBc]::attr(aria-label)").get()
        current_percent_change = get_percent_change(current_percent_change_raw_value)
        followed_entries.append({
            "title": google_most_followed.css(".TwnKPb::text").get(),
            "quote": re.search(r"\.\/quote\/(\w+):",google_most_followed.attrib["href"]).group(1),
            "following": re.search(r"(\d+\.\d+)M", google_most_followed.css(".Iap8Fc::text").get()).group(1),
            "percent_price_change": current_percent_change
        })
    return followed_entries

def extract_news(selector):
    news_entries = []
    for index, news in enumerate(selector.css(".yY3Lee"), start=1):
        news_entries.append({
            "position": index,
            "title": news.css(".Yfwt5::text").get(),
            "link": news.css(".z4rs2b a::attr(href)").get(),
            "source": news.css(".sfyJob::text").get(),
            "published": news.css(".Adak::text").get(),
            "thumbnail": news.css("img.Z4idke::attr(src)").get()
        })
    return news_entries

def extract_interesting(selector):
    top_results = []
    bottom_results = []
    for index, interested in enumerate(selector.css(".sbnBtf:not(.xJvDsc) .SxcTic"), start=1):
        current_percent_change_raw_value = interested.css("[jsname=Fe7oBc]::attr(aria-label)").get()
        current_percent_change = get_percent_change(current_percent_change_raw_value)
        top_results.append({
            "index": index,
            "title": interested.css(".ZvmM7::text").get(),
            "quote": interested.css(".COaKTb::text").get(),
            "price_change": interested.css(".SEGxAb .P2Luy::text").get(),
            "percent_price_change": current_percent_change
        })
    for index, interested in enumerate(selector.css(".HDXgAf .tOzDHb"), start=1):
        current_percent_change_raw_value = interested.css("[jsname=Fe7oBc]::attr(aria-label)").get()
        current_percent_change = get_percent_change(current_percent_change_raw_value)
        bottom_results.append({
            "position": index,
            "ticker": interested.css(".COaKTb::text").get(),
            "ticker_link": f'https://www.google.com/finance{interested.attrib["href"].replace("./", "/")}',
            "title": interested.css(".RwFyvf::text").get(),
            "price": interested.css(".YMlKec::text").get(),
            "percent_price_change": current_percent_change
        })
    return top_results, bottom_results

def get_percent_change(percent_change_raw_value):
    if percent_change_raw_value:
        match = re.search(r"by\s?(\d+\.\d+)%", percent_change_raw_value)
        if match:
            return f"+{match.group(1)}" if "Up" in percent_change_raw_value else f"-{match.group(1)}"
    return None

def scrape_google_finance_main_page():
    html = get_html("https://www.google.com/finance/")
    if html:
        selector = Selector(text=html)
        market_trends_top, market_trends_bottom = extract_market_trends(selector)
        earning_calendar = extract_earning_calendar(selector)
        most_followed = extract_most_followed(selector)
        news = extract_news(selector)
        interesting_top, interesting_bottom = extract_interesting(selector)
        
        ticker_data = {
            "market_trends": {
                "top_position": market_trends_top,
                "bottom_position": market_trends_bottom
            },
            "interested_in": {
                "top_position": interesting_top,
                "bottom_position": interesting_bottom
            },
            "earning_calendar": earning_calendar,
            "most_followed_on_google": most_followed,
            "news": news,
        }
        
        return ticker_data
    else:
        return None

# scrape_google_finance_main_page()
with open("google_finance_main.json", "w") as file:
    file.write(json.dumps(scrape_google_finance_main_page(), indent=2, ensure_ascii=False))
