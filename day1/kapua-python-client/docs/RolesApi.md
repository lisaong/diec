# swagger_client.RolesApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**role_count**](RolesApi.md#role_count) | **POST** /{scopeId}/roles/_count | Counts the Roles
[**role_create**](RolesApi.md#role_create) | **POST** /{scopeId}/roles | Create a Role
[**role_delete**](RolesApi.md#role_delete) | **DELETE** /{scopeId}/roles/{roleId} | Delete a Role
[**role_find**](RolesApi.md#role_find) | **GET** /{scopeId}/roles/{roleId} | Get a Role
[**role_permission_count**](RolesApi.md#role_permission_count) | **POST** /{scopeId}/roles/{roleId}/permissions/_count | Counts the RolePermissions
[**role_permission_create**](RolesApi.md#role_permission_create) | **POST** /{scopeId}/roles/{roleId}/permissions | Create a RolePermission
[**role_permission_delete**](RolesApi.md#role_permission_delete) | **DELETE** /{scopeId}/roles/{roleId}/permissions/{rolePermissionId} | Delete an RolePermission
[**role_permission_find**](RolesApi.md#role_permission_find) | **GET** /{scopeId}/roles/{roleId}/permissions/{rolePermissionId} | Get a RolePermission
[**role_permission_query**](RolesApi.md#role_permission_query) | **POST** /{scopeId}/roles/{roleId}/permissions/_query | Queries the RolePermissions
[**role_permission_simple_query**](RolesApi.md#role_permission_simple_query) | **GET** /{scopeId}/roles/{roleId}/permissions | Gets the RolePermission list in the scope
[**role_query**](RolesApi.md#role_query) | **POST** /{scopeId}/roles/_query | Queries the Roles
[**role_simple_query**](RolesApi.md#role_simple_query) | **GET** /{scopeId}/roles | Gets the Role list in the scope
[**role_update**](RolesApi.md#role_update) | **PUT** /{scopeId}/roles/{roleId} | Update an Role


# **role_count**
> CountResult role_count(scope_id, body)

Counts the Roles

Counts the Roles with the given RoleQuery parameter returning the number of matching Roles

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.RoleQuery() # RoleQuery | The RoleQuery to use to filter count results

try:
    # Counts the Roles
    api_response = api_instance.role_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**RoleQuery**](RoleQuery.md)| The RoleQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_create**
> Role role_create(scope_id, body)

Create a Role

Creates a new Role based on the information provided in RoleCreator parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the Account
body = swagger_client.RoleCreator() # RoleCreator | Provides the information for the new Role to be created

try:
    # Create a Role
    api_response = api_instance.role_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the Account | 
 **body** | [**RoleCreator**](RoleCreator.md)| Provides the information for the new Role to be created | 

### Return type

[**Role**](Role.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_delete**
> role_delete(scope_id, role_id)

Delete a Role

Deletes the Role specified by the \"roleId\" path parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Account to delete.
role_id = 'role_id_example' # str | The id of the Role to be deleted

try:
    # Delete a Role
    api_instance.role_delete(scope_id, role_id)
except ApiException as e:
    print("Exception when calling RolesApi->role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Account to delete. | 
 **role_id** | **str**| The id of the Role to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_find**
> Role role_find(scope_id, role_id)

Get a Role

Returns the Role specified by the \"roleId\" path parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Account.
role_id = 'role_id_example' # str | The id of the requested Role

try:
    # Get a Role
    api_response = api_instance.role_find(scope_id, role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Account. | 
 **role_id** | **str**| The id of the requested Role | 

### Return type

[**Role**](Role.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_permission_count**
> CountResult role_permission_count(scope_id, role_id, body)

Counts the RolePermissions

Counts the RolePermissions with the given RolePermissionQuery parameter returning the number of matching RolePermissions

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results.
role_id = 'role_id_example' # str | The Role id in which to count results.
body = swagger_client.RolePermissionQuery() # RolePermissionQuery | The RolePermissionQuery to use to filter results.

try:
    # Counts the RolePermissions
    api_response = api_instance.role_permission_count(scope_id, role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_permission_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results. | 
 **role_id** | **str**| The Role id in which to count results. | 
 **body** | [**RolePermissionQuery**](RolePermissionQuery.md)| The RolePermissionQuery to use to filter results. | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_permission_create**
> RolePermission role_permission_create(scope_id, role_id, body)

Create a RolePermission

Creates a new RolePermission based on the information provided in RolePermissionCreator parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the RolePermission
role_id = 'role_id_example' # str | The Role id in which to create the RolePermission.
body = swagger_client.RolePermissionCreator() # RolePermissionCreator | Provides the information for the new RolePermission to be created

try:
    # Create a RolePermission
    api_response = api_instance.role_permission_create(scope_id, role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_permission_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the RolePermission | 
 **role_id** | **str**| The Role id in which to create the RolePermission. | 
 **body** | [**RolePermissionCreator**](RolePermissionCreator.md)| Provides the information for the new RolePermission to be created | 

### Return type

[**RolePermission**](RolePermission.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_permission_delete**
> role_permission_delete(scope_id, role_id, role_permission_id)

Delete an RolePermission

Deletes the RolePermission specified by the \"rolePermissionId\" path parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the RolePermission to delete.
role_id = 'role_id_example' # str | Specifies the Role Id for the requested RolePermission
role_permission_id = 'role_permission_id_example' # str | The id of the RolePermission to be deleted

try:
    # Delete an RolePermission
    api_instance.role_permission_delete(scope_id, role_id, role_permission_id)
except ApiException as e:
    print("Exception when calling RolesApi->role_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the RolePermission to delete. | 
 **role_id** | **str**| Specifies the Role Id for the requested RolePermission | 
 **role_permission_id** | **str**| The id of the RolePermission to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_permission_find**
> RolePermission role_permission_find(scope_id, role_id, role_permission_id)

Get a RolePermission

Returns the RolePermission specified by the \"rolePermissionId\" path parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested RolePermission.
role_id = 'role_id_example' # str | Specifies the RoleId for the requested RolePermission
role_permission_id = 'role_permission_id_example' # str | The id of the requested RolePermission

try:
    # Get a RolePermission
    api_response = api_instance.role_permission_find(scope_id, role_id, role_permission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_permission_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested RolePermission. | 
 **role_id** | **str**| Specifies the RoleId for the requested RolePermission | 
 **role_permission_id** | **str**| The id of the requested RolePermission | 

### Return type

[**RolePermission**](RolePermission.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_permission_query**
> RolePermissionListResult role_permission_query(scope_id, role_id, body)

Queries the RolePermissions

Queries the RolePermissions with the given RolePermissionQuery parameter returning all matching RolePermissions

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
role_id = 'role_id_example' # str | The Role id in which to search results.
body = swagger_client.RolePermissionQuery() # RolePermissionQuery | The RolePermissionQuery to use to filter results.

try:
    # Queries the RolePermissions
    api_response = api_instance.role_permission_query(scope_id, role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_permission_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **role_id** | **str**| The Role id in which to search results. | 
 **body** | [**RolePermissionQuery**](RolePermissionQuery.md)| The RolePermissionQuery to use to filter results. | 

### Return type

[**RolePermissionListResult**](RolePermissionListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_permission_simple_query**
> RolePermissionListResult role_permission_simple_query(scope_id, role_id, name=name, action=action, offset=offset, limit=limit)

Gets the RolePermission list in the scope

Returns the list of all the rolePermissions associated to the current selected scope.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
role_id = 'role_id_example' # str | The id of the Role to filter results.
name = 'name_example' # str | The domain name to filter results. (optional)
action = 'action_example' # str | The action to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the RolePermission list in the scope
    api_response = api_instance.role_permission_simple_query(scope_id, role_id, name=name, action=action, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_permission_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **role_id** | **str**| The id of the Role to filter results. | 
 **name** | **str**| The domain name to filter results. | [optional] 
 **action** | **str**| The action to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**RolePermissionListResult**](RolePermissionListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_query**
> RoleListResult role_query(scope_id, body)

Queries the Roles

Queries the Roles with the given RoleQuery parameter returning all matching Roles

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.RoleQuery() # RoleQuery | The RoleQuery to use to filter results.

try:
    # Queries the Roles
    api_response = api_instance.role_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**RoleQuery**](RoleQuery.md)| The RoleQuery to use to filter results. | 

### Return type

[**RoleListResult**](RoleListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_simple_query**
> RoleListResult role_simple_query(scope_id, name=name, offset=offset, limit=limit)

Gets the Role list in the scope

Returns the list of all the roles associated to the current selected scope.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
name = 'name_example' # str | The role name to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the Role list in the scope
    api_response = api_instance.role_simple_query(scope_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **name** | **str**| The role name to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**RoleListResult**](RoleListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_update**
> Role role_update(scope_id, role_id, body)

Update an Role

Updates a new Role based on the information provided in the Role parameter.

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
api_instance = swagger_client.RolesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Account.
role_id = 'role_id_example' # str | The id of the requested Role
body = swagger_client.Role() # Role | The modified Role whose attributed need to be updated

try:
    # Update an Role
    api_response = api_instance.role_update(scope_id, role_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->role_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Account. | 
 **role_id** | **str**| The id of the requested Role | 
 **body** | [**Role**](Role.md)| The modified Role whose attributed need to be updated | 

### Return type

[**Role**](Role.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

