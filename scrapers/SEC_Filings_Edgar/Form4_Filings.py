import pandas as pd
import requests
from bs4 import BeautifulSoup
import io

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
# print(form_4)
document_1 = form_4.iloc[0]['primaryDocument']
# print(document_1)

accessNum_1 = form_4.iloc[0]['accessionNumber']
accessNum_1 = accessNum_1.replace('-', '')

xml_form4 = requests.get(
    f'https://www.sec.gov/Archives/edgar/data/{cik}/{accessNum_1}/{document_1}',
    headers=headers
    )
  
xml_form4 = io.StringIO(xml_form4.text)
parse_form4 = pd.read_html(xml_form4)

# Parsing the HTML Form 4 data
soup = BeautifulSoup(xml_form4, 'html.parser')
# print(soup.prettify())
# # Find all <a> elements with href containing "getcompany"
reporting_person_links = soup.find_all('a', href=lambda href: href and 'getcompany' in href)

# # Extract the text from the first link found
if reporting_person_links:
    reporting_person_name = reporting_person_links[0].text.strip()
    print("Reporting Person:", reporting_person_name)
else:
    print("Reporting Person not found in the HTML.")