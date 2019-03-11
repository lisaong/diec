# swagger_client.CredentialsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credential_count**](CredentialsApi.md#credential_count) | **POST** /{scopeId}/credentials/_count | Counts the Credentials
[**credential_create**](CredentialsApi.md#credential_create) | **POST** /{scopeId}/credentials | Create a Credential
[**credential_delete**](CredentialsApi.md#credential_delete) | **DELETE** /{scopeId}/credentials/{credentialId} | Delete a Credential
[**credential_find**](CredentialsApi.md#credential_find) | **GET** /{scopeId}/credentials/{credentialId} | Get a Credential
[**credential_query**](CredentialsApi.md#credential_query) | **POST** /{scopeId}/credentials/_query | Queries the Credentials
[**credential_simple_query**](CredentialsApi.md#credential_simple_query) | **GET** /{scopeId}/credentials | Gets the Credential list in the scope
[**credential_unlock**](CredentialsApi.md#credential_unlock) | **POST** /{scopeId}/credentials/{credentialId}/unlock | Unlock a Credential
[**credential_update**](CredentialsApi.md#credential_update) | **PUT** /{scopeId}/credentials/{credentialId} | Update an Credential


# **credential_count**
> CountResult credential_count(scope_id, body)

Counts the Credentials

Counts the Credentials with the given CredentialQuery parameter returning the number of matching Credentials

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.CredentialQuery() # CredentialQuery | The CredentialQuery to use to filter count results

try:
    # Counts the Credentials
    api_response = api_instance.credential_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**CredentialQuery**](CredentialQuery.md)| The CredentialQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_create**
> Credential credential_create(scope_id, body)

Create a Credential

Creates a new Credential based on the information provided in CredentialCreator parameter.

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the Credential
body = swagger_client.CredentialCreator() # CredentialCreator | Provides the information for the new Credential to be created

try:
    # Create a Credential
    api_response = api_instance.credential_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the Credential | 
 **body** | [**CredentialCreator**](CredentialCreator.md)| Provides the information for the new Credential to be created | 

### Return type

[**Credential**](Credential.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_delete**
> credential_delete(scope_id, credential_id)

Delete a Credential

Deletes the Credential specified by the \"credentialId\" path parameter.

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Credential to delete.
credential_id = 'credential_id_example' # str | The id of the Credential to be deleted

try:
    # Delete a Credential
    api_instance.credential_delete(scope_id, credential_id)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Credential to delete. | 
 **credential_id** | **str**| The id of the Credential to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_find**
> Credential credential_find(scope_id, credential_id)

Get a Credential

Returns the Credential specified by the \"credentialId\" path parameter.

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Credential.
credential_id = 'credential_id_example' # str | The id of the requested Credential

try:
    # Get a Credential
    api_response = api_instance.credential_find(scope_id, credential_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Credential. | 
 **credential_id** | **str**| The id of the requested Credential | 

### Return type

[**Credential**](Credential.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_query**
> CredentialListResult credential_query(scope_id, body)

Queries the Credentials

Queries the Credentials with the given CredentialQuery parameter returning all matching Credentials

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.CredentialQuery() # CredentialQuery | The CredentialQuery to use to filter results.

try:
    # Queries the Credentials
    api_response = api_instance.credential_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**CredentialQuery**](CredentialQuery.md)| The CredentialQuery to use to filter results. | 

### Return type

[**CredentialListResult**](CredentialListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_simple_query**
> CredentialListResult credential_simple_query(scope_id, limit, user_id=user_id, offset=offset)

Gets the Credential list in the scope

Returns the list of all the credentials associated to the current selected scope.

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
limit = 50 # int | The result set limit. (default to 50)
user_id = 'user_id_example' # str | The optional id to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)

try:
    # Gets the Credential list in the scope
    api_response = api_instance.credential_simple_query(scope_id, limit, user_id=user_id, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **limit** | **int**| The result set limit. | [default to 50]
 **user_id** | **str**| The optional id to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]

### Return type

[**CredentialListResult**](CredentialListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_unlock**
> credential_unlock(scope_id, credential_id)

Unlock a Credential

Unlocks a Credential that has been locked due to a lockout policy.

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Credential to delete.
credential_id = 'credential_id_example' # str | The id of the Credential to be unlocked

try:
    # Unlock a Credential
    api_instance.credential_unlock(scope_id, credential_id)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_unlock: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Credential to delete. | 
 **credential_id** | **str**| The id of the Credential to be unlocked | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credential_update**
> Credential credential_update(scope_id, credential_id, body)

Update an Credential

Updates a new Credential based on the information provided in the Credential parameter.

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
api_instance = swagger_client.CredentialsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Credential.
credential_id = 'credential_id_example' # str | The id of the requested Credential
body = swagger_client.Credential() # Credential | The modified Credential whose attributed need to be updated

try:
    # Update an Credential
    api_response = api_instance.credential_update(scope_id, credential_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CredentialsApi->credential_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Credential. | 
 **credential_id** | **str**| The id of the requested Credential | 
 **body** | [**Credential**](Credential.md)| The modified Credential whose attributed need to be updated | 

### Return type

[**Credential**](Credential.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

