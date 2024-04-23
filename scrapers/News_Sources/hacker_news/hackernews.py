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
    url_latest_item = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"
    try:
        latest_item = requests.get(url_latest_item).json()
    except Exception as e:
        print(f"Failed to fetch latest item ID: {e}")
        latest_item = 33620611  # Fallback to the last known ID
    
    start = time.time()
    print("Fetching Hacker News items...")

    all_json_files = combine_all_items(latest_item)

    end = time.time()
    print(f"Fetched {len(all_json_files)} items in {end - start:.2f} seconds.")

    # Filter out None values (failed requests)
    all_json_files = [item for item in all_json_files if item is not None]

    print(f"Successfully fetched {len(all_json_files)} items.")

    if all_json_files:
        df = pd.DataFrame(all_json_files)
        df.to_json("hackernews.json", orient="records", lines=True)
        print("Data saved to hackernews.json.")
    else:
        print("No data to save.")
