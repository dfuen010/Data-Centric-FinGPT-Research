import yfinance as yf
import pandas as pd
import json

list_companies = ["MSFT", "APPL", "TSLA"]
companyDict = {}

# go through listed companies
for company in list_companies:
    
    # use yahoofinance api to get ticker object
    ticker = yf.Ticker(company)
    
    # history = ticker.history(period = "1mo")
    
    #get the information from company
    companyDict[company] = ticker.info
    

# put data in to json
with open('data.json', 'w') as f:
    json.dump(companyDict, f)
    
    
