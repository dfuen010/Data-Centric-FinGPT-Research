import pandas as pd
import requests
from bs4 import BeautifulSoup

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

accessNum_1 = form_4.iloc[0]['accessionNumber']
accessNum_1 = accessNum_1.replace('-', '')

xml_form4 = requests.get(
    f'https://www.sec.gov/Archives/edgar/data/{cik}/{accessNum_1}/{document_1}',
    headers=headers
    )

  
parse_form4 = pd.read_html(xml_form4.text)

# Parsing the HTML Form 4 data
soup = BeautifulSoup(xml_form4.text, 'html.parser')

# Extracting relevant information from the tables
tables = soup.find_all('table')

# Extracting data from Table I - Non-Derivative Securities Acquired, Disposed of, or Beneficially Owned
try:
    table1_rows = tables[1].find_all('tr')
    for row in table1_rows:
        columns = row.find_all('td')
        if len(columns) > 0:
            security_title = columns[0].text.strip()
            transaction_date = columns[1].text.strip()
            transaction_amount = columns[5].text.strip()
            ownership_amount = columns[7].text.strip()
            ownership_form = columns[8].text.strip()

            # Do something with extracted data
            print("Security Title:", security_title)
            print("Transaction Date:", transaction_date)
            print("Transaction Amount:", transaction_amount)
            print("Ownership Amount:", ownership_amount)
            print("Ownership Form:", ownership_form)
            print()

except IndexError:
    print("Error: Table I not found in the HTML.")

# Extracting data from Table II - Derivative Securities Acquired, Disposed of, or Beneficially Owned
try:
    table2_rows = tables[2].find_all('tr')
    for row in table2_rows:
        columns = row.find_all('td')
        if len(columns) > 0:
            derivative_title = columns[0].text.strip()
            exercise_price = columns[1].text.strip()
            transaction_date = columns[2].text.strip()
            transaction_amount = columns[6].text.strip()
            expiration_date = columns[8].text.strip()
            underlying_security_title = columns[10].text.strip()
            underlying_security_amount = columns[11].text.strip()
            price_of_derivative_security = columns[13].text.strip()
            ownership_amount = columns[14].text.strip()
            ownership_form = columns[15].text.strip()

            # Do something with extracted data
            print("Derivative Title:", derivative_title)
            print("Exercise Price:", exercise_price)
            print("Transaction Date:", transaction_date)
            print("Transaction Amount:", transaction_amount)
            print("Expiration Date:", expiration_date)
            print("Underlying Security Title:", underlying_security_title)
            print("Underlying Security Amount:", underlying_security_amount)
            print("Price of Derivative Security:", price_of_derivative_security)
            print("Ownership Amount:", ownership_amount)
            print("Ownership Form:", ownership_form)
            print()

except IndexError:
    print("Error: Table II not found in the HTML.")