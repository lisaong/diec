# swagger_client.DataChannelsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_channel_count**](DataChannelsApi.md#data_channel_count) | **POST** /{scopeId}/data/channels/_count | Counts the ChannelInfos
[**data_channel_find**](DataChannelsApi.md#data_channel_find) | **GET** /{scopeId}/data/channels/{channelInfoId} | Gets an ChannelInfo
[**data_channel_query**](DataChannelsApi.md#data_channel_query) | **POST** /{scopeId}/data/channels/_query | Queries the ChannelInfos
[**data_channel_simple_query**](DataChannelsApi.md#data_channel_simple_query) | **GET** /{scopeId}/data/channels | Gets the ChannelInfo list in the scope


# **data_channel_count**
> CountResult data_channel_count(scope_id, body)

Counts the ChannelInfos

Counts the ChannelInfos with the given ChannelInfoQuery parameter returning the number of matching ChannelInfos

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
api_instance = swagger_client.DataChannelsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.ChannelInfoQuery() # ChannelInfoQuery | The ChannelInfoQuery to use to filter count results

try:
    # Counts the ChannelInfos
    api_response = api_instance.data_channel_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataChannelsApi->data_channel_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**ChannelInfoQuery**](ChannelInfoQuery.md)| The ChannelInfoQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_channel_find**
> ChannelInfo data_channel_find(scope_id, channel_info_id)

Gets an ChannelInfo

Gets the ChannelInfo specified by the channelInfoId path parameter

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
api_instance = swagger_client.DataChannelsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested ChannelInfo.
channel_info_id = 'channel_info_id_example' # str | The id of the requested ChannelInfo

try:
    # Gets an ChannelInfo
    api_response = api_instance.data_channel_find(scope_id, channel_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataChannelsApi->data_channel_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested ChannelInfo. | 
 **channel_info_id** | **str**| The id of the requested ChannelInfo | 

### Return type

[**ChannelInfo**](ChannelInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_channel_query**
> ChannelInfoListResult data_channel_query(scope_id, body)

Queries the ChannelInfos

Queries the ChannelInfos with the given ChannelInfoQuery parameter returning all matching ChannelInfos

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
api_instance = swagger_client.DataChannelsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.ChannelInfoQuery() # ChannelInfoQuery | The ChannelInfoQuery to use to filter results

try:
    # Queries the ChannelInfos
    api_response = api_instance.data_channel_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataChannelsApi->data_channel_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**ChannelInfoQuery**](ChannelInfoQuery.md)| The ChannelInfoQuery to use to filter results | 

### Return type

[**ChannelInfoListResult**](ChannelInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_channel_simple_query**
> ChannelInfoListResult data_channel_simple_query(scope_id, client_id=client_id, name=name, offset=offset, limit=limit)

Gets the ChannelInfo list in the scope

Returns the list of all the channelInfos associated to the current selected scope.

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
api_instance = swagger_client.DataChannelsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
client_id = 'client_id_example' # str | The client id to filter results (optional)
name = 'name_example' # str | The channel name to filter results. It allows '#' wildcard in last channel level (optional)
offset = 0 # int | The result set offset (optional) (default to 0)
limit = 50 # int | The result set limit (optional) (default to 50)

try:
    # Gets the ChannelInfo list in the scope
    api_response = api_instance.data_channel_simple_query(scope_id, client_id=client_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataChannelsApi->data_channel_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **client_id** | **str**| The client id to filter results | [optional] 
 **name** | **str**| The channel name to filter results. It allows &#39;#&#39; wildcard in last channel level | [optional] 
 **offset** | **int**| The result set offset | [optional] [default to 0]
 **limit** | **int**| The result set limit | [optional] [default to 50]

### Return type

[**ChannelInfoListResult**](ChannelInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

