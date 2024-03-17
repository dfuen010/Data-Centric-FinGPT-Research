# import required modules
from bs4 import BeautifulSoup
import requests
 
# get URL
landing_page = "https://en.wikipedia.org/wiki/Main_Page"
 
# making a function that attempts to move to other pages of wikipedia to scrape data
def scrape_page(url):
    print ("URL: " + url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    next_page_link = soup.find("a", class_="next")
    if next_page_link is not None:
        href = next_page_link.get("href")
        scrape_page(href)
    else:
        print ("Done")

def get_data(soup):
    list(soup.children)
 
    # find all occurrence of p in HTML
    # includes HTML tags
    print(soup.find_all('p'))
    
    print('\n\n')
    
    # return only text
    # does not include HTML tags
    print(soup.find_all('p')[0].get_text())

    return soup.find_all('p')[0].get_text()

scrape_page(landing_page)