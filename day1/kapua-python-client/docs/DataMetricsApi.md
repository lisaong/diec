# swagger_client.DataMetricsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_metric_count**](DataMetricsApi.md#data_metric_count) | **POST** /{scopeId}/data/metrics/_count | Counts the MetricInfos
[**data_metric_find**](DataMetricsApi.md#data_metric_find) | **GET** /{scopeId}/data/metrics/{metricInfoId} | Gets an MetricInfo
[**data_metric_query**](DataMetricsApi.md#data_metric_query) | **POST** /{scopeId}/data/metrics/_query | Queries the MetricInfos
[**data_metric_simple_query**](DataMetricsApi.md#data_metric_simple_query) | **GET** /{scopeId}/data/metrics | Gets the MetricInfo list in the scope


# **data_metric_count**
> CountResult data_metric_count(scope_id, body)

Counts the MetricInfos

Counts the MetricInfos with the given MetricInfoQuery parameter returning the number of matching MetricInfos

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
api_instance = swagger_client.DataMetricsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.MetricInfoQuery() # MetricInfoQuery | The MetricInfoQuery to use to filter count results

try:
    # Counts the MetricInfos
    api_response = api_instance.data_metric_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMetricsApi->data_metric_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**MetricInfoQuery**](MetricInfoQuery.md)| The MetricInfoQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_metric_find**
> MetricInfo data_metric_find(scope_id, metric_info_id)

Gets an MetricInfo

Gets the MetricInfo specified by the metricInfoId path parameter

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
api_instance = swagger_client.DataMetricsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested MetricInfo.
metric_info_id = 'metric_info_id_example' # str | The id of the requested MetricInfo

try:
    # Gets an MetricInfo
    api_response = api_instance.data_metric_find(scope_id, metric_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMetricsApi->data_metric_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested MetricInfo. | 
 **metric_info_id** | **str**| The id of the requested MetricInfo | 

### Return type

[**MetricInfo**](MetricInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_metric_query**
> MetricInfoListResult data_metric_query(scope_id, body)

Queries the MetricInfos

Queries the MetricInfos with the given MetricInfoQuery parameter returning all matching MetricInfos

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
api_instance = swagger_client.DataMetricsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.MetricInfoQuery() # MetricInfoQuery | The MetricInfoQuery to use to filter results

try:
    # Queries the MetricInfos
    api_response = api_instance.data_metric_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMetricsApi->data_metric_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**MetricInfoQuery**](MetricInfoQuery.md)| The MetricInfoQuery to use to filter results | 

### Return type

[**MetricInfoListResult**](MetricInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_metric_simple_query**
> MetricInfoListResult data_metric_simple_query(scope_id, client_id=client_id, channel=channel, name=name, offset=offset, limit=limit)

Gets the MetricInfo list in the scope

Returns the list of all the metricInfos associated to the current selected scope.

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
api_instance = swagger_client.DataMetricsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
client_id = 'client_id_example' # str | The client id to filter results (optional)
channel = 'channel_example' # str | The channel to filter results. It allows '#' wildcard in last channel level (optional)
name = 'name_example' # str | The metric name to filter results (optional)
offset = 0 # int | The result set offset (optional) (default to 0)
limit = 50 # int | The result set limit (optional) (default to 50)

try:
    # Gets the MetricInfo list in the scope
    api_response = api_instance.data_metric_simple_query(scope_id, client_id=client_id, channel=channel, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMetricsApi->data_metric_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **client_id** | **str**| The client id to filter results | [optional] 
 **channel** | **str**| The channel to filter results. It allows &#39;#&#39; wildcard in last channel level | [optional] 
 **name** | **str**| The metric name to filter results | [optional] 
 **offset** | **int**| The result set offset | [optional] [default to 0]
 **limit** | **int**| The result set limit | [optional] [default to 50]

### Return type

[**MetricInfoListResult**](MetricInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

