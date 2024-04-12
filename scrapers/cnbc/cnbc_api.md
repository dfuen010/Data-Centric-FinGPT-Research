# CNBC API SETUP

## Set up:

`pip install cnbc`

## How to use CNBC API

### APIWrapper

The APIWrapper class is used to make requests to the CNBC API.

```
from cnbc import APIWrapper, Endpoints

api_wrapper = APIWrapper(
    api_key='YOUR_API_KEY',
    endpoint=Endpoints.TRANSLATE
)

# The APIWrapper class will supply the required parameters for the configured CNBC API endpoint.
api_wrapper_params = api_wrapper.params
api_wrapper_params['symbol'] = 'AAPL'
# The APIWrapper class will make a request to the CNBC API and return the response in JSON.
json_response = api_wrapper.request()

# The APIWrapper class can be repurposed to make multiple requests to the CNBC API.
api_wrapper.endpoint = Endpoints.GET_SUMMARY
api_wrapper_params = api_wrapper.params
api_wrapper_params['issueIds'] = json_response['issueId']
json_response = api_wrapper.request()
```

### Translate Endpoint

A majority of the CNBC API endpoints require an `issueId` or `issueIds` parameter. The translate endpoint is used to convert a symbol to an `issueId`.

The APIWrapper class contains a translation table which can be loaded and saved to a file to reduce the number of requests to the CNBC API.
`api_wrapper.translation_table_save('translation_table.json')`
