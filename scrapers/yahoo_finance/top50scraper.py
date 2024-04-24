import yfinance as yf
import json

file_path = "scrapers/yahoo_finance/top50.txt"

listCompanies = []

with open(file_path, "r") as f:
    
    # go thru text file
    for line in f:
        
        #add companies to array
        company = line.strip()
        listCompanies.append(company)

with open("datasets/news/yahoo_finance/top50financials.txt", "w") as f:
    
    for company in listCompanies:
        
        ticker = yf.Ticker(company)
        incomeStatement = ticker.income_stmt
        balanceSheet = ticker.balance_sheet
        if(balanceSheet.columns.empty):
            continue
        f.write(f"\n\n{company} Financials(Income Statement/Balance Sheet):\n\n")
        f.write(f"Income Statement for {company}{incomeStatement}\n\n")
        f.write(f"Balance Sheet for {company}{balanceSheet.to_string()}\n\n")
        