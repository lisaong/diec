# swagger_client.DataClientsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_client_count**](DataClientsApi.md#data_client_count) | **POST** /{scopeId}/data/clients/_count | Counts the ClientInfos
[**data_client_find**](DataClientsApi.md#data_client_find) | **GET** /{scopeId}/data/clients/{clientInfoId} | Gets an ClientInfo
[**data_client_query**](DataClientsApi.md#data_client_query) | **POST** /{scopeId}/data/clients/_query | Queries the ClientInfos
[**data_client_simple_query**](DataClientsApi.md#data_client_simple_query) | **GET** /{scopeId}/data/clients | Gets the ClientInfo list in the scope


# **data_client_count**
> CountResult data_client_count(scope_id, body)

Counts the ClientInfos

Counts the ClientInfos with the given ClientInfoQuery parameter returning the number of matching ClientInfos

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
api_instance = swagger_client.DataClientsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.ClientInfoQuery() # ClientInfoQuery | The ClientInfoQuery to use to filter count results

try:
    # Counts the ClientInfos
    api_response = api_instance.data_client_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClientsApi->data_client_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**ClientInfoQuery**](ClientInfoQuery.md)| The ClientInfoQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_client_find**
> ClientInfo data_client_find(scope_id, client_info_id)

Gets an ClientInfo

Gets the ClientInfo specified by the clientInfoId path parameter

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
api_instance = swagger_client.DataClientsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested ClientInfo.
client_info_id = 'client_info_id_example' # str | The id of the requested ClientInfo

try:
    # Gets an ClientInfo
    api_response = api_instance.data_client_find(scope_id, client_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClientsApi->data_client_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested ClientInfo. | 
 **client_info_id** | **str**| The id of the requested ClientInfo | 

### Return type

[**ClientInfo**](ClientInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_client_query**
> ClientInfoListResult data_client_query(scope_id, body)

Queries the ClientInfos

Queries the ClientInfos with the given ClientInfoQuery parameter returning all matching ClientInfos

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
api_instance = swagger_client.DataClientsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.ClientInfoQuery() # ClientInfoQuery | The ClientInfoQuery to use to filter results

try:
    # Queries the ClientInfos
    api_response = api_instance.data_client_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClientsApi->data_client_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**ClientInfoQuery**](ClientInfoQuery.md)| The ClientInfoQuery to use to filter results | 

### Return type

[**ClientInfoListResult**](ClientInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_client_simple_query**
> ClientInfoListResult data_client_simple_query(scope_id, client_id=client_id, offset=offset, limit=limit)

Gets the ClientInfo list in the scope

Returns the list of all the clientInfos associated to the current selected scope.

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
api_instance = swagger_client.DataClientsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
client_id = 'client_id_example' # str | The client id to filter results (optional)
offset = 0 # int | The result set offset (optional) (default to 0)
limit = 50 # int | The result set limit (optional) (default to 50)

try:
    # Gets the ClientInfo list in the scope
    api_response = api_instance.data_client_simple_query(scope_id, client_id=client_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataClientsApi->data_client_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **client_id** | **str**| The client id to filter results | [optional] 
 **offset** | **int**| The result set offset | [optional] [default to 0]
 **limit** | **int**| The result set limit | [optional] [default to 50]

### Return type

[**ClientInfoListResult**](ClientInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

