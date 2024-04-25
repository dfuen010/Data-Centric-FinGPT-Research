import pandas as pd

def get_years():
    return [str(year) for year in range(2019, 2026)]

def get_col_names():
    col_names = [
    "Ticker",
    "Name",
    "Market Cap",
    "Sector",
    "Business Summary",
    "Industry",
    "Shares Outstanding",
    "Institution Ownership",
    "Current Price",
    "52-Week High",
    "52-Week Low",
    "Enterprise Value",
    "Beta",
    "Weekly Price Change %",
    "Monthly Price Change %",
    "Quarterly Price Change %",
    "Half-Yearly Price Change %",
    "Yearly Price Change %",
    "YTD Price Change %",
    ]
    return col_names

def get_market_links():
    links = {
        "AAPL": "https://www.marketscreener.com/quote/stock/APPLE-INC-4849/finances/", 
        "MSFT": "https://www.marketscreener.com/quote/stock/MICROSOFT-CORPORATION-4835/finances/", 
        "GOOG": "https://www.marketscreener.com/quote/stock/ALPHABET-INC-24203373/finances/", 
        "TSLA": "https://www.marketscreener.com/quote/stock/TESLA-INC-6344549/finances/", 
        "META": "https://www.marketscreener.com/quote/stock/META-PLATFORMS-INC-10547141/finances/", 
        "ADBE": "https://www.marketscreener.com/quote/stock/ADOBE-INC-4844/finances/", 
        "CRM": "https://www.marketscreener.com/quote/stock/SALESFORCE-COM-INC-12180/finances/", 
        "NFLX": "https://www.marketscreener.com/quote/stock/NETFLIX-INC-44292425/finances/", 
        "AMD": "https://www.marketscreener.com/quote/stock/ADVANCED-MICRO-DEVICES-IN-19475876/finances/", 
        "NVDA": "https://www.marketscreener.com/quote/stock/NVIDIA-CORPORATION-57355629/finances/", 
        "F": "https://www.marketscreener.com/quote/stock/FORD-MOTOR-COMPANY-12542/finances/", 
        "BA": "https://www.marketscreener.com/quote/stock/THE-BOEING-COMPANY-103502379/finances/", 
        "ROKU": "https://www.marketscreener.com/quote/stock/ROKU-INC-37892974/finances/", 
        "PYPL": "https://www.marketscreener.com/quote/stock/PAYPAL-HOLDINGS-INC-23377703/finances/", 
        "SQ": "https://www.marketscreener.com/quote/stock/BLOCK-INC-24935553/finances/", 
        "COIN": "https://www.marketscreener.com/quote/stock/COINBASE-GLOBAL-INC-121300010/finances/", 
        "SNAP": "https://www.marketscreener.com/quote/stock/SNAP-INC-34091150/finances/", 
        "SE": "https://www.marketscreener.com/quote/stock/SEA-LIMITED-38150303/finances/", 
        "ZM": "https://www.marketscreener.com/quote/stock/ZOOM-VIDEO-COMMUNICATIONS-57086220/finances/", 
        "BYND": "https://www.marketscreener.com/quote/stock/BEYOND-MEAT-INC-57878377/finances/", 
        "BABA": "https://www.marketscreener.com/quote/stock/ALIBABA-GROUP-HOLDING-LIM-17916677/finances/", 
        "BILI": "https://www.marketscreener.com/quote/stock/BILIBILI-INC-42503507/finances/", 
        "DIDIY": "https://www.marketscreener.com/quote/stock/DIDI-GLOBAL-INC-124258212/finances/", 
        "BIDU": "https://www.marketscreener.com/quote/stock/BAIDU-INC-8563/finances/", 
        "TCEHY": "https://www.marketscreener.com/quote/stock/TENCENT-HOLDINGS-LIMITED-120792085/finances/", 
        "SHOP": "https://www.marketscreener.com/quote/stock/SHOPIFY-INC-22283351/finances/", 
        "TTD": "https://www.marketscreener.com/quote/stock/THE-TRADE-DESK-INC-31370485/finances/", 
        "INTC": "https://www.marketscreener.com/quote/stock/INTEL-CORPORATION-4829/finances/", 
        "QCOM": "https://www.marketscreener.com/quote/stock/QUALCOMM-INC-4897/finances/", 
        "MU": "https://www.marketscreener.com/quote/stock/MICRON-TECHNOLOGY-INC-13639/finances/", 
        "AMZN": "https://www.marketscreener.com/quote/stock/APPLE-INC-4849/finances/", 
        "TSM": "https://www.marketscreener.com/quote/stock/MICROSOFT-CORPORATION-4835/finances/"
    }
    return links
    