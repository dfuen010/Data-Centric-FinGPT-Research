import pandas as pd
import requests

headers = {"User-Agent": "email@address.com"}

companyTickers = requests.get(
    "https://www.sec.gov/files/company_tickers.json", headers=headers
)

companyData = pd.DataFrame.from_dict(companyTickers.json(), orient="index")

companyData["cik_str"] = companyData["cik_str"].astype(str).str.zfill(10)


cik = companyData.iloc[0]["cik_str"]
print(cik)

filingMetadata = requests.get(
    f"https://data.sec.gov/submissions/CIK{cik}.json", headers=headers
)

# Getting into the filings reports
print(filingMetadata.json()["filings"]["recent"].keys())

allForms = pd.DataFrame.from_dict(filingMetadata.json()["filings"]["recent"])

# Getting the 10-Q filings + variations
tenQ = allForms[
    allForms["form"].str.contains("10-Q|10-QT|10QSB|10QSB40|10-Q405|10-Q/A")
]
print(tenQ.head())
