import pandas as pd
import requests
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer
import os
import sys

def get_tickers(headers):
    company_tickers = requests.get(
        "https://www.sec.gov/files/company_tickers.json",
        headers=headers
        )

    # dictionary to dataframe
    company_data = pd.DataFrame.from_dict(company_tickers.json(), orient='index')

    company_data['cik_str'] = company_data['cik_str'].astype(str).str.zfill(10)
    return company_data


"""
This function will get the link for the specific filing form, given the headers and cik
    args: headers, cik
    returns: filing
"""
def get_filing_form(headers, cik):
    filing_metadata = requests.get(
        f'https://data.sec.gov/submissions/CIK{cik}.json',
        headers=headers
        )

    # Getting into the filings reports
    # print(filingMetadata.json()['filings']['recent'].keys())

    all_forms = pd.DataFrame.from_dict(
        filing_metadata.json()['filings']['recent']
        )
    # Getting the 10-K filings + variations

    all_10k_forms = all_forms[all_forms['form'].str.contains('10-K|10-KT|10KSB|10KT405|10KSB40|10-K405|10-K/A')]
    
    # example for 1st form
    first_form = all_10k_forms.iloc[0]["primaryDocument"]

    accession_number = all_10k_forms.iloc[0]["accessionNumber"].replace("-", "")

    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}/{first_form}"
    
def get_xbrl_data(filing_link):
    # Getting the XBRL data
    filing_data = requests.get(filing_link, headers=headers)
    
    xbrl_parser = XBRLParser()
    sys.stdout = open(os.devnull, 'w')
    xbrl = xbrl_parser.parse(open(filing_data.content))

    # Now you can access XBRL data elements, such as GAAP and DEI data
    # For example:
    gaap_data = xbrl.get_gaap()
    dei_data = xbrl.get_dei()

    # You can serialize the data if needed
    gaap_serializer = GAAPSerializer()
    dei_serializer = DEISerializer()

    gaap_df = gaap_serializer.serialize(gaap_data)
    dei_df = dei_serializer.serialize(dei_data)

    sys.stdout = sys.__stdout__
    return gaap_df, dei_df
    

if __name__ == "__main__":
    headers = {'User-Agent': "email@address.com"}

    companyData = get_tickers(headers)        

    filing_link = get_filing_form(headers, companyData.iloc[0]['cik_str'])
    
    gaap_df,dei_df = get_xbrl_data(filing_link)