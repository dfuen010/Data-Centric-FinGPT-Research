import pandas as pd
from bs4 import BeautifulSoup
import requests


headers = {"User-Agent": "email@address.com"}

companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json", headers=headers
)

companyData = pd.DataFrame.from_dict(companyTickers.json(), orient="index")

companyData["cik_str"] = companyData["cik_str"].astype(str).str.zfill(10)


# Apple Inc.
cik = companyData.iloc[1]["cik_str"]
print("Apple Inc. CIK: ", cik)

filingMetadata = requests.get(
    f"https://data.sec.gov/submissions/CIK{cik}.json", headers=headers
)
# All keys for the filings
# print(filingMetadata.json()["filings"]["recent"].keys())
# dict_keys(['accessionNumber', 'filingDate', 'reportDate', 'acceptanceDateTime', 'act', 'form', 'fileNumber', 'filmNumber', 'items', 'size', 'isXBRL', 'isInlineXBRL', 'primaryDocument', 'primaryDocDescription'])

allForms = pd.DataFrame.from_dict(filingMetadata.json()["filings"]["recent"])

# Getting the 10-Q filings
tenQ = allForms[allForms["form"].str.contains("10-Q|10Q")]

# Print all of the 10-Q filings
print(tenQ)

doc = tenQ.iloc[0]["primaryDocument"]
print(doc)

accessionNumber = tenQ.iloc[0]["accessionNumber"]
accessionNumber = accessionNumber.replace("-", "")
print(accessionNumber)

filing = requests.get(
    f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber}/{doc}",
    headers=headers,
)

parsed_filing = BeautifulSoup(filing.text, "lxml")

shares_tag = parsed_filing.find("ix:nonfraction", {"unitref": "shares"})
print(shares_tag.text.strip())
