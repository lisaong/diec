# swagger_client.DomainsApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**domain_count**](DomainsApi.md#domain_count) | **POST** /{scopeId}/domains/_count | Counts the Domains
[**domain_find**](DomainsApi.md#domain_find) | **GET** /{scopeId}/domains/{domainId} | Get a Domain
[**domain_query**](DomainsApi.md#domain_query) | **POST** /{scopeId}/domains/_query | Queries the Domains
[**domain_simple_query**](DomainsApi.md#domain_simple_query) | **GET** /{scopeId}/domains | Gets the Domain list in the scope


# **domain_count**
> CountResult domain_count(scope_id, body)

Counts the Domains

Counts the Domains with the given DomainQuery parameter returning the number of matching Domains

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
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.DomainQuery() # DomainQuery | The DomainQuery to use to filter count results

try:
    # Counts the Domains
    api_response = api_instance.domain_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domain_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**DomainQuery**](DomainQuery.md)| The DomainQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_find**
> Domain domain_find(scope_id, domain_id)

Get a Domain

Returns the Domain specified by the \"domainId\" path parameter.

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
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Domain.
domain_id = 'domain_id_example' # str | The id of the requested Domain

try:
    # Get a Domain
    api_response = api_instance.domain_find(scope_id, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domain_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Domain. | 
 **domain_id** | **str**| The id of the requested Domain | 

### Return type

[**Domain**](Domain.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_query**
> DomainListResult domain_query(scope_id, body)

Queries the Domains

Queries the Domains with the given DomainQuery parameter returning all matching Domains

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
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.DomainQuery() # DomainQuery | The DomainQuery to use to filter results.

try:
    # Queries the Domains
    api_response = api_instance.domain_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domain_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**DomainQuery**](DomainQuery.md)| The DomainQuery to use to filter results. | 

### Return type

[**DomainListResult**](DomainListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **domain_simple_query**
> DomainListResult domain_simple_query(scope_id, name=name, offset=offset, limit=limit)

Gets the Domain list in the scope

Returns the list of all the domains associated to the current selected scope.

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
api_instance = swagger_client.DomainsApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
name = 'name_example' # str | The domain name to filter results. (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the Domain list in the scope
    api_response = api_instance.domain_simple_query(scope_id, name=name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->domain_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **name** | **str**| The domain name to filter results. | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**DomainListResult**](DomainListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

