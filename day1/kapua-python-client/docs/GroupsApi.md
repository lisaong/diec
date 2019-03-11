# swagger_client.GroupsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**group_count**](GroupsApi.md#group_count) | **POST** /{scopeId}/groups/_count | Counts the Groups
[**group_create**](GroupsApi.md#group_create) | **POST** /{scopeId}/groups | Create a Group
[**group_delete**](GroupsApi.md#group_delete) | **DELETE** /{scopeId}/groups/{groupId} | Delete an Group
[**group_find**](GroupsApi.md#group_find) | **GET** /{scopeId}/groups/{groupId} | Get an Group
[**group_query**](GroupsApi.md#group_query) | **POST** /{scopeId}/groups/_query | Queries the Groups
[**group_simple_query**](GroupsApi.md#group_simple_query) | **GET** /{scopeId}/groups | Gets the Group list in the scope
[**group_update**](GroupsApi.md#group_update) | **PUT** /{scopeId}/groups/{groupId} | Update an Group


# **group_count**
> CountResult group_count(scope_id, body)

Counts the Groups

Counts the Groups with the given GroupQuery parameter returning the number of matching Groups

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.GroupQuery() # GroupQuery | The GroupQuery to use to filter count results

try:
    # Counts the Groups
    api_response = api_instance.group_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**GroupQuery**](GroupQuery.md)| The GroupQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_create**
> Group group_create(scope_id, body)

Create a Group

Creates a new Group based on the information provided in GroupCreator parameter.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the Group
body = swagger_client.GroupCreator() # GroupCreator | Provides the information for the new Group to be created

try:
    # Create a Group
    api_response = api_instance.group_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the Group | 
 **body** | [**GroupCreator**](GroupCreator.md)| Provides the information for the new Group to be created | 

### Return type

[**Group**](Group.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_delete**
> group_delete(scope_id, group_id)

Delete an Group

Deletes the Group specified by the \"groupId\" path parameter.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Group to delete.
group_id = 'group_id_example' # str | The id of the Group to be deleted

try:
    # Delete an Group
    api_instance.group_delete(scope_id, group_id)
except ApiException as e:
    print("Exception when calling GroupsApi->group_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Group to delete. | 
 **group_id** | **str**| The id of the Group to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_find**
> Group group_find(scope_id, group_id)

Get an Group

Returns the Group specified by the \"groupId\" path parameter.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Group.
group_id = 'group_id_example' # str | The id of the requested Group

try:
    # Get an Group
    api_response = api_instance.group_find(scope_id, group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Group. | 
 **group_id** | **str**| The id of the requested Group | 

### Return type

[**Group**](Group.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_query**
> GroupListResult group_query(scope_id, body)

Queries the Groups

Queries the Groups with the given GroupQuery parameter returning all matching Groups

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.GroupQuery() # GroupQuery | The GroupQuery to use to filter results.

try:
    # Queries the Groups
    api_response = api_instance.group_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**GroupQuery**](GroupQuery.md)| The GroupQuery to use to filter results. | 

### Return type

[**GroupListResult**](GroupListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_simple_query**
> GroupListResult group_simple_query(scope_id, name=name, offset=offset, limit=limit)

Gets the Group list in the scope

Returns the list of all the groups associated to the current selected scope.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
name = 'name_example' # str | The group name to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the Group list in the scope
    api_response = api_instance.group_simple_query(scope_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **name** | **str**| The group name to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**GroupListResult**](GroupListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_update**
> Group group_update(scope_id, group_id, body)

Update an Group

Updates a new Group based on the information provided in the Group parameter.

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
api_instance = swagger_client.GroupsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Group.
group_id = 'group_id_example' # str | The id of the requested Group
body = swagger_client.Group() # Group | The modified Group whose attributed need to be updated

try:
    # Update an Group
    api_response = api_instance.group_update(scope_id, group_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->group_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Group. | 
 **group_id** | **str**| The id of the requested Group | 
 **body** | [**Group**](Group.md)| The modified Group whose attributed need to be updated | 

### Return type

[**Group**](Group.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

