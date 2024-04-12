from cnbc import APIWrapper, Endpoints
import json
import csv

# Initialize the APIWrapper to the TRANSLATE endpoint
api_wrapper = APIWrapper(
    # RapidAPI API key
    api_key='4d6d8e080bmsh68dcf84f504154ap1335bbjsn0a70ea825650',
    endpoint=Endpoints.TRANSLATE
)

# Grab the 50 most trending news articles on CNBC
api_wrapper.endpoint = Endpoints.LIST_TRENDING_NEWS
api_wrapper_params = api_wrapper.params
print(api_wrapper_params)
api_wrapper_params['count'] = 50
response = api_wrapper.request()

# Convert the response dict to a JSON string
response_json = json.dumps(response, indent=4)

# Save the response to a file
with open('./scrapers/cnbc/trending_news.json', 'w') as f:
	f.write(response_json)

# From the json, convert the response to a dataset of news articles, each with the following fields:
# - headline: The headline of the article
# - url: The URL of the article
# - timestamp: The timestamp of the article
# - tags: The tags of the article
# - summary: The summary of the article
# Extracting articles and creating dataset
data = json.loads(response_json)
articles = data["data"]["mostPopularEntries"]["assets"]
dataset = []

for article in articles:
    headline = article["shorterHeadline"]
    url = article["url"]
    timestamp = article["dateLastPublished"]
    tags = article["relatedTagsFilteredFormatted"].split("|")
    summary = article["description"]
    
    dataset.append({
        "headline": headline,
        "url": url,
        "timestamp": timestamp,
        "tags": tags,
        "summary": summary
    })

# Create a csv file from the dataset
keys = dataset[0].keys()
with open('./scrapers/cnbc/trending_news.csv', 'w', newline='') as f:
	dict_writer = csv.DictWriter(f, keys)
	dict_writer.writeheader()
	dict_writer.writerows(dataset)