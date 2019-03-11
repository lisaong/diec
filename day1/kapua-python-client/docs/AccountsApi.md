# swagger_client.AccountsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_count**](AccountsApi.md#account_count) | **POST** /{scopeId}/accounts/_count | Counts the Accounts
[**account_create**](AccountsApi.md#account_create) | **POST** /{scopeId}/accounts | Create an Account
[**account_delete**](AccountsApi.md#account_delete) | **DELETE** /{scopeId}/accounts/{accountId} | Delete an Account
[**account_find**](AccountsApi.md#account_find) | **GET** /{scopeId}/accounts/{accountId} | Get an Account
[**account_query**](AccountsApi.md#account_query) | **POST** /{scopeId}/accounts/_query | Queries the Accounts
[**account_simple_query**](AccountsApi.md#account_simple_query) | **GET** /{scopeId}/accounts | Gets the Account list in the scope
[**account_update**](AccountsApi.md#account_update) | **PUT** /{scopeId}/accounts/{accountId} | Update an Account


# **account_count**
> CountResult account_count(scope_id, body)

Counts the Accounts

Counts the Accounts with the given AccountQuery parameter returning the number of matching Accounts

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.AccountQuery() # AccountQuery | The AccountQuery to use to filter count results

try:
    # Counts the Accounts
    api_response = api_instance.account_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**AccountQuery**](AccountQuery.md)| The AccountQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_create**
> Account account_create(scope_id, body)

Create an Account

Creates a new Account based on the information provided in AccountCreator parameter.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the Account
body = swagger_client.AccountCreator() # AccountCreator | Provides the information for the new Account to be created

try:
    # Create an Account
    api_response = api_instance.account_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the Account | 
 **body** | [**AccountCreator**](AccountCreator.md)| Provides the information for the new Account to be created | 

### Return type

[**Account**](Account.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_delete**
> account_delete(scope_id, account_id)

Delete an Account

Deletes the Account specified by the \"accountId\" path parameter.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Account to delete.
account_id = 'account_id_example' # str | The id of the Account to be deleted

try:
    # Delete an Account
    api_instance.account_delete(scope_id, account_id)
except ApiException as e:
    print("Exception when calling AccountsApi->account_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Account to delete. | 
 **account_id** | **str**| The id of the Account to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_find**
> Account account_find(scope_id, account_id)

Get an Account

Returns the Account specified by the \"accountId\" path parameter.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Account.
account_id = 'account_id_example' # str | The id of the requested Account

try:
    # Get an Account
    api_response = api_instance.account_find(scope_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Account. | 
 **account_id** | **str**| The id of the requested Account | 

### Return type

[**Account**](Account.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_query**
> AccountListResult account_query(scope_id, body)

Queries the Accounts

Queries the Accounts with the given AccountQuery parameter returning all matching Accounts

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.AccountQuery() # AccountQuery | The AccountQuery to use to filter results.

try:
    # Queries the Accounts
    api_response = api_instance.account_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**AccountQuery**](AccountQuery.md)| The AccountQuery to use to filter results. | 

### Return type

[**AccountListResult**](AccountListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_simple_query**
> AccountListResult account_simple_query(scope_id, name=name, offset=offset, limit=limit)

Gets the Account list in the scope

Returns the list of all the accounts associated to the current selected scope.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
name = 'name_example' # str | The account name to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the Account list in the scope
    api_response = api_instance.account_simple_query(scope_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **name** | **str**| The account name to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**AccountListResult**](AccountListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_update**
> Account account_update(scope_id, account_id, body)

Update an Account

Updates a new Account based on the information provided in the Account parameter.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Account.
account_id = 'account_id_example' # str | The id of the requested Account
body = swagger_client.Account() # Account | The modified Account whose attributes needs to be updated

try:
    # Update an Account
    api_response = api_instance.account_update(scope_id, account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->account_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Account. | 
 **account_id** | **str**| The id of the requested Account | 
 **body** | [**Account**](Account.md)| The modified Account whose attributes needs to be updated | 

### Return type

[**Account**](Account.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

