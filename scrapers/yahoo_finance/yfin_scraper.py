import yfinance as yf
import pandas as pd
import json

list_companies = ["MSFT", "AAPL", "TSLA"]
companyDict = {}


# go through listed companies
for company in list_companies:
    
    # use yahoofinance api to get ticker object
    ticker = yf.Ticker(company)
    
    # history = ticker.history(period = "1mo")
    
    #get the information from company
    companyDict[company] = ticker.info
    

# # put data in to json
# with open('data.json', 'w') as f:
#     json.dump(companyDict, f)
    


# Get Summary of Company
msft_summary = companyDict["MSFT"]["longBusinessSummary"]
apple_summary = companyDict["AAPL"]["longBusinessSummary"]
tesla_summary = companyDict["TSLA"]["longBusinessSummary"]

# Get last 1 month stock information (buy / sell)
msft_stock_month = yf.download("SPY AAPL", period="1mo")
appl_stock_month = yf.download("SPY MSFT",period = "1mo" )
tsla_stock_month = yf.download("SPY TSLA",period = "1mo" )


print(msft_summary, "\n", msft_stock_month)
print("\n")

print(apple_summary, "\n", appl_stock_month)
print("\n")

print(tesla_summary, "\n", tsla_stock_month)
print("\n")
