# swagger_client.StreamsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stream_publish**](StreamsApi.md#stream_publish) | **POST** /{scopeId}/streams/messages | Publishes a fire-and-forget message


# **stream_publish**
> stream_publish(scope_id, body, timeout=timeout)

Publishes a fire-and-forget message

Publishes a fire-and-forget message to a topic composed of [account-name] / [client-id] / [semtantic-parts]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: kapuaAccessToken
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.StreamsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device
body = swagger_client.JsonKapuaDataMessage() # JsonKapuaDataMessage | The input request
timeout = 789 # int | The timeout of the request execution (optional)

try:
    # Publishes a fire-and-forget message
    api_instance.stream_publish(scope_id, body, timeout=timeout)
except ApiException as e:
    print("Exception when calling StreamsApi->stream_publish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device | 
 **body** | [**JsonKapuaDataMessage**](JsonKapuaDataMessage.md)| The input request | 
 **timeout** | **int**| The timeout of the request execution | [optional] 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

