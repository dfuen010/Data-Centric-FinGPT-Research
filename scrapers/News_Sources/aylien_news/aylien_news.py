from __future__ import print_function
import aylien_news_api
from aylien_news_api.rest import ApiException

# Configure Aylien News API
configuration = aylien_news_api.Configuration(
    host="https://api.aylien.com/news",
    api_key={
        'app_id': '720ad7a9',
        'app_key': '490ab930b4123fa941e670b8895f76d0'
    }
)

# Create API client
with aylien_news_api.ApiClient(configuration) as api_client:
    api_instance = aylien_news_api.DefaultApi(api_client)
    
    # Define query parameters
    query = {
        "$and": [
            {
                "$or": [
                    {"body": {"$text": "Tim Cook"}},
                    {"social.shares.count.reddit.max": {"$gte": 5000, "$boost": 5}}
                ]
            },
            {
                "entity": {
                    "$and": [
                        {"name": {"$text": "Apple", "$boost": 2}},
                        {"$not": [{"type": {"$eq": "Fruit"}}]}
                    ]
                }
            }
        ]
    }
    per_page = 10
    sort_by = 'published_at'
    sort_direction = 'desc'

    try:
        # Call the API to get article information
        api_response = api_instance.advanced_list_stories(
            query,
            per_page=per_page,
            sort_by=sort_by,
            sort_direction=sort_direction
        )
        
        # Extract and print article information
        for article in api_response.stories:
            print("Title:", article.title)
            print("Source:", article.source.name)
            print("Published At:", article.published_at)
            print("Summary:", article.summary)
            print("URL:", article.links.permalink)
            print()
    except ApiException as e:
        print("Exception when calling DefaultApi->advanced_list_stories: %s\n" % e)
