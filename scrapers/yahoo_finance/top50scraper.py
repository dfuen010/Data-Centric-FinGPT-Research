import yfinance as yf
import json

file_path = "scrapers/yahoo_finance/top100.txt"

listCompanies = []

with open(file_path, "r") as f:
    
    # go thru text file
    for line in f:
        
        #add companies to array
        company = line.strip()
        listCompanies.append(company)

# for all company tickers
companyDict = {}
x = listCompanies[0]
tick = yf.Ticker(x)
print(tick.balance_sheet)

with open("datasets/news/yahoo_finance/top50financials"):
    
    for company in listCompanies:
        
        ticker = yf.Ticker(company)
        incomeStatement = ticker.income_stmt
        balanceSheet = ticker.balance_sheet