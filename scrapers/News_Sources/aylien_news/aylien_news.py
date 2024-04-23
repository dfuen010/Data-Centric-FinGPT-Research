from __future__ import print_function

import time
import aylien_news_api
from aylien_news_api.rest import ApiException
from pprint import pprint

configuration = aylien_news_api.Configuration(
    host="https://api.aylien.com/news"
)

configuration = aylien_news_api.Configuration(
    host="https://api.aylien.com/news",
    api_key={
        'app_id': '720ad7a9'
    }
)

configuration = aylien_news_api.Configuration(
    host="https://api.aylien.com/news",
    api_key={
        'app_key': '490ab930b4123fa941e670b8895f76d0'
    }
)

with aylien_news_api.ApiClient(configuration) as api_client:
    api_instance = aylien_news_api.DefaultApi(api_client)
    unknown_base_type = {"$and":[{"$or":[{"body":{"$text":"Tim Cook"}},{"social.shares.count.reddit.max":{"$gte":5000,"$boost":5}}]},{"entity":{"$and":[{"name":{"$text":"Apple","$boost":2}},{"$not":[{"type":{"$eq":"Fruit"}}]}]}}]}
published_at_start = 'published_at_start_example'
published_at_end = 'published_at_end_example'
_return = ['_return_example']
sort_by = 'published_at'
sort_direction = 'desc'
cursor = '*'
per_page = 10

try:
    api_response = api_instance.advanced_list_stories(unknown_base_type, published_at_start=published_at_start, published_at_end=published_at_end, _return=_return, sort_by=sort_by, sort_direction=sort_direction, cursor=cursor, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->advanced_list_stories: %s\n" % e)
