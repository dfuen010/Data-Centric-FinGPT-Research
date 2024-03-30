import pandas as pd
import requests
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer
from bs4 import BeautifulSoup
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
    
    
def extract_page_directory(filing_link):
    # Getting the XBRL data
    filing_data = requests.get(filing_link, headers=headers)
    
    soup = BeautifulSoup(filing_data.text, features="xml")
    # with open('table_of_contents.txt', 'w', encoding='utf-8') as file:
    #     file.write(soup.prettify()) 
   
    specific_span = soup.find_all('span', style='background-color:rgba(0,0,0,0);color:rgba(0,0,0,1);white-space:pre-wrap;font-weight:normal;font-size:10.0pt;font-family:"Arial", sans-serif;min-width:fit-content;')

    df = pd.DataFrame(columns=['Item Number', 'Topic', 'Page Number'])
    
    for i in range(len(specific_span)):
        if "Item" in specific_span[i].text:
            df.loc[len(df)] = [str(specific_span[i].text), None, None]
        elif specific_span[i].text == "[Reserved]":
            continue
        elif (specific_span[i].text).isdigit():
            df.loc[len(df)-1, 'Page Number'] = specific_span[i].text
        else:
            if df.loc[len(df)-1, 'Topic'] is None:
                df.loc[len(df)-1, 'Topic'] = [specific_span[i].text]
            else:
                df.loc[len(df)-1, 'Topic'].append(specific_span[i].text)
        if specific_span[i].text == "109":
            break            

    return df
    

if __name__ == "__main__":
    headers = {'User-Agent': "email@address.com"}

    companyData = get_tickers(headers)        

    filing_link = get_filing_form(headers, companyData.iloc[0]['cik_str'])
    
    df = extract_page_directory(filing_link)
    
    df.to_csv('10k_microsoft.csv', index=False)
