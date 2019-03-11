# swagger_client.TagsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag**](TagsApi.md#create_tag) | **POST** /{scopeId}/tags | Create a Tag
[**tag_count**](TagsApi.md#tag_count) | **POST** /{scopeId}/tags/_count | Counts the Tags
[**tag_delete**](TagsApi.md#tag_delete) | **DELETE** /{scopeId}/tags/{tagId} | Delete an Tag
[**tag_find**](TagsApi.md#tag_find) | **GET** /{scopeId}/tags/{tagId} | Get a Tag
[**tag_query**](TagsApi.md#tag_query) | **POST** /{scopeId}/tags/_query | Queries the Tags
[**tag_simple_query**](TagsApi.md#tag_simple_query) | **GET** /{scopeId}/tags | Gets the Tag list in the scope
[**tag_update**](TagsApi.md#tag_update) | **PUT** /{scopeId}/tags/{tagId} | Update a Tag


# **create_tag**
> Tag create_tag(scope_id, body)

Create a Tag

Creates a new Tag based on the information provided in TagCreator parameter.

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the Tag
body = swagger_client.TagCreator() # TagCreator | Provides the information for the new Tag to be created

try:
    # Create a Tag
    api_response = api_instance.create_tag(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->create_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the Tag | 
 **body** | [**TagCreator**](TagCreator.md)| Provides the information for the new Tag to be created | 

### Return type

[**Tag**](Tag.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_count**
> CountResult tag_count(scope_id, body)

Counts the Tags

Counts the Tags with the given TagQuery parameter returning the number of matching Tags

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.TagQuery() # TagQuery | The TagQuery to use to filter count results

try:
    # Counts the Tags
    api_response = api_instance.tag_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tag_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**TagQuery**](TagQuery.md)| The TagQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_delete**
> tag_delete(scope_id, tag_id)

Delete an Tag

Deletes the Tag specified by the \"tagId\" path parameter.

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Tag to delete.
tag_id = 'tag_id_example' # str | The id of the Tag to be deleted

try:
    # Delete an Tag
    api_instance.tag_delete(scope_id, tag_id)
except ApiException as e:
    print("Exception when calling TagsApi->tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Tag to delete. | 
 **tag_id** | **str**| The id of the Tag to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_find**
> Tag tag_find(scope_id, tag_id)

Get a Tag

Returns the Tag specified by the \"tagId\" path parameter.

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Tag.
tag_id = 'tag_id_example' # str | The id of the requested Tag

try:
    # Get a Tag
    api_response = api_instance.tag_find(scope_id, tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tag_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Tag. | 
 **tag_id** | **str**| The id of the requested Tag | 

### Return type

[**Tag**](Tag.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_query**
> TagListResult tag_query(scope_id, body)

Queries the Tags

Queries the Tags with the given TagQuery parameter returning all matching Tags

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.TagQuery() # TagQuery | The TagQuery to use to filter results.

try:
    # Queries the Tags
    api_response = api_instance.tag_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tag_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**TagQuery**](TagQuery.md)| The TagQuery to use to filter results. | 

### Return type

[**TagListResult**](TagListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_simple_query**
> TagListResult tag_simple_query(scope_id, name=name, offset=offset, limit=limit)

Gets the Tag list in the scope

Returns the list of all the tags associated to the current selected scope.

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
name = 'name_example' # str | The tag name to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the Tag list in the scope
    api_response = api_instance.tag_simple_query(scope_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tag_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **name** | **str**| The tag name to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**TagListResult**](TagListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_update**
> Tag tag_update(scope_id, tag_id, body)

Update a Tag

Updates a new Tag based on the information provided in the Tag parameter.

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
api_instance = swagger_client.TagsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Tag.
tag_id = 'tag_id_example' # str | The id of the requested Tag
body = swagger_client.Tag() # Tag | The modified Tag whose attributed need to be updated

try:
    # Update a Tag
    api_response = api_instance.tag_update(scope_id, tag_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagsApi->tag_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Tag. | 
 **tag_id** | **str**| The id of the requested Tag | 
 **body** | [**Tag**](Tag.md)| The modified Tag whose attributed need to be updated | 

### Return type

[**Tag**](Tag.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

