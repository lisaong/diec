# swagger_client.AuthenticationApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authentication_api_key**](AuthenticationApi.md#authentication_api_key) | **POST** /authentication/apikey | Authenticate an user
[**authentication_jwt**](AuthenticationApi.md#authentication_jwt) | **POST** /authentication/jwt | Authenticate an user
[**authentication_logout**](AuthenticationApi.md#authentication_logout) | **POST** /authentication/logout | Logs out an user
[**authentication_refresh**](AuthenticationApi.md#authentication_refresh) | **POST** /authentication/refresh | Refreshes an AccessToken
[**authentication_user**](AuthenticationApi.md#authentication_user) | **POST** /authentication/user | Authenticate an user


# **authentication_api_key**
> AccessToken authentication_api_key(body)

Authenticate an user

Authenticates an user with API KEY and returns the authentication token to be used in subsequent REST API calls.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.ApiKeyCredentials() # ApiKeyCredentials | The API KEY authentication credential of a user.

try:
    # Authenticate an user
    api_response = api_instance.authentication_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiKeyCredentials**](ApiKeyCredentials.md)| The API KEY authentication credential of a user. | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_jwt**
> AccessToken authentication_jwt(body)

Authenticate an user

Authenticates an user with a JWT and returns the authentication token to be used in subsequent REST API calls.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.JwtCredentials() # JwtCredentials | The JWT authentication credential of a user.

try:
    # Authenticate an user
    api_response = api_instance.authentication_jwt(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_jwt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**JwtCredentials**](JwtCredentials.md)| The JWT authentication credential of a user. | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_logout**
> authentication_logout()

Logs out an user

Terminates the current session and invalidates the access token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()

try:
    # Logs out an user
    api_instance.authentication_logout()
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_refresh**
> AccessToken authentication_refresh(body)

Refreshes an AccessToken

Both the current AccessToken and the Refresh token will be invalidated. If also the Refresh token is expired, the user will have to restart with a new login.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.RefreshTokenCredentials() # RefreshTokenCredentials | The current AccessToken's tokenId and refreshToken

try:
    # Refreshes an AccessToken
    api_response = api_instance.authentication_refresh(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_refresh: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RefreshTokenCredentials**](RefreshTokenCredentials.md)| The current AccessToken&#39;s tokenId and refreshToken | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authentication_user**
> AccessToken authentication_user(body)

Authenticate an user

Authenticates an user with username and password and returns the authentication token to be used in subsequent REST API calls.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthenticationApi()
body = swagger_client.UsernamePasswordCredentials() # UsernamePasswordCredentials | The username and password authentication credential of a user.

try:
    # Authenticate an user
    api_response = api_instance.authentication_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authentication_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsernamePasswordCredentials**](UsernamePasswordCredentials.md)| The username and password authentication credential of a user. | 

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

