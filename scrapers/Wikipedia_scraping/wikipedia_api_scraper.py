import wikipediaapi
import requests
import re
import random
import requests

# file for writing the text data we obtain from wikipedia
output_file = open("wikipedia_data.txt", "w")


# main code for scraping wikipedia 
if __name__ == "__main__":
    def write_by_sections(sections, output_file, level=0):
        for s in sections:
            output_file.write("{}: {} \n\n".format("*" * (level + 1), s.title))
            encoded_text = " ".join(re.split("[^A-Za-z0-9]+", s.text)) 
            output_file.write("{} \n\n".format(encoded_text))
            write_by_sections(s.sections, output_file, level + 1)

    # create a wikipedia object using the API with our user agent
    # this wikipedia object initalization creates our request to the wikipedia API using the User-Agent as the header
    # requested in their documentation
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='Data-Centric/0.0 (https://github.com/dfuen010/; dfuen010@gmail.com)',
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    # We will scrape 100 pages from wikipedia to start with this scraper starting with the wiki page for python
    pages = 100
    i = 0
    page_string = 'Python_(programming_language)'
    # specifies a page to scrape text from 
    current_page = wiki_wiki.page(page_string)
    while i != pages:

        i += 1
        page_text = current_page.text
        output_file.write("Page Title - " + current_page.title + "\n\n")
        # remove any non-ascii values that may appear from the page text 
        encoded_text = " ".join(re.split("[^A-Za-z0-9]+", page_text)) 
        write_by_sections(current_page.sections, output_file)

        # next let's get the links to next pages and go to the next page and continue this loop
        links = current_page.links
        # let's go to a random page in our list of links
        if len(links) != 0:
            link_to_visit = random.choice(list(links.keys()))
            current_page = links[link_to_visit]
            output_file.write("\n\n")
        else:
            # if there are no external links we'll stop for now
            break
        
        

    output_file.close()