from cnbc import APIWrapper, Endpoints
import json
import csv

# Initialize the APIWrapper to the TRANSLATE endpoint
api_wrapper = APIWrapper(
    # RapidAPI API key
    api_key='4d6d8e080bmsh68dcf84f504154ap1335bbjsn0a70ea825650',
    endpoint=Endpoints.LIST_SYMBOL_NEWS
)

# Grab the earnings chart for Apple Inc. (AAPL) (issueId: 36276)
api_wrapper_params = api_wrapper.params

api_wrapper_params['symbol'] = 'AAPL'
api_wrapper_params['page'] = 1
api_wrapper_params['pageSize'] = 50
response = api_wrapper.request()

# Convert the response dict to a JSON string
response_json = json.dumps(response, indent=4)

# Save the response to a file
with open('./datasets/News/cnbc/cnbc_aapl_news.json', 'w') as f:
    f.write(response_json)

# From the json, convert the response to a dataset of news articles, each with the following fields:
# - headline: The headline of the article
# - url: The URL of the article
# - timestamp: The timestamp of the article
# - tags: The tags of the article
# - summary: The summary of the article
# Extracting articles and creating dataset
data = json.loads(response_json)
articles = data["data"]["symbolEntries"]["results"]
dataset = []

for article in articles:
    headline = article["headline"]
    url = article["url"]
    timestamp = article["dateLastPublished"]
    tags = article["relatedTagsFilteredFormatted"].split("|")
    summary = article["description"],
    ticker_symbols = [symbol["symbol"] for symbol in article["tickerSymbols"]]
    
    dataset.append({
        "headline": headline,
        "url": url,
        "timestamp": timestamp,
        "tags": tags,
        "summary": summary,
        "ticker_symbols": ticker_symbols
    })
    
csv_columns = ["headline", "url", "timestamp", "tags", "summary", "ticker_symbols"]

# Create a csv file from the dataset
keys = dataset[0].keys()
with open('./datasets/News/cnbc/cnbc_aapl_news.csv', 'w', newline='') as f:
    dict_writer = csv.DictWriter(f, keys)
    dict_writer.writeheader()
    dict_writer.writerows(dataset)


# Get fundamentals chart for Apple Inc. (AAPL) (issueId: 36276)
api_wrapper.endpoint = Endpoints.GET_FUNDAMENTALS
api_wrapper_params = api_wrapper.params
api_wrapper_params['issueIds'] = 36276
response = api_wrapper.request()

# Convert the response dict to a JSON string
response_json = json.dumps(response, indent=4)

# Save the response to a file
with open('./datasets/News/cnbc/cnbc_aapl_fundamentals.json', 'w') as f:
    f.write(response_json)

# From the json, convert the response to a dataset of fundamentals, each with the following fields:
# - name: The name of the fundamental
# - value: The value of the fundamental
data = json.loads(response_json)

# Extracting relevant information
stock_id = list(data.keys())[0]
ranges = data[stock_id]["Ranges"]
values = data[stock_id]["Values"]

# Writing data to CSV file
csv_columns = ["Name", "HighValue", "HighValueRaw", "HighDate", "LowValue", "LowValueRaw", "LowDate"]
csv_file = "./datasets/News/cnbc/cnbc_aapl_fundamentals_ranges.csv"

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in ranges:
        writer.writerow(item)

csv_columns = ["Name", "Value", "SectorAvg", "SectorHigh", "SectorLow", "IndustryAvg", "IndustryHigh", "IndustryLow", "RawValue", "PerfDate" ]
csv_file = "./datasets/News/cnbc/cnbc_aapl_fundamentals_values.csv"

with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    for item in values:
        writer.writerow(item)