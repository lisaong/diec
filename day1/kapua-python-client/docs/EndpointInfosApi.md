# swagger_client.EndpointInfosApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_endpoint_info**](EndpointInfosApi.md#create_endpoint_info) | **POST** /{scopeId}/endpointInfos | Create a EndpointInfo
[**endpoint_info_count**](EndpointInfosApi.md#endpoint_info_count) | **POST** /{scopeId}/endpointInfos/_count | Counts the EndpointInfos
[**endpoint_info_delete**](EndpointInfosApi.md#endpoint_info_delete) | **DELETE** /{scopeId}/endpointInfos/{endpointInfoId} | Delete an EndpointInfo
[**endpoint_info_find**](EndpointInfosApi.md#endpoint_info_find) | **GET** /{scopeId}/endpointInfos/{endpointInfoId} | Get a EndpointInfo
[**endpoint_info_query**](EndpointInfosApi.md#endpoint_info_query) | **POST** /{scopeId}/endpointInfos/_query | Queries the EndpointInfos
[**endpoint_info_simple_query**](EndpointInfosApi.md#endpoint_info_simple_query) | **GET** /{scopeId}/endpointInfos | Gets the EndpointInfo list in the scope
[**endpoint_info_update**](EndpointInfosApi.md#endpoint_info_update) | **PUT** /{scopeId}/endpointInfos/{endpointInfoId} | Update a EndpointInfo


# **create_endpoint_info**
> EndpointInfo create_endpoint_info(scope_id, body)

Create a EndpointInfo

Creates a new EndpointInfo based on the information provided in EndpointInfoCreator parameter.

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the EndpointInfo
body = swagger_client.EndpointInfoCreator() # EndpointInfoCreator | Provides the information for the new EndpointInfo to be created

try:
    # Create a EndpointInfo
    api_response = api_instance.create_endpoint_info(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->create_endpoint_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the EndpointInfo | 
 **body** | [**EndpointInfoCreator**](EndpointInfoCreator.md)| Provides the information for the new EndpointInfo to be created | 

### Return type

[**EndpointInfo**](EndpointInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_info_count**
> CountResult endpoint_info_count(scope_id, body)

Counts the EndpointInfos

Counts the EndpointInfos with the given EndpointInfoQuery parameter returning the number of matching EndpointInfos

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.EndpointInfoQuery() # EndpointInfoQuery | The EndpointInfoQuery to use to filter count results

try:
    # Counts the EndpointInfos
    api_response = api_instance.endpoint_info_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->endpoint_info_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**EndpointInfoQuery**](EndpointInfoQuery.md)| The EndpointInfoQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_info_delete**
> endpoint_info_delete(scope_id, endpoint_info_id)

Delete an EndpointInfo

Deletes the EndpointInfo specified by the \"endpointInfoId\" path parameter.

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the EndpointInfo to delete.
endpoint_info_id = 'endpoint_info_id_example' # str | The id of the EndpointInfo to be deleted

try:
    # Delete an EndpointInfo
    api_instance.endpoint_info_delete(scope_id, endpoint_info_id)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->endpoint_info_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the EndpointInfo to delete. | 
 **endpoint_info_id** | **str**| The id of the EndpointInfo to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_info_find**
> EndpointInfo endpoint_info_find(scope_id, endpoint_info_id)

Get a EndpointInfo

Returns the EndpointInfo specified by the \"endpointInfoId\" path parameter.

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested EndpointInfo.
endpoint_info_id = 'endpoint_info_id_example' # str | The id of the requested EndpointInfo

try:
    # Get a EndpointInfo
    api_response = api_instance.endpoint_info_find(scope_id, endpoint_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->endpoint_info_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested EndpointInfo. | 
 **endpoint_info_id** | **str**| The id of the requested EndpointInfo | 

### Return type

[**EndpointInfo**](EndpointInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_info_query**
> EndpointInfoListResult endpoint_info_query(scope_id, body)

Queries the EndpointInfos

Queries the EndpointInfos with the given EndpointInfoQuery parameter returning all matching EndpointInfos

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.EndpointInfoQuery() # EndpointInfoQuery | The EndpointInfoQuery to use to filter results.

try:
    # Queries the EndpointInfos
    api_response = api_instance.endpoint_info_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->endpoint_info_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**EndpointInfoQuery**](EndpointInfoQuery.md)| The EndpointInfoQuery to use to filter results. | 

### Return type

[**EndpointInfoListResult**](EndpointInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_info_simple_query**
> EndpointInfoListResult endpoint_info_simple_query(scope_id, usage=usage, offset=offset, limit=limit)

Gets the EndpointInfo list in the scope

Returns the list of all the endpointInfos associated to the current selected scope.

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
usage = 'usage_example' # str | The endpointInfo usage to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the EndpointInfo list in the scope
    api_response = api_instance.endpoint_info_simple_query(scope_id, usage=usage, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->endpoint_info_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **usage** | **str**| The endpointInfo usage to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**EndpointInfoListResult**](EndpointInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_info_update**
> EndpointInfo endpoint_info_update(scope_id, endpoint_info_id, body)

Update a EndpointInfo

Updates a new EndpointInfo based on the information provided in the EndpointInfo parameter.

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
api_instance = swagger_client.EndpointInfosApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested EndpointInfo.
endpoint_info_id = 'endpoint_info_id_example' # str | The id of the requested EndpointInfo
body = swagger_client.EndpointInfo() # EndpointInfo | The modified EndpointInfo whose attributed need to be updated

try:
    # Update a EndpointInfo
    api_response = api_instance.endpoint_info_update(scope_id, endpoint_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndpointInfosApi->endpoint_info_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested EndpointInfo. | 
 **endpoint_info_id** | **str**| The id of the requested EndpointInfo | 
 **body** | [**EndpointInfo**](EndpointInfo.md)| The modified EndpointInfo whose attributed need to be updated | 

### Return type

[**EndpointInfo**](EndpointInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

