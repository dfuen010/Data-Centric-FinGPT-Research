import pandas as pd
import requests

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
print(cik)

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
form_4 = allForms[allForms['form'].str.contains('4')]

document_1 = form_4.iloc[0]['primaryDocument']
print(document_1)

