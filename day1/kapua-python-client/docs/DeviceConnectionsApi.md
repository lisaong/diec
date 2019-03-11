# swagger_client.DeviceConnectionsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_connection_count**](DeviceConnectionsApi.md#device_connection_count) | **POST** /{scopeId}/deviceconnections/_count | Counts the DeviceConnections
[**device_connection_find**](DeviceConnectionsApi.md#device_connection_find) | **GET** /{scopeId}/deviceconnections/{deviceConnectionId} | Get an DeviceConnection
[**device_connection_query**](DeviceConnectionsApi.md#device_connection_query) | **POST** /{scopeId}/deviceconnections/_query | Queries the DeviceConnections
[**device_connection_simple_query**](DeviceConnectionsApi.md#device_connection_simple_query) | **GET** /{scopeId}/deviceconnections | Gets the DeviceConnection list in the scope
[**find**](DeviceConnectionsApi.md#find) | **GET** /{scopeId}/deviceconnections/{connectionId}/options | Gets the DeviceConnection list in the scope
[**update**](DeviceConnectionsApi.md#update) | **PUT** /{scopeId}/deviceconnections/{connectionId}/options | Get an DeviceConnectionOption


# **device_connection_count**
> CountResult device_connection_count(scope_id, body)

Counts the DeviceConnections

Counts the DeviceConnections with the given DeviceConnectionQuery parameter returning the number of matching DeviceConnections

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
api_instance = swagger_client.DeviceConnectionsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.DeviceConnectionQuery() # DeviceConnectionQuery | The DeviceConnectionQuery to use to filter count results

try:
    # Counts the DeviceConnections
    api_response = api_instance.device_connection_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceConnectionsApi->device_connection_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**DeviceConnectionQuery**](DeviceConnectionQuery.md)| The DeviceConnectionQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_connection_find**
> DeviceConnection device_connection_find(scope_id, device_connection_id)

Get an DeviceConnection

Returns the DeviceConnection specified by the \"deviceConnectionId\" path parameter.

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
api_instance = swagger_client.DeviceConnectionsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested DeviceConnection.
device_connection_id = 'device_connection_id_example' # str | The id of the requested DeviceConnection

try:
    # Get an DeviceConnection
    api_response = api_instance.device_connection_find(scope_id, device_connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceConnectionsApi->device_connection_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested DeviceConnection. | 
 **device_connection_id** | **str**| The id of the requested DeviceConnection | 

### Return type

[**DeviceConnection**](DeviceConnection.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_connection_query**
> DeviceConnectionListResult device_connection_query(scope_id, body)

Queries the DeviceConnections

Queries the DeviceConnections with the given DeviceConnections parameter returning all matching DeviceConnections

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
api_instance = swagger_client.DeviceConnectionsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.DeviceConnectionQuery() # DeviceConnectionQuery | The DeviceConnectionQuery to use to filter results.

try:
    # Queries the DeviceConnections
    api_response = api_instance.device_connection_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceConnectionsApi->device_connection_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**DeviceConnectionQuery**](DeviceConnectionQuery.md)| The DeviceConnectionQuery to use to filter results. | 

### Return type

[**DeviceConnectionListResult**](DeviceConnectionListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_connection_simple_query**
> DeviceConnectionListResult device_connection_simple_query(scope_id, body=body, status=status, offset=offset, limit=limit)

Gets the DeviceConnection list in the scope

Returns the list of all the deviceConnections associated to the current selected scope.

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
api_instance = swagger_client.DeviceConnectionsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = 'body_example' # str | The client id to filter results. (optional)
status = 'status_example' # str | The connection status to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the DeviceConnection list in the scope
    api_response = api_instance.device_connection_simple_query(scope_id, body=body, status=status, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceConnectionsApi->device_connection_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | **str**| The client id to filter results. | [optional] 
 **status** | **str**| The connection status to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**DeviceConnectionListResult**](DeviceConnectionListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find**
> DeviceConnection find(scope_id, connection_id)

Gets the DeviceConnection list in the scope

Returns the list of all the deviceConnections associated to the current selected scope.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceConnectionsApi()
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
connection_id = 'connection_id_example' # str | The connection id of the requested options.

try:
    # Gets the DeviceConnection list in the scope
    api_response = api_instance.find(scope_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceConnectionsApi->find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **connection_id** | **str**| The connection id of the requested options. | 

### Return type

[**DeviceConnection**](DeviceConnection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> DeviceConnectionOption update(scope_id, connection_id, body)

Get an DeviceConnectionOption

Returns the DeviceConnectionOption specified by the given parameters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DeviceConnectionsApi()
scope_id = 'scope_id_example' # str | The ScopeId of the requested DeviceConnectionOptions.
connection_id = 'connection_id_example' # str | The id of the requested DeviceConnectionOptions
body = swagger_client.DeviceConnectionOption() # DeviceConnectionOption | The modified Device connection options whose attributed need to be updated

try:
    # Get an DeviceConnectionOption
    api_response = api_instance.update(scope_id, connection_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceConnectionsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested DeviceConnectionOptions. | 
 **connection_id** | **str**| The id of the requested DeviceConnectionOptions | 
 **body** | [**DeviceConnectionOption**](DeviceConnectionOption.md)| The modified Device connection options whose attributed need to be updated | 

### Return type

[**DeviceConnectionOption**](DeviceConnectionOption.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

