import pandas as pd
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
print(tenQ.head())
# Now we can get the 10-Q filings for Apple Inc.
# and start analyzing the data

for index, row in tenQ.iterrows():
    accessionNumber = row["accessionNumber"]
    print(accessionNumber)
    filing = requests.get(
        f"https://www.sec.gov/Archives/edgar/data/{cik}/{accessionNumber.replace('-', '')}/{accessionNumber}-index.htm",
        headers=headers,
    )
    print(filing)
    print(filing.text)
    break

# The code above will print the accession number and the response from the filing request
# The response will be a 200 status code, meaning the request was successful
# The response will contain the HTML of the filing page
# The HTML will contain the links to the 10-Q filings
# The links will be used to download the 10-Q filings
# The 10-Q filings will be used to extract the financial data
# The financial data will be used to analyze the company's financial health
# The analysis will be used to make investment decisions
