# swagger_client.DataMessagesApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_message_count**](DataMessagesApi.md#data_message_count) | **POST** /{scopeId}/data/messages/_count | Counts the DatastoreMessages
[**data_message_find**](DataMessagesApi.md#data_message_find) | **GET** /{scopeId}/data/messages/{datastoreMessageId} | Gets an DatastoreMessage
[**data_message_query**](DataMessagesApi.md#data_message_query) | **POST** /{scopeId}/data/messages/_query | Queries the DatastoreMessages
[**data_message_simple_query**](DataMessagesApi.md#data_message_simple_query) | **GET** /{scopeId}/data/messages | Gets the DatastoreMessage list in the scope
[**data_message_store**](DataMessagesApi.md#data_message_store) | **POST** /{scopeId}/data/messages | Stores a new KapuaDataMessage


# **data_message_count**
> CountResult data_message_count(scope_id, body)

Counts the DatastoreMessages

Counts the DatastoreMessages with the given DatastoreMessageQuery parameter returning the number of matching DatastoreMessages

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
api_instance = swagger_client.DataMessagesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.MessageQuery() # MessageQuery | The DatastoreMessageQuery to use to filter count results

try:
    # Counts the DatastoreMessages
    api_response = api_instance.data_message_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMessagesApi->data_message_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**MessageQuery**](MessageQuery.md)| The DatastoreMessageQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_message_find**
> DatastoreMessage data_message_find(scope_id, datastore_message_id)

Gets an DatastoreMessage

Gets the DatastoreMessage specified by the datastoreMessageId path parameter

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
api_instance = swagger_client.DataMessagesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested DatastoreMessage.
datastore_message_id = 'datastore_message_id_example' # str | The id of the requested DatastoreMessage

try:
    # Gets an DatastoreMessage
    api_response = api_instance.data_message_find(scope_id, datastore_message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMessagesApi->data_message_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested DatastoreMessage. | 
 **datastore_message_id** | **str**| The id of the requested DatastoreMessage | 

### Return type

[**DatastoreMessage**](DatastoreMessage.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_message_query**
> MessageListResult data_message_query(scope_id, body)

Queries the DatastoreMessages

Queries the DatastoreMessages with the given DatastoreMessageQuery parameter returning all matching DatastoreMessages

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
api_instance = swagger_client.DataMessagesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.JsonMessageQuery() # JsonMessageQuery | The DatastoreMessageQuery to use to filter results

try:
    # Queries the DatastoreMessages
    api_response = api_instance.data_message_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMessagesApi->data_message_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**JsonMessageQuery**](JsonMessageQuery.md)| The DatastoreMessageQuery to use to filter results | 

### Return type

[**MessageListResult**](MessageListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_message_simple_query**
> MessageListResult data_message_simple_query(scope_id, client_id=client_id, channel=channel, strict_channel=strict_channel, start_date=start_date, end_date=end_date, metric_name=metric_name, metric_type=metric_type, metric_min=metric_min, metric_max=metric_max, offset=offset, limit=limit)

Gets the DatastoreMessage list in the scope

Returns the list of all the datastoreMessages associated to the current selected scope.

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
api_instance = swagger_client.DataMessagesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
client_id = 'client_id_example' # str | The client id to filter results (optional)
channel = 'channel_example' # str | The channel to filter results. (optional)
strict_channel = true # bool | Restrict the search only to this channel ignoring its children. Only meaningful if channel is set. (optional)
start_date = 'start_date_example' # str | The start date to filter the results. Must come before endDate parameter (optional)
end_date = 'end_date_example' # str | The end date to filter the results. Must come after startDate parameter (optional)
metric_name = 'metric_name_example' # str | The metric name to filter results (optional)
metric_type = 'metric_type_example' # str | The metric type to filter results (optional)
metric_min = 'metric_min_example' # str | The min metric value to filter results (optional)
metric_max = 'metric_max_example' # str | The max metric value to filter results (optional)
offset = 0 # int | The result set offset (optional) (default to 0)
limit = 50 # int | The result set limit (optional) (default to 50)

try:
    # Gets the DatastoreMessage list in the scope
    api_response = api_instance.data_message_simple_query(scope_id, client_id=client_id, channel=channel, strict_channel=strict_channel, start_date=start_date, end_date=end_date, metric_name=metric_name, metric_type=metric_type, metric_min=metric_min, metric_max=metric_max, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMessagesApi->data_message_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **client_id** | **str**| The client id to filter results | [optional] 
 **channel** | **str**| The channel to filter results. | [optional] 
 **strict_channel** | **bool**| Restrict the search only to this channel ignoring its children. Only meaningful if channel is set. | [optional] 
 **start_date** | **str**| The start date to filter the results. Must come before endDate parameter | [optional] 
 **end_date** | **str**| The end date to filter the results. Must come after startDate parameter | [optional] 
 **metric_name** | **str**| The metric name to filter results | [optional] 
 **metric_type** | **str**| The metric type to filter results | [optional] 
 **metric_min** | **str**| The min metric value to filter results | [optional] 
 **metric_max** | **str**| The max metric value to filter results | [optional] 
 **offset** | **int**| The result set offset | [optional] [default to 0]
 **limit** | **int**| The result set limit | [optional] [default to 50]

### Return type

[**MessageListResult**](MessageListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_message_store**
> StorableId data_message_store(scope_id, body=body)

Stores a new KapuaDataMessage

Stores a new KapuaDataMessage under the account of the currently connected user. In this case, the provided message will only be stored in the back-end database and it will not be forwarded to the message broker.

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
api_instance = swagger_client.DataMessagesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to store the message
body = swagger_client.JsonKapuaDataMessage() # JsonKapuaDataMessage | The KapuaDataMessage to be stored (optional)

try:
    # Stores a new KapuaDataMessage
    api_response = api_instance.data_message_store(scope_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataMessagesApi->data_message_store: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to store the message | 
 **body** | [**JsonKapuaDataMessage**](JsonKapuaDataMessage.md)| The KapuaDataMessage to be stored | [optional] 

### Return type

[**StorableId**](StorableId.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

