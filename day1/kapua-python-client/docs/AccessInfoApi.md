# swagger_client.AccessInfoApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**access_info_count**](AccessInfoApi.md#access_info_count) | **POST** /{scopeId}/accessinfos/_count | Counts the AccessInfos
[**access_info_create**](AccessInfoApi.md#access_info_create) | **POST** /{scopeId}/accessinfos | Creates a new AccessInfo
[**access_info_delete**](AccessInfoApi.md#access_info_delete) | **DELETE** /{scopeId}/accessinfos/{accessInfoId} | Deletes an AccessInfo
[**access_info_find**](AccessInfoApi.md#access_info_find) | **GET** /{scopeId}/accessinfos/{accessInfoId} | Gets an AccessInfo
[**access_info_query**](AccessInfoApi.md#access_info_query) | **POST** /{scopeId}/accessinfos/_query | Queries the AccessInfos
[**access_info_simple_query**](AccessInfoApi.md#access_info_simple_query) | **GET** /{scopeId}/accessinfos | Gets the AccessInfo list in the scope.
[**access_permission_count**](AccessInfoApi.md#access_permission_count) | **POST** /{scopeId}/accessinfos/{accessInfoId}/permissions/_count | Counts the AccessPermissions
[**access_permission_create**](AccessInfoApi.md#access_permission_create) | **POST** /{scopeId}/accessinfos/{accessInfoId}/permissions | Create an AccessPermission
[**access_permission_delete**](AccessInfoApi.md#access_permission_delete) | **DELETE** /{scopeId}/accessinfos/{accessInfoId}/permissions/{accessPermissionId} | Delete an AccessPermission
[**access_permission_find**](AccessInfoApi.md#access_permission_find) | **GET** /{scopeId}/accessinfos/{accessInfoId}/permissions/{accessPermissionId} | Get an AccessPermission
[**access_permission_query**](AccessInfoApi.md#access_permission_query) | **POST** /{scopeId}/accessinfos/{accessInfoId}/permissions/_query | Queries the AccessPermissions
[**access_permission_simple_query**](AccessInfoApi.md#access_permission_simple_query) | **GET** /{scopeId}/accessinfos/{accessInfoId}/permissions | Gets the AccessPermission list in the scope
[**access_role_count**](AccessInfoApi.md#access_role_count) | **POST** /{scopeId}/accessinfos/{accessInfoId}/roles/_count | Counts the AccessRoles
[**access_role_create**](AccessInfoApi.md#access_role_create) | **POST** /{scopeId}/accessinfos/{accessInfoId}/roles | Create an AccessRole
[**access_role_delete**](AccessInfoApi.md#access_role_delete) | **DELETE** /{scopeId}/accessinfos/{accessInfoId}/roles/{accessRoleId} | Delete an AccessRole
[**access_role_find**](AccessInfoApi.md#access_role_find) | **GET** /{scopeId}/accessinfos/{accessInfoId}/roles/{accessRoleId} | Get an AccessRole
[**access_role_query**](AccessInfoApi.md#access_role_query) | **POST** /{scopeId}/accessinfos/{accessInfoId}/roles/_query | Queries the AccessRoles
[**access_role_simple_query**](AccessInfoApi.md#access_role_simple_query) | **GET** /{scopeId}/accessinfos/{accessInfoId}/roles | Gets the AccessRole list in the scope


# **access_info_count**
> CountResult access_info_count(scope_id, body)

Counts the AccessInfos

Counts the AccessInfos with the given AccessInfoQuery parameter returning the number of matching AccessInfos

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.AccessInfoQuery() # AccessInfoQuery | The AccessInfoQuery to use to filter count results

try:
    # Counts the AccessInfos
    api_response = api_instance.access_info_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**AccessInfoQuery**](AccessInfoQuery.md)| The AccessInfoQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_info_create**
> AccessInfo access_info_create(scope_id, body)

Creates a new AccessInfo

Creates a new AccessInfo based on the information provided in AccessInfoCreator parameter

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the AccessInfo
body = swagger_client.AccessInfoCreator() # AccessInfoCreator | Provides the information for the new AccessInfo to be created

try:
    # Creates a new AccessInfo
    api_response = api_instance.access_info_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the AccessInfo | 
 **body** | [**AccessInfoCreator**](AccessInfoCreator.md)| Provides the information for the new AccessInfo to be created | 

### Return type

[**AccessInfo**](AccessInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_info_delete**
> access_info_delete(scope_id, access_info_id)

Deletes an AccessInfo

Deletes the AccessInfo specified by the accessInfoId path parameter

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the AccessInfo
access_info_id = 'access_info_id_example' # str | The id of the AccessInfo to delete

try:
    # Deletes an AccessInfo
    api_instance.access_info_delete(scope_id, access_info_id)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the AccessInfo | 
 **access_info_id** | **str**| The id of the AccessInfo to delete | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_info_find**
> AccessInfo access_info_find(scope_id, access_info_id)

Gets an AccessInfo

Gets the AccessInfo specified by the accessInfoId path parameter

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested AccessInfo.
access_info_id = 'access_info_id_example' # str | The id of the requested AccessInfo

try:
    # Gets an AccessInfo
    api_response = api_instance.access_info_find(scope_id, access_info_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested AccessInfo. | 
 **access_info_id** | **str**| The id of the requested AccessInfo | 

### Return type

[**AccessInfo**](AccessInfo.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_info_query**
> AccessInfoListResult access_info_query(scope_id, body)

Queries the AccessInfos

Queries the AccessInfos with the given AccessInfoQuery parameter returning all matching AccessInfos

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
body = swagger_client.AccessInfoQuery() # AccessInfoQuery | The AccessInfoQuery to use to filter results

try:
    # Queries the AccessInfos
    api_response = api_instance.access_info_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **body** | [**AccessInfoQuery**](AccessInfoQuery.md)| The AccessInfoQuery to use to filter results | 

### Return type

[**AccessInfoListResult**](AccessInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_info_simple_query**
> AccessInfoListResult access_info_simple_query(scope_id, user_id=user_id, offset=offset, limit=limit)

Gets the AccessInfo list in the scope.

Gets the AccessInfo list in the scope. The query parameter userId is optional and can be used to filter results

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results
user_id = 'user_id_example' # str | The optional User id to filter results (optional)
offset = 0 # int | The result set offset (optional) (default to 0)
limit = 50 # int | The result set limit (optional) (default to 50)

try:
    # Gets the AccessInfo list in the scope.
    api_response = api_instance.access_info_simple_query(scope_id, user_id=user_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_info_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results | 
 **user_id** | **str**| The optional User id to filter results | [optional] 
 **offset** | **int**| The result set offset | [optional] [default to 0]
 **limit** | **int**| The result set limit | [optional] [default to 50]

### Return type

[**AccessInfoListResult**](AccessInfoListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_permission_count**
> CountResult access_permission_count(scope_id, access_info_id, body)

Counts the AccessPermissions

Counts the AccessPermissions with the given AccessPermissionQuery parameter returning the number of matching AccessPermissions

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
access_info_id = 'access_info_id_example' # str | The AccessInfo id in which to count results.
body = swagger_client.AccessPermissionQuery() # AccessPermissionQuery | The AccessPermissionQuery to use to filter count results

try:
    # Counts the AccessPermissions
    api_response = api_instance.access_permission_count(scope_id, access_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_permission_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **access_info_id** | **str**| The AccessInfo id in which to count results. | 
 **body** | [**AccessPermissionQuery**](AccessPermissionQuery.md)| The AccessPermissionQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_permission_create**
> AccessPermission access_permission_create(scope_id, access_info_id, body)

Create an AccessPermission

Creates a new AccessPermission based on the information provided in AccessPermissionCreator parameter.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the AccessPermission
access_info_id = 'access_info_id_example' # str | The AccessInfo id in which to create the AccessPermission.
body = swagger_client.AccessPermissionCreator() # AccessPermissionCreator | Provides the information for the new AccessPermission to be created

try:
    # Create an AccessPermission
    api_response = api_instance.access_permission_create(scope_id, access_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_permission_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the AccessPermission | 
 **access_info_id** | **str**| The AccessInfo id in which to create the AccessPermission. | 
 **body** | [**AccessPermissionCreator**](AccessPermissionCreator.md)| Provides the information for the new AccessPermission to be created | 

### Return type

[**AccessPermission**](AccessPermission.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_permission_delete**
> access_permission_delete(scope_id, access_info_id, access_permission_id)

Delete an AccessPermission

Deletes the AccessPermission specified by the \"accessPermissionId\" path parameter.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the AccessPermission to delete.
access_info_id = 'access_info_id_example' # str | Specifies the AccessInfo Id for the requested AccessPermission
access_permission_id = 'access_permission_id_example' # str | The id of the AccessPermission to be deleted

try:
    # Delete an AccessPermission
    api_instance.access_permission_delete(scope_id, access_info_id, access_permission_id)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_permission_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the AccessPermission to delete. | 
 **access_info_id** | **str**| Specifies the AccessInfo Id for the requested AccessPermission | 
 **access_permission_id** | **str**| The id of the AccessPermission to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_permission_find**
> AccessPermission access_permission_find(scope_id, access_info_id, access_permission_id)

Get an AccessPermission

Returns the AccessPermission specified by the \"accessPermissionId\" path parameter.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested AccessPermission.
access_info_id = 'access_info_id_example' # str | Specifies the AccessPermissionId for the requested AccessPermission
access_permission_id = 'access_permission_id_example' # str | The id of the requested AccessPermission

try:
    # Get an AccessPermission
    api_response = api_instance.access_permission_find(scope_id, access_info_id, access_permission_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_permission_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested AccessPermission. | 
 **access_info_id** | **str**| Specifies the AccessPermissionId for the requested AccessPermission | 
 **access_permission_id** | **str**| The id of the requested AccessPermission | 

### Return type

[**AccessPermission**](AccessPermission.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_permission_query**
> AccessPermissionListResult access_permission_query(scope_id, access_info_id, body)

Queries the AccessPermissions

Queries the AccessPermissions with the given AccessPermissionQuery parameter returning all matching AccessPermissions

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
access_info_id = 'access_info_id_example' # str | The AccessInfo id in which to search results.
body = swagger_client.AccessPermissionQuery() # AccessPermissionQuery | The AccessPermissionQuery to use to filter results.

try:
    # Queries the AccessPermissions
    api_response = api_instance.access_permission_query(scope_id, access_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_permission_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **access_info_id** | **str**| The AccessInfo id in which to search results. | 
 **body** | [**AccessPermissionQuery**](AccessPermissionQuery.md)| The AccessPermissionQuery to use to filter results. | 

### Return type

[**AccessPermissionListResult**](AccessPermissionListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_permission_simple_query**
> AccessPermissionListResult access_permission_simple_query(scope_id, access_info_id, offset=offset, limit=limit)

Gets the AccessPermission list in the scope

Gets the AccessPermission list in the scope. The query parameter accessInfoId is optional and can be used to filter results

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
access_info_id = 'access_info_id_example' # str | The optional id to filter results.
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the AccessPermission list in the scope
    api_response = api_instance.access_permission_simple_query(scope_id, access_info_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_permission_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **access_info_id** | **str**| The optional id to filter results. | 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**AccessPermissionListResult**](AccessPermissionListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_role_count**
> CountResult access_role_count(scope_id, access_info_id, body)

Counts the AccessRoles

Counts the AccessRoles with the given AccessRoleQuery parameter returning the number of matching AccessRoles

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
access_info_id = 'access_info_id_example' # str | The AccessInfo id in which to count results.
body = swagger_client.AccessRoleQuery() # AccessRoleQuery | The AccessRoleQuery to use to filter count results

try:
    # Counts the AccessRoles
    api_response = api_instance.access_role_count(scope_id, access_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_role_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **access_info_id** | **str**| The AccessInfo id in which to count results. | 
 **body** | [**AccessRoleQuery**](AccessRoleQuery.md)| The AccessRoleQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_role_create**
> AccessRole access_role_create(scope_id, access_info_id, body)

Create an AccessRole

Creates a new AccessRole based on the information provided in AccessRoleCreator parameter.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the AccessRole
access_info_id = 'access_info_id_example' # str | The AccessInfo id in which to create the AccessRole.
body = swagger_client.AccessRoleCreator() # AccessRoleCreator | Provides the information for the new AccessRole to be created

try:
    # Create an AccessRole
    api_response = api_instance.access_role_create(scope_id, access_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_role_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the AccessRole | 
 **access_info_id** | **str**| The AccessInfo id in which to create the AccessRole. | 
 **body** | [**AccessRoleCreator**](AccessRoleCreator.md)| Provides the information for the new AccessRole to be created | 

### Return type

[**AccessRole**](AccessRole.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_role_delete**
> access_role_delete(scope_id, access_info_id, access_role_id)

Delete an AccessRole

Deletes the AccessRole specified by the \"accessRoleId\" path parameter.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the AccessRole to delete.
access_info_id = 'access_info_id_example' # str | Specifies the AccessInfoId for the requested AccessPermission
access_role_id = 'access_role_id_example' # str | The id of the AccessRole to be deleted

try:
    # Delete an AccessRole
    api_instance.access_role_delete(scope_id, access_info_id, access_role_id)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_role_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the AccessRole to delete. | 
 **access_info_id** | **str**| Specifies the AccessInfoId for the requested AccessPermission | 
 **access_role_id** | **str**| The id of the AccessRole to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_role_find**
> AccessRole access_role_find(scope_id, access_info_id, access_role_id)

Get an AccessRole

Returns the AccessRole specified by the \"accessRoleId\" path parameter.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested AccessRole.
access_info_id = 'access_info_id_example' # str | Specifies the AccessRoleId for the requested AccessRole
access_role_id = 'access_role_id_example' # str | The id of the requested AccessRole

try:
    # Get an AccessRole
    api_response = api_instance.access_role_find(scope_id, access_info_id, access_role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_role_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested AccessRole. | 
 **access_info_id** | **str**| Specifies the AccessRoleId for the requested AccessRole | 
 **access_role_id** | **str**| The id of the requested AccessRole | 

### Return type

[**AccessRole**](AccessRole.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_role_query**
> AccessRoleListResult access_role_query(scope_id, access_info_id, body)

Queries the AccessRoles

Queries the AccessRoles with the given AccessRoleQuery parameter returning all matching AccessRoles

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
access_info_id = 'access_info_id_example' # str | The AccessInfo id in which to search results.
body = swagger_client.AccessRoleQuery() # AccessRoleQuery | The AccessRoleQuery to use to filter results.

try:
    # Queries the AccessRoles
    api_response = api_instance.access_role_query(scope_id, access_info_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_role_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **access_info_id** | **str**| The AccessInfo id in which to search results. | 
 **body** | [**AccessRoleQuery**](AccessRoleQuery.md)| The AccessRoleQuery to use to filter results. | 

### Return type

[**AccessRoleListResult**](AccessRoleListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **access_role_simple_query**
> AccessRoleListResult access_role_simple_query(scope_id, access_info_id, limit, offset=offset)

Gets the AccessRole list in the scope

Returns the list of all the accessRoles associated to the current selected scope.

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
api_instance = swagger_client.AccessInfoApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
access_info_id = 'access_info_id_example' # str | The optional id to filter results.
limit = 50 # int | The result set limit. (default to 50)
offset = 0 # int | The result set offset. (optional) (default to 0)

try:
    # Gets the AccessRole list in the scope
    api_response = api_instance.access_role_simple_query(scope_id, access_info_id, limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessInfoApi->access_role_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **access_info_id** | **str**| The optional id to filter results. | 
 **limit** | **int**| The result set limit. | [default to 50]
 **offset** | **int**| The result set offset. | [optional] [default to 0]

### Return type

[**AccessRoleListResult**](AccessRoleListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

