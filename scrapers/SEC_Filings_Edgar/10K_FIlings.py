import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent': "email@address.com"}

companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
    )

# dictionary to dataframe
companyData = pd.DataFrame.from_dict(companyTickers.json(),
                                     orient='index')

companyData['cik_str'] = companyData['cik_str'].astype(
                           str).str.zfill(10)


# example for 1st company
cik = companyData.iloc[0]['cik_str']

filingMetadata = requests.get(
    f'https://data.sec.gov/submissions/CIK{cik}.json',
    headers=headers
    )

# Getting into the filings reports
# print(filingMetadata.json()['filings']['recent'].keys())

allForms = pd.DataFrame.from_dict(
             filingMetadata.json()['filings']['recent']
             )

# Getting the 10-K filings + variations
all_10k_forms = allForms[allForms['form'].str.contains('10-K|10-KT|10KSB|10KT405|10KSB40|10-K405|10-K/A')]
print(all_10k_forms.head())

first_form = all_10k_forms.iloc[0]["primaryDocument"]

accessionNumber = all_10k_forms.iloc[0]["accessionNumber"].replace("-", "")

filing = requests.get(
    f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber}/{first_form}",
    headers=headers
    )

tables = pd.read_html(filing.text)
print(tables)