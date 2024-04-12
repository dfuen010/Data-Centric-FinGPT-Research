import pandas as pd
import requests
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer
from bs4 import BeautifulSoup
import os
import sys
import json

def get_tickers(headers):
    company_tickers = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers
        )

    # dictionary to dataframe
    company_data = pd.DataFrame.from_dict(company_tickers.json(), orient='index')

    company_data['cik_str'] = company_data['cik_str'].astype(str).str.zfill(10)
    return company_data

def get_report(headers, cik):
    filing_metadata = requests.get(
        f'https://data.sec.gov/submissions/CIK{cik}.json',
        headers=headers
        )

    # Getting into the filings reports
    # print(filingMetadata.json()['filings']['recent'].keys())

    all_forms = pd.DataFrame.from_dict(
        filing_metadata.json()['filings']['recent']
        )
    form_4 = all_forms[all_forms['form'].str.contains('4')]
    document_1 = form_4.iloc[0]['primaryDocument']

    access_num_1 = form_4.iloc[0]['accessionNumber']
    access_num_1 = access_num_1.replace('-', '')

    return f'https://www.sec.gov/Archives/edgar/data/{cik}/{access_num_1}/{document_1}'

def extract_data(headers, filing_link):
    response = requests.get(filing_link, headers=headers)
    
    soup = BeautifulSoup(response.content, 'lxml')
    with open('form4.txt', 'w') as file:
        file.write(soup.prettify())

if __name__ == "__main__":
    headers = {'User-Agent': "email@address.com"}

    # Get all the tickers
    companyData = get_tickers(headers)  

    # Example for 1st company     
    cik = companyData.iloc[0]['cik_str']
    filing_link = get_report(headers, cik)

    print(filing_link)
    # Get the filing data
    extract_data(headers, filing_link)



