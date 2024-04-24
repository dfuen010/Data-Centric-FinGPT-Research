import yfinance as yf
import json

# Get Directory Path
file_path = "scrapers/yahoo_finance/top50.txt"
listCompanies = []

# Open Company Text File
with open(file_path, "r") as f:
    
    # Go Through Each Line (each line is company ticker)
    for line in f:
        
        #add companies to list
        company = line.strip()
        listCompanies.append(company)

# Open file to write Company Financials
with open("datasets/news/yahoo_finance/top50financials.txt", "w") as f:
    
    # Go through previously created List
    for company in listCompanies:
        
        # Get Ticker
        ticker = yf.Ticker(company)
        # Get Income and Balance Statements
        incomeStatement = ticker.income_stmt
        balanceSheet = ticker.balance_sheet
        # Check if there is there income/balanace info available
        if(balanceSheet.columns.empty):
            # if not, go to next company
            continue
        # Format and Write to File the Required Information
        f.write(f"\n\n{company} Financials(Income Statement/Balance Sheet):\n\n")
        f.write(f"Income Statement for {company}{incomeStatement}\n\n")
        f.write(f"Balance Sheet for {company}{balanceSheet.to_string()}\n\n")
        