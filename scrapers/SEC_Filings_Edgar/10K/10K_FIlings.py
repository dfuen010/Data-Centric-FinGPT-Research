import pandas as pd
import requests
from xbrl import XBRLParser, GAAP, GAAPSerializer, DEISerializer
from bs4 import BeautifulSoup
import os
import sys
import json

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

    filing_date = all_10k_forms.iloc[0]["filingDate"]
    report_date = all_10k_forms.iloc[0]["reportDate"]
    accession_number = all_10k_forms.iloc[0]["accessionNumber"].replace("-", "")

    return f"https://www.sec.gov/Archives/edgar/data/{cik}/{accession_number}/{first_form}", filing_date, report_date, accession_number
    
    

"""
This function will extract the page's table of contents from the filing link given
    args: soup
    returns: df
"""
def extract_page_directory(soup):
    # Getting the XBRL data
    
    specific_span = soup.find_all('span', style='background-color:rgba(0,0,0,0);color:rgba(0,0,0,1);white-space:pre-wrap;font-weight:normal;font-size:10.0pt;font-family:"Arial", sans-serif;min-width:fit-content;')

    df = pd.DataFrame(columns=['Item Number', 'Topic', 'Page Number'])
    
    for i in range(len(specific_span)):
        if "Item" in specific_span[i].text:
            df.loc[len(df)] = [str(specific_span[i].text), None, None]
        elif (specific_span[i].text).isdigit():
            if df.loc[len(df)-1, 'Page Number'] is None:
                df.loc[len(df)-1, 'Page Number'] = [specific_span[i].text]
            else:
                df.loc[len(df)-1, 'Page Number'].append(specific_span[i].text)
        else:
            if df.loc[len(df)-1, 'Topic'] is None:
                df.loc[len(df)-1, 'Topic'] = [specific_span[i].text]
            else:
                df.loc[len(df)-1, 'Topic'].append(specific_span[i].text)
        if specific_span[i].text == "109":
            break            

    return df

"""
This function will extract the sections from the page's table of contents
    args: df (table of contents)
    args: soup (filing link)
    args: filing_link, filing_date, report_date, accession_num, companytest_ticker (filing details)
    effects: creates a JSON file with the report data, split up into sections where each section is a new topic
    returns: none
"""
def extract_sections(table_contents, soup, filing_link, filing_date, report_date, accession_num, companytest_ticker):
    sections = []

    # Create a dictionary containing filing details
    filing_details = {
        "filing_link": filing_link,
        "filing_date": filing_date,
        "report_date": report_date,
        "accession_num": accession_num,
        "company_ticker": companytest_ticker
    }

    # Append filing details to the sections list
    sections.append(filing_details)

    span_texts = soup.find_all('span')

    for i in range(len(table_contents)):
        section_titles = table_contents.loc[i, 'Topic']
        page_numbers = table_contents.loc[i, 'Page Number']
        item_number = table_contents.loc[i, 'Item Number']

        if i == len(table_contents) - 1:
            next_item_with_title_abbr = "NONE"
        else:
            next_item_with_title_abbr = table_contents.loc[i + 1, 'Item Number'] + " " + table_contents.loc[i + 1, 'Topic'][0][0]

        for title, page_number in zip(section_titles, page_numbers):
            item_with_title_abbr = item_number + " " + title[0]
            found_starting_point = False
            section_text = []

            for span in span_texts:
                if found_starting_point:
                    if next_item_with_title_abbr.upper() in span.text:
                        break
                    else:
                        section_text.append(span.text.strip())
                else:
                    if item_with_title_abbr.upper() in span.text:
                        found_starting_point = True

            sections.append({
                "title": title,
                "page_number": page_number,
                "text": "\n".join(section_text)
            })

    # Write the sections data along with filing details to the JSON file
    file_name = f"{companytest_ticker}_10kfiling_{filing_date}.json"
    with open(file_name, 'w', encoding='utf-8') as json_file:
        json.dump(sections, json_file, ensure_ascii=False, indent=4)

        

if __name__ == "__main__":
    headers = {'User-Agent': "email@address.com"}

    # Get all the tickers
    companyData = get_tickers(headers)        

    # Creating a test company for smaller scale first
    companytest = companyData.iloc[0]['cik_str']
    companytest_ticker = companyData.iloc[0]['ticker']
    
    filing_link, filing_date, report_date, accession_num = get_filing_form(headers, companytest)

    filing_data = requests.get(filing_link, headers=headers)
    
    soup = BeautifulSoup(filing_data.text, features="xml")
    
    table_contents = extract_page_directory(soup)

    extract_sections(table_contents, soup, filing_link, filing_date, report_date, accession_num, companytest_ticker)


