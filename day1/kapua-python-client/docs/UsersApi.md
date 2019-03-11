# swagger_client.UsersApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_count**](UsersApi.md#user_count) | **POST** /{scopeId}/users/_count | Counts the Users
[**user_create**](UsersApi.md#user_create) | **POST** /{scopeId}/users | Create an User
[**user_delete**](UsersApi.md#user_delete) | **DELETE** /{scopeId}/users/{userId} | Delete an User
[**user_find**](UsersApi.md#user_find) | **GET** /{scopeId}/users/{userId} | Get an User
[**user_query**](UsersApi.md#user_query) | **POST** /{scopeId}/users/_query | Queries the Users
[**user_simple_query**](UsersApi.md#user_simple_query) | **GET** /{scopeId}/users | Gets the User list in the scope
[**user_update**](UsersApi.md#user_update) | **PUT** /{scopeId}/users/{userId} | Update an User


# **user_count**
> CountResult user_count(scope_id, body)

Counts the Users

Counts the Users with the given UserQuery parameter returning the number of matching Users

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.UserQuery() # UserQuery | The UserQuery to use to filter count results

try:
    # Counts the Users
    api_response = api_instance.user_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**UserQuery**](UserQuery.md)| The UserQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> User user_create(scope_id, body)

Create an User

Creates a new User based on the information provided in UserCreator parameter.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the User
body = swagger_client.UserCreator() # UserCreator | Provides the information for the new User to be created

try:
    # Create an User
    api_response = api_instance.user_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the User | 
 **body** | [**UserCreator**](UserCreator.md)| Provides the information for the new User to be created | 

### Return type

[**User**](User.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_delete**
> user_delete(scope_id, user_id)

Delete an User

Deletes the User specified by the \"userId\" path parameter.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the User to delete.
user_id = 'user_id_example' # str | The id of the User to be deleted

try:
    # Delete an User
    api_instance.user_delete(scope_id, user_id)
except ApiException as e:
    print("Exception when calling UsersApi->user_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the User to delete. | 
 **user_id** | **str**| The id of the User to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_find**
> User user_find(scope_id, user_id)

Get an User

Returns the User specified by the \"userId\" path parameter.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested User.
user_id = 'user_id_example' # str | The id of the requested User

try:
    # Get an User
    api_response = api_instance.user_find(scope_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested User. | 
 **user_id** | **str**| The id of the requested User | 

### Return type

[**User**](User.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_query**
> UserListResult user_query(scope_id, body)

Queries the Users

Queries the Users with the given UserQuery parameter returning all matching Users

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.UserQuery() # UserQuery | The UserQuery to use to filter results.

try:
    # Queries the Users
    api_response = api_instance.user_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**UserQuery**](UserQuery.md)| The UserQuery to use to filter results. | 

### Return type

[**UserListResult**](UserListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_simple_query**
> UserListResult user_simple_query(scope_id, name=name, offset=offset, limit=limit)

Gets the User list in the scope

Returns the list of all the users associated to the current selected scope.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
name = 'name_example' # str | The user name to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the User list in the scope
    api_response = api_instance.user_simple_query(scope_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **name** | **str**| The user name to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**UserListResult**](UserListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update**
> User user_update(scope_id, user_id, body)

Update an User

Updates a new User based on the information provided in the User parameter.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested User.
user_id = 'user_id_example' # str | The id of the requested User
body = swagger_client.User() # User | The modified User whose attributes needs to be updated

try:
    # Update an User
    api_response = api_instance.user_update(scope_id, user_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->user_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested User. | 
 **user_id** | **str**| The id of the requested User | 
 **body** | [**User**](User.md)| The modified User whose attributes needs to be updated | 

### Return type

[**User**](User.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

