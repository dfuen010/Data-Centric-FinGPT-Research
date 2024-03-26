'''
Scraper for wikipedia using BeautifulSoup (for initial scraping, might potentially change)

The license in which wikipedia's data allows it's distribution of data in any medium
'''

# import required modules
from bs4 import BeautifulSoup, SoupStrainer
import requests
import pandas
 
# get Base URL for wikipedia
landing_page = "https://en.wikipedia.org/wiki/Main_Page"

# file for writing the text data
output_file = open("wikipedia_data.txt", "w")
 
# making a function that attempts to move to other pages of wikipedia to scrape data
# scrapping the current page as well
def scrape_page(url, file):
    print ("URL: " + url)
    r = requests.get(url)
    # get the base url of the link (slice after the first / after https://)
    source_url = url[8:]
    # strip to only get base link for moving to other pages
    source_url = source_url[:source_url.index('/')]
    print(source_url)
    soup = BeautifulSoup(r.content, "html.parser")
    get_data(soup)
    # get any links to other wiki pages here
    found_web_links = soup.select('a')
    actual_web_links = [web_link['href'] for web_link in found_web_links] 
    links_to_scrape = []
    for link in actual_web_links:
        if link.startswith("/wiki"):
            links_to_scrape.append(link)
            #print(link)
    if len(links_to_scrape) != 0:
        next_page = url[:8] + source_url + links_to_scrape[1]
        if next_page == url:
            pass
        #print(next_page)
        scrape_page(next_page, file)
    else:
        print ("Done")
    text = soup.find_all("p")
    file.write(str(text))
    file.close()

# function to get all text data found in the html using the 'p' paragraph tag and return it 
def get_data(soup):
    list(soup.children)
 
    # find all occurrence of p in HTML
    # includes HTML tags
    # testing
    # print(soup.find_all('p'))
    
    print('\n\n')
    
    # return only text
    # does not include HTML tags
    return soup.find_all('p')[0].get_text()


if __name__ == "__main__":
    scrape_page(landing_page, output_file)