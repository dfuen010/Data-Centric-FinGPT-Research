import requests
#free api not accessible
API_KEY = ""
API_ENDPOINT = "https://api.newsfilter.io/search?token={}".format()

# Define the news search parameters
queryString = "symbols:NFLX AND publishedAt:[2020-02-01 TO 2020-05-20]"

payload = {
    "queryString": queryString,
    "from": 0,
    "size": 10
}

# Send the search query to the Search API
response = requests.post(API_ENDPOINT, json=payload)

# Read the response
articles = response.json()

print(articles)