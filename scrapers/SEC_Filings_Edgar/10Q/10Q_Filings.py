import pandas as pd
from bs4 import BeautifulSoup
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer
import requests

def main():
    cik, headers = grab_apple_ticker()
    ten_q = get_filing_metadata(cik, headers)
    print(ten_q)
    parse_filings(ten_q, headers)

    # Get the XBRL data for the 10-Q filing
    # parse_xbrl_data("0000320193-21-000056")

def grab_apple_ticker():
    headers = {"User-Agent": "email@address.com"}

    company_tickers = requests.get(
        "https://www.sec.gov/files/company_tickers.json", headers=headers
    )

    company_data = pd.DataFrame.from_dict(company_tickers.json(), orient="index")

    company_data["cik_str"] = company_data["cik_str"].astype(str).str.zfill(10)


    # Apple Inc.
    cik = company_data.iloc[1]["cik_str"]
    print("Apple Inc. CIK: ", cik)
    return cik, headers

# All keys for the filings
# print(filingMetadata.json()["filings"]["recent"].keys())
# dict_keys(['accessionNumber', 'filingDate', 'reportDate', 'acceptanceDateTime', 'act', 'form', 'fileNumber', 'filmNumber', 'items', 'size', 'isXBRL', 'isInlineXBRL', 'primaryDocument', 'primaryDocDescription'])

def get_filing_metadata(cik, headers):
    filing_metadata = requests.get(
        f"https://data.sec.gov/submissions/CIK{cik}.json", headers=headers
    )

    all_forms = pd.DataFrame.from_dict(filing_metadata.json()["filings"]["recent"])

    # Getting the 10-Q filings
    ten_q = all_forms[all_forms["form"].str.contains("10-Q|10Q")]
    ten_q.to_csv("10Q_apple_filings.csv")

    return ten_q

def parse_filings(ten_q, headers):
    for i in range(0, len(ten_q)):
        acceptance_date_time = ten_q.iloc[i]["acceptanceDateTime"]
        acceptance_year = acceptance_date_time[:4]
        accession_number = ten_q.iloc[i]["accessionNumber"]
        accession_number = accession_number.replace("-", "")
        parse_xbrl_data(accession_number, headers)

# Getting the XBRL data for the 10-Q filing based on the accession number
def parse_xbrl_data(accession_number, headers):
    xbrl_filing = requests.get(
        f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}/{doc}",
        headers=headers,
    )

    xbrl_soup = BeautifulSoup(xbrl_filing.text, features="xml")

    xbrl_parser = XBRLParser()

    xbrl = xbrl_parser.parse(xbrl_soup)

    gaap_obj = xbrl_parser.parseGAAP(xbrl, doc)

    gaap_serializer = GAAPSerializer()

    gaap_data = gaap_serializer.serialize(gaap_obj)

    return gaap_data
