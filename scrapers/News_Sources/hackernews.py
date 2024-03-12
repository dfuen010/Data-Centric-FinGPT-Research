# Use API https://github.com/HackerNews/API/tree/master
# Under the MIT License so it's OK to use it.
import requests
import pandas as pd
from multiprocessing.pool import ThreadPool

def get_item(item_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json?print=pretty"
    print(requests.get(url).json())
    return requests.get(url).json()

def combine_all_items(starting_id):
    all_possible_ids = list(range(starting_id, 0, -1))
    with ThreadPool(16) as pool:
        all_json_files = pool.map(get_item, all_possible_ids)
        pool.close()
    return all_json_files

if __name__ == "__main__":
    # Maximum item id, which is the latest item, can walk backwards to discover all items.
    url_latest_item = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"
    latest_item = requests.get(url_latest_item).json()

    # Get all items
    all_json_files = combine_all_items(latest_item)
