import yfinance as yf
import json

# Read the first 30 lines from the CSV file
file_path = "scrapers/yahoo_finance/bats_symbols.csv"
list_companies = []

with open(file_path, "r") as f:
    for i, line in enumerate(f):
        if i >= 30:
            break
        company = line.split(",")[0]
        list_companies.append(company)

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

# Write summaries to text file
with open('datasets/news/yahoo_finance/summaries.txt', 'w') as f:
    for company in list_companies:
        summary = companyDict[company].get("longBusinessSummary", "Summary not available")
        f.write(f"{company} Summary:\n{summary}\n\n")

# Write stock information to text file
with open('datasets/news/yahoo_finance/stock_info.txt', 'w') as f:
    for company in list_companies:
        stock_month = yf.download(company, period="1mo")
        f.write(f"{company} Stock:\n{stock_month}\n\n")
