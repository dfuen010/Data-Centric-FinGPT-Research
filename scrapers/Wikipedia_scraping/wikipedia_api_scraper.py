import wikipediaapi
import requests
import re
import random
import requests
import json

# file for writing the text data we obtain from wikipedia
output_file = open("wikipedia_data.txt", "w")


# main code for scraping wikipedia 
if __name__ == "__main__":
    def write_by_sections(sections, output_file, page_data, level=0):
        for s in sections:
            encoded_title = " ".join(re.split("[^A-Za-z0-9]+", s.title)) 
            output_file.write("{}: {} \n\n".format("*" * (level + 1), encoded_title))
            encoded_text = " ".join(re.split("[^A-Za-z0-9]+", s.text)) 
            
            page_data["sections"][encoded_title] = {"text": encoded_text, "sections": {}}
            output_file.write("{} \n\n".format(encoded_text))

            # pass in for the json dictionary the new section of the page in recursion call
            write_by_sections(s.sections, output_file, page_data["sections"][encoded_title], level + 1)

    # create a wikipedia object using the API with our user agent
    # this wikipedia object initalization creates our request to the wikipedia API using the User-Agent as the header
    # requested in their documentation
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='Data-Centric/0.0 (https://github.com/dfuen010/; dfuen010@gmail.com)',
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    # We will scrape 200 pages from wikipedia to start with this scraper starting with the wiki page for python
    pages = 200
    i = 0
    page_string = "Bank"
    # specifies a page to scrape text from 
    current_page = wiki_wiki.page(page_string)

    # dictionary to store wiki page information as a dictionary to convert to a JSON format (better storage for text information
    # for ML purposes)
    wiki_data = {}

    # let's have an array that keeps track of the pages we have visited in the case we go to dead end (page with no link)
    visited_pages = []
    while i != pages:

        i += 1
        page_text = current_page.text
        encoded_title = " ".join(re.split("[^A-Za-z0-9]+", current_page.title)) 
        output_file.write("Page Title - " + encoded_title + "\n\n")
        # remove any non-ascii values that may appear from the page text 
        encoded_text = " ".join(re.split("[^A-Za-z0-9]+", page_text)) 
        # add title and its text and sections to dictionary for JSON format
        wiki_data[encoded_title] = {"text": encoded_text, "sections": {}}
        write_by_sections(current_page.sections, output_file, wiki_data[encoded_title])

        # next let's get the links to next pages and go to the next page and continue this loop
        links = current_page.links
        # let's go to a random page in our list of links
        if len(links) != 0:
            link_to_visit = random.choice(list(links.keys()))
            current_page = links[link_to_visit]
            visited_pages.append(current_page)
            output_file.write("\n\n")
        else:
            # if there are any pages on our stack and we go to the previous and select a different link
            if visited_pages:
                current_page = visited_pages.pop()
            else:
                # we have no more pages to go back to so we break out
                break
        

    output_file.close()
    # Convert the dictionary to JSON format for better storage of text data
    with open("wikipedia_data.json", "w") as json_file:
        json.dump(wiki_data, json_file, indent=4)