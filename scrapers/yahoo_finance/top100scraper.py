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

# check all companies scraped properly
print(listCompanies)
