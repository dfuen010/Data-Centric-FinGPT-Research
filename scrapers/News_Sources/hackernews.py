"""
Use API https://github.com/HackerNews/API/tree/master
https://www.kaggle.com/datasets/hacker-news/hacker-news/data?select=full Public dataset available, but last updated in 2022, last ID: 33620611
Under the MIT License so it's open source data.
"""
import requests
import pandas as pd
from multiprocessing.pool import ThreadPool
import time


def get_item(item_id):
    headers = {'User-Agent': "email@address.com",
               'Content-Type': 'application/json',
               'accept': 'application/json'}
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json?print=pretty"
    return requests.get(url, headers=headers).json()

def combine_all_items(starting_id):
    last_id = 33620611
    all_possible_ids = list(range(starting_id, starting_id-200, -1))
    with ThreadPool(20) as pool:
        all_json_files = pool.map(get_item, all_possible_ids)
        pool.close()
    return all_json_files

if __name__ == "__main__":
    # Maximum item id, which is the latest item, can walk backwards to discover all items.
    url_latest_item = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"
    latest_item = requests.get(url_latest_item).json()

    start = time.time()

    # Get all items
    all_json_files = combine_all_items(latest_item)
    
    end = time.time()
    print(end - start)
    
    # Convert to dataframe
    df = pd.DataFrame(all_json_files)
    df.to_json("hackernews.json", orient="records", lines=True)
