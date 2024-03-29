import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from xbrl import XBRLParser, GAAP, GAAPSerializer

def getTickers(headers):
    companyTickers = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers
        )

    # dictionary to dataframe
    companyData = pd.DataFrame.from_dict(companyTickers.json(), orient='index')

    companyData['cik_str'] = companyData['cik_str'].astype(str).str.zfill(10)
    return companyData


"""
This function will get the link for the specific filing form, given the headers and cik
    args: headers, cik
    returns: filing
"""
def getFilingForm(headers, cik):
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
    
    # example for 1st form
    first_form = all_10k_forms.iloc[0]["primaryDocument"]

    accessionNumber = all_10k_forms.iloc[0]["accessionNumber"].replace("-", "")

    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber}/{first_form}"
    
def getXBRLData(filing_link):
    # Getting the XBRL data
    xbrl_data = requests.get(filing_link)

    # Parsing the XBRL data
    xbrl_parser = XBRLParser()
    xbrl = xbrl_parser.parseString(xbrl_data.text)


    return 

if __name__ == "__main__":
    headers = {'User-Agent': "email@address.com"}

    companyData = getTickers(headers)        

    filing_link = getFilingForm(headers, companyData.iloc[0]['cik_str'])
    
    