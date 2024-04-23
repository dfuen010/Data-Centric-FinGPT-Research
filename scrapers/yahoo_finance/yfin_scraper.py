import yfinance as yf
import pandas as pd
import json

list_companies = ["MSFT", "AAPL", "TSLA", "GOOGL", "AMZN", "FB", "NFLX", "GOOG", "NVDA", "PYPL"]
companyDict = {}

# Go through listed companies
for company in list_companies:
    
    # Use yahoofinance API to get ticker object
    ticker = yf.Ticker(company)
    
    # Get the information for the company
    companyDict[company] = ticker.info

# Put data into JSON
with open('data.json', 'w') as f:
    json.dump(companyDict, f)

# Get Summary of Company
for company in list_companies:
    summary = companyDict[company].get("longBusinessSummary", "Summary not available")
    print(f"{company} Summary:")
    print(summary)
    print()

# Get last 1 month stock information (buy / sell)
for company in list_companies:
    stock_month = yf.download(company, period="1mo")
    print(f"{company} Stock:")
    print(stock_month)
    print()
