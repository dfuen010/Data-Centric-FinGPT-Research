import requests
import pandas as pd
from multiprocessing.pool import ThreadPool
import time

def fetch_latest_item_id():
    url_latest_item = "https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty"
    try:
        latest_item = requests.get(url_latest_item).json()
        return latest_item
    except Exception as e:
        print(f"Failed to fetch latest item ID: {e}")
        return None

def get_item(item_id):
    headers = {'User-Agent': "email@address.com",
               'Content-Type': 'application/json',
               'accept': 'application/json'}
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json?print=pretty"
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to fetch item {item_id}: HTTP Error {response.status_code}: {response.reason}")
            return None
    except Exception as e:
        print(f"Failed to fetch item {item_id}: {e}")
        return None

def fetch_multiple_items(item_ids):
    with ThreadPool(20) as pool:
        all_json_files = pool.map(get_item, item_ids)
        pool.close()
    return all_json_files

def save_to_json(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_json(filename, orient="records", lines=True)
        print(f"Data saved to {filename}.")
    except Exception as e:
        print(f"Failed to save data to {filename}: {e}")

if __name__ == "__main__":
    latest_item_id = fetch_latest_item_id()
    if latest_item_id:
        print("Fetching Hacker News items...")
        start = time.time()

        # Generate a list of item IDs to fetch, starting from the latest item ID
        item_ids = list(range(latest_item_id, latest_item_id - 200, -1))

        # Fetch details of multiple items concurrently
        all_items = fetch_multiple_items(item_ids)

        end = time.time()
        print(f"Fetched {len(all_items)} items in {end - start:.2f} seconds.")

        # Filter out None values (failed requests)
        all_items = [item for item in all_items if item is not None]

        print(f"Successfully fetched {len(all_items)} items.")

        if all_items:
            save_to_json(all_items, "hackernews.json")
        else:
            print("No data to save.")
    else:
        print("Failed to fetch the latest item ID. Exiting.")
