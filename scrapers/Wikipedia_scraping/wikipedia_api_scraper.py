import wikipediaapi
import requests
import re

import requests

# file for writing the text data we obtain from wikipedia
output_file = open("wikipedia_data.txt", "w")


# main code for scraping wikipedia 
if __name__ == "__main__":

    def get_links(page):
        links = page.links
        print(links)
        #for title in sorted(links.keys()):
        #    print("%s: %s" % (title, links[title]))


    # create a wikipedia object using the API with our user agent
    # this wikipedia object initalization creates our request to the wikipedia API using the User-Agent as the header
    # requested in their documentation
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='Data-Centric/0.0 (https://github.com/dfuen010/; dfuen010@gmail.com)',
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    # specifies a page to scrape text from 
    page_text = wiki_wiki.page('Python_(programming_language)').text
    encoded_text = " ".join(re.split("[^A-Za-z0-9]+", page_text)) 
    output_file.write(encoded_text)

    output_file.close()