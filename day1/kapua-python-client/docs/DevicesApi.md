# swagger_client.DevicesApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_asset_filtered_get**](DevicesApi.md#device_asset_filtered_get) | **POST** /{scopeId}/devices/{deviceId}/assets | Gets a list of assets
[**device_asset_get**](DevicesApi.md#device_asset_get) | **GET** /{scopeId}/devices/{deviceId}/assets | Gets a list of assets
[**device_asset_read**](DevicesApi.md#device_asset_read) | **POST** /{scopeId}/devices/{deviceId}/assets/_read | Reads asset channel values
[**device_asset_write**](DevicesApi.md#device_asset_write) | **POST** /{scopeId}/devices/{deviceId}/assets/_write | Gets a list of assets
[**device_bundle_get**](DevicesApi.md#device_bundle_get) | **GET** /{scopeId}/devices/{deviceId}/bundles | Gets a list of bundles
[**device_bundle_start**](DevicesApi.md#device_bundle_start) | **POST** /{scopeId}/devices/{deviceId}/bundles/{bundleId}/_start | Start a bundle
[**device_bundle_stop**](DevicesApi.md#device_bundle_stop) | **POST** /{scopeId}/devices/{deviceId}/bundles/{bundleId}/_stop | Stop a bundle
[**device_command_execute**](DevicesApi.md#device_command_execute) | **POST** /{scopeId}/devices/{deviceId}/commands/_execute | Executes a command
[**device_configuration_component_get**](DevicesApi.md#device_configuration_component_get) | **GET** /{scopeId}/devices/{deviceId}/configurations/{componentId} | Gets the configuration of a component on a device
[**device_configuration_component_update**](DevicesApi.md#device_configuration_component_update) | **PUT** /{scopeId}/devices/{deviceId}/configurations/{componentId} | Updates the configuration of a component on a device
[**device_configuration_get**](DevicesApi.md#device_configuration_get) | **GET** /{scopeId}/devices/{deviceId}/configurations | Gets the device configurations
[**device_configuration_update**](DevicesApi.md#device_configuration_update) | **PUT** /{scopeId}/devices/{deviceId}/configurations | Updates a device configuration
[**device_count**](DevicesApi.md#device_count) | **POST** /{scopeId}/devices/_count | Counts the Devices
[**device_create**](DevicesApi.md#device_create) | **POST** /{scopeId}/devices | Create an Device
[**device_delete**](DevicesApi.md#device_delete) | **DELETE** /{scopeId}/devices/{deviceId} | Delete a Device
[**device_event_count**](DevicesApi.md#device_event_count) | **POST** /{scopeId}/devices/{deviceId}/events/_count | Counts the DeviceEvents
[**device_event_delete**](DevicesApi.md#device_event_delete) | **DELETE** /{scopeId}/devices/{deviceId}/events/{deviceEventId} | Delete a DeviceEvent
[**device_event_find**](DevicesApi.md#device_event_find) | **GET** /{scopeId}/devices/{deviceId}/events/{deviceEventId} | Get an DeviceEvent
[**device_event_query**](DevicesApi.md#device_event_query) | **POST** /{scopeId}/devices/{deviceId}/events/_query | Queries the DeviceEvents
[**device_event_simple_query**](DevicesApi.md#device_event_simple_query) | **GET** /{scopeId}/devices/{deviceId}/events | Gets the DeviceEvent list in the scope
[**device_find**](DevicesApi.md#device_find) | **GET** /{scopeId}/devices/{deviceId} | Get a Device
[**device_package_download**](DevicesApi.md#device_package_download) | **POST** /{scopeId}/devices/{deviceId}/packages/_download | Installs a package
[**device_package_get**](DevicesApi.md#device_package_get) | **GET** /{scopeId}/devices/{deviceId}/packages | Gets a list of packages
[**device_package_uninstall**](DevicesApi.md#device_package_uninstall) | **POST** /{scopeId}/devices/{deviceId}/packages/_uninstall | Uninstalls a package
[**device_query**](DevicesApi.md#device_query) | **POST** /{scopeId}/devices/_query | Queries the Devices
[**device_request_send**](DevicesApi.md#device_request_send) | **POST** /{scopeId}/devices/{deviceId}/requests | Sends a request
[**device_simple_query**](DevicesApi.md#device_simple_query) | **GET** /{scopeId}/devices | Gets the Device list in the scope
[**device_snapshot_get**](DevicesApi.md#device_snapshot_get) | **GET** /{scopeId}/devices/{deviceId}/snapshots | Gets a list of snapshots
[**device_snapshot_rollback**](DevicesApi.md#device_snapshot_rollback) | **POST** /{scopeId}/devices/{deviceId}/snapshots/{snapshotId}/_rollback | Gets a list of snapshots
[**device_update**](DevicesApi.md#device_update) | **PUT** /{scopeId}/devices/{deviceId} | Update a Device


# **device_asset_filtered_get**
> DeviceAssets device_asset_filtered_get(scope_id, device_id, timeout=timeout, body=body)

Gets a list of assets

Returns the list of all the Assets installed on the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)
body = swagger_client.DeviceAssets() # DeviceAssets | The filter of the request (optional)

try:
    # Gets a list of assets
    api_response = api_instance.device_asset_filtered_get(scope_id, device_id, timeout=timeout, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_asset_filtered_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 
 **body** | [**DeviceAssets**](DeviceAssets.md)| The filter of the request | [optional] 

### Return type

[**DeviceAssets**](DeviceAssets.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_get**
> DeviceAssets device_asset_get(scope_id, device_id, timeout=timeout)

Gets a list of assets

Returns the list of all the Assets installed on the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Gets a list of assets
    api_response = api_instance.device_asset_get(scope_id, device_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_asset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

[**DeviceAssets**](DeviceAssets.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_read**
> DeviceAssets device_asset_read(scope_id, device_id, timeout=timeout, body=body)

Reads asset channel values

Returns the value read from the asset channel

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)
body = swagger_client.DeviceAssets() # DeviceAssets | The filter of the read request (optional)

try:
    # Reads asset channel values
    api_response = api_instance.device_asset_read(scope_id, device_id, timeout=timeout, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_asset_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 
 **body** | [**DeviceAssets**](DeviceAssets.md)| The filter of the read request | [optional] 

### Return type

[**DeviceAssets**](DeviceAssets.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_asset_write**
> DeviceAssets device_asset_write(scope_id, device_id, timeout=timeout, body=body)

Gets a list of assets

Returns the list of all the Assets installed on the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)
body = swagger_client.DeviceAssets() # DeviceAssets | The values to write to the asset channels (optional)

try:
    # Gets a list of assets
    api_response = api_instance.device_asset_write(scope_id, device_id, timeout=timeout, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_asset_write: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 
 **body** | [**DeviceAssets**](DeviceAssets.md)| The values to write to the asset channels | [optional] 

### Return type

[**DeviceAssets**](DeviceAssets.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_bundle_get**
> DeviceBundles device_bundle_get(scope_id, device_id, timeout=timeout)

Gets a list of bundles

Returns the list of all the Bundles installed on the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Gets a list of bundles
    api_response = api_instance.device_bundle_get(scope_id, device_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_bundle_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

[**DeviceBundles**](DeviceBundles.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_bundle_start**
> device_bundle_start(scope_id, device_id, bundle_id, timeout=timeout)

Start a bundle

Starts the specified bundle

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
bundle_id = 'bundle_id_example' # str | the ID of the bundle to start
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Start a bundle
    api_instance.device_bundle_start(scope_id, device_id, bundle_id, timeout=timeout)
except ApiException as e:
    print("Exception when calling DevicesApi->device_bundle_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **bundle_id** | **str**| the ID of the bundle to start | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_bundle_stop**
> device_bundle_stop(scope_id, device_id, bundle_id, timeout=timeout)

Stop a bundle

Stops the specified bundle

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device.
device_id = 'device_id_example' # str | The id of the device
bundle_id = 'bundle_id_example' # str | the ID of the bundle to stop
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Stop a bundle
    api_instance.device_bundle_stop(scope_id, device_id, bundle_id, timeout=timeout)
except ApiException as e:
    print("Exception when calling DevicesApi->device_bundle_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device. | 
 **device_id** | **str**| The id of the device | 
 **bundle_id** | **str**| the ID of the bundle to stop | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_command_execute**
> DeviceCommandOutput device_command_execute(scope_id, device_id, body, timeout=timeout)

Executes a command

Executes a remote command on a device and return the command output.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device
device_id = 'device_id_example' # str | The id of the device
body = swagger_client.DeviceCommandInput() # DeviceCommandInput | The input command
timeout = 789 # int | The timeout of the command execution (optional)

try:
    # Executes a command
    api_response = api_instance.device_command_execute(scope_id, device_id, body, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_command_execute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device | 
 **device_id** | **str**| The id of the device | 
 **body** | [**DeviceCommandInput**](DeviceCommandInput.md)| The input command | 
 **timeout** | **int**| The timeout of the command execution | [optional] 

### Return type

[**DeviceCommandOutput**](DeviceCommandOutput.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_configuration_component_get**
> DeviceConfiguration device_configuration_component_get(scope_id, device_id, component_id, timeout=timeout)

Gets the configuration of a component on a device

Returns the configuration of a device or the configuration of the OSGi component identified with specified PID (service's persistent identity). In the OSGi framework, the service's persistent identity is defined as the name attribute of the Component Descriptor XML file; at runtime, the same value is also available in the component.name and in the service.pid attributes of the Component Configuration.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device.
device_id = 'device_id_example' # str | The id of the device
component_id = 'component_id_example' # str | An optional id of the component to get the configuration for
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Gets the configuration of a component on a device
    api_response = api_instance.device_configuration_component_get(scope_id, device_id, component_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_configuration_component_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device. | 
 **device_id** | **str**| The id of the device | 
 **component_id** | **str**| An optional id of the component to get the configuration for | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

[**DeviceConfiguration**](DeviceConfiguration.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_configuration_component_update**
> DeviceConfiguration device_configuration_component_update(scope_id, device_id, component_id, body, timeout=timeout)

Updates the configuration of a component on a device

Updates a device component configuration

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device.
device_id = 'device_id_example' # str | The id of the device
component_id = 'component_id_example' # str | The component id to update
body = swagger_client.DeviceComponentConfiguration() # DeviceComponentConfiguration | The component configuration to send to the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Updates the configuration of a component on a device
    api_response = api_instance.device_configuration_component_update(scope_id, device_id, component_id, body, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_configuration_component_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device. | 
 **device_id** | **str**| The id of the device | 
 **component_id** | **str**| The component id to update | 
 **body** | [**DeviceComponentConfiguration**](DeviceComponentConfiguration.md)| The component configuration to send to the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

[**DeviceConfiguration**](DeviceConfiguration.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_configuration_get**
> DeviceConfiguration device_configuration_get(scope_id, device_id, timeout=timeout)

Gets the device configurations

Returns the current configuration of a device

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device.
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Gets the device configurations
    api_response = api_instance.device_configuration_get(scope_id, device_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_configuration_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device. | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

[**DeviceConfiguration**](DeviceConfiguration.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_configuration_update**
> DeviceConfiguration device_configuration_update(scope_id, device_id, body, timeout=timeout)

Updates a device configuration

Updates a device configuration

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device.
device_id = 'device_id_example' # str | The id of the device
body = swagger_client.DeviceConfiguration() # DeviceConfiguration | The configuration to send to the device
timeout = 789 # int | The timeout of the operation in milliseconds (optional)

try:
    # Updates a device configuration
    api_response = api_instance.device_configuration_update(scope_id, device_id, body, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_configuration_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device. | 
 **device_id** | **str**| The id of the device | 
 **body** | [**DeviceConfiguration**](DeviceConfiguration.md)| The configuration to send to the device | 
 **timeout** | **int**| The timeout of the operation in milliseconds | [optional] 

### Return type

[**DeviceConfiguration**](DeviceConfiguration.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_count**
> CountResult device_count(scope_id, body)

Counts the Devices

Counts the Devices with the given DeviceQuery parameter returning the number of matching Devices

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results
body = swagger_client.DeviceQuery() # DeviceQuery | The DeviceQuery to use to filter count results

try:
    # Counts the Devices
    api_response = api_instance.device_count(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results | 
 **body** | [**DeviceQuery**](DeviceQuery.md)| The DeviceQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_create**
> Device device_create(scope_id, body)

Create an Device

Creates a new Device based on the information provided in DeviceCreator parameter.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to create the Device.
body = swagger_client.DeviceCreator() # DeviceCreator | Provides the information for the new Device to be created

try:
    # Create an Device
    api_response = api_instance.device_create(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to create the Device. | 
 **body** | [**DeviceCreator**](DeviceCreator.md)| Provides the information for the new Device to be created | 

### Return type

[**Device**](Device.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete**
> device_delete(scope_id, device_id)

Delete a Device

Deletes the Device specified by the \"deviceId\" path parameter.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device to delete.
device_id = 'device_id_example' # str | The id of the Device to be deleted

try:
    # Delete a Device
    api_instance.device_delete(scope_id, device_id)
except ApiException as e:
    print("Exception when calling DevicesApi->device_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device to delete. | 
 **device_id** | **str**| The id of the Device to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_count**
> CountResult device_event_count(scope_id, device_id, body)

Counts the DeviceEvents

Counts the DeviceEvents with the given DeviceEventQuery parameter returning the number of matching DeviceEvents

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to count results.
device_id = 'device_id_example' # str | The id of the Device in which to count results
body = swagger_client.DeviceEventQuery() # DeviceEventQuery | The DeviceEventQuery to use to filter count results

try:
    # Counts the DeviceEvents
    api_response = api_instance.device_event_count(scope_id, device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_event_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to count results. | 
 **device_id** | **str**| The id of the Device in which to count results | 
 **body** | [**DeviceEventQuery**](DeviceEventQuery.md)| The DeviceEventQuery to use to filter count results | 

### Return type

[**CountResult**](CountResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_delete**
> device_event_delete(scope_id, device_id, device_event_id)

Delete a DeviceEvent

Deletes the DeviceEvent specified by the \"deviceEventId\" path parameter.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | 
device_id = 'device_id_example' # str | The id of the Device in which to delete the event.
device_event_id = 'device_event_id_example' # str | The id of the DeviceEvent to be deleted

try:
    # Delete a DeviceEvent
    api_instance.device_event_delete(scope_id, device_id, device_event_id)
except ApiException as e:
    print("Exception when calling DevicesApi->device_event_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**|  | 
 **device_id** | **str**| The id of the Device in which to delete the event. | 
 **device_event_id** | **str**| The id of the DeviceEvent to be deleted | 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_find**
> DeviceEvent device_event_find(scope_id, device_id, device_event_id)

Get an DeviceEvent

Returns the DeviceEvent specified by the \"deviceEventId\" path parameter.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested DeviceEvent.
device_id = 'device_id_example' # str | The id of the requested Device
device_event_id = 'device_event_id_example' # str | The id of the requested DeviceEvent

try:
    # Get an DeviceEvent
    api_response = api_instance.device_event_find(scope_id, device_id, device_event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_event_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested DeviceEvent. | 
 **device_id** | **str**| The id of the requested Device | 
 **device_event_id** | **str**| The id of the requested DeviceEvent | 

### Return type

[**DeviceEvent**](DeviceEvent.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_query**
> DeviceEventListResult device_event_query(scope_id, device_id, body)

Queries the DeviceEvents

Queries the DeviceEvents with the given DeviceEvents parameter returning all matching DeviceEvents

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
device_id = 'device_id_example' # str | The id of the Device in which to search results
body = swagger_client.DeviceEventQuery() # DeviceEventQuery | The DeviceEventQuery to use to filter results.

try:
    # Queries the DeviceEvents
    api_response = api_instance.device_event_query(scope_id, device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_event_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **device_id** | **str**| The id of the Device in which to search results | 
 **body** | [**DeviceEventQuery**](DeviceEventQuery.md)| The DeviceEventQuery to use to filter results. | 

### Return type

[**DeviceEventListResult**](DeviceEventListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_event_simple_query**
> DeviceEventListResult device_event_simple_query(scope_id, device_id, resource=resource, offset=offset, limit=limit)

Gets the DeviceEvent list in the scope

Returns the list of all the deviceEvents associated to the current selected scope.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
device_id = 'device_id_example' # str | The client id to filter results.
resource = 'resource_example' # str | The resource of the DeviceEvent in which to search results (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the DeviceEvent list in the scope
    api_response = api_instance.device_event_simple_query(scope_id, device_id, resource=resource, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_event_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **device_id** | **str**| The client id to filter results. | 
 **resource** | **str**| The resource of the DeviceEvent in which to search results | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**DeviceEventListResult**](DeviceEventListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_find**
> Device device_find(scope_id, device_id)

Get a Device

Returns the Device specified by the \"deviceId\" path parameter.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Device
device_id = 'device_id_example' # str | The id of the requested Device

try:
    # Get a Device
    api_response = api_instance.device_find(scope_id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Device | 
 **device_id** | **str**| The id of the requested Device | 

### Return type

[**Device**](Device.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_package_download**
> device_package_download(scope_id, device_id, body, timeout=timeout)

Installs a package

Installs a package into the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device
device_id = 'device_id_example' # str | The id of the device
body = swagger_client.DevicePackageDownloadRequest() # DevicePackageDownloadRequest | Mandatory object with all the informations needed to download and install a package
timeout = 789 # int | The timeout of the operation (optional)

try:
    # Installs a package
    api_instance.device_package_download(scope_id, device_id, body, timeout=timeout)
except ApiException as e:
    print("Exception when calling DevicesApi->device_package_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device | 
 **device_id** | **str**| The id of the device | 
 **body** | [**DevicePackageDownloadRequest**](DevicePackageDownloadRequest.md)| Mandatory object with all the informations needed to download and install a package | 
 **timeout** | **int**| The timeout of the operation | [optional] 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_package_get**
> DeviceSnapshots device_package_get(scope_id, device_id, timeout=timeout)

Gets a list of packages

Returns the list of all the packages installed on the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation (optional)

try:
    # Gets a list of packages
    api_response = api_instance.device_package_get(scope_id, device_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_package_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation | [optional] 

### Return type

[**DeviceSnapshots**](DeviceSnapshots.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_package_uninstall**
> device_package_uninstall(scope_id, device_id, body, timeout=timeout)

Uninstalls a package

Uninstalls a package into the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the Device
device_id = 'device_id_example' # str | The id of the device
body = swagger_client.DevicePackageUninstallRequest() # DevicePackageUninstallRequest | Mandatory object with all the informations needed to uninstall a package
timeout = 789 # int | The timeout of the operation (optional)

try:
    # Uninstalls a package
    api_instance.device_package_uninstall(scope_id, device_id, body, timeout=timeout)
except ApiException as e:
    print("Exception when calling DevicesApi->device_package_uninstall: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the Device | 
 **device_id** | **str**| The id of the device | 
 **body** | [**DevicePackageUninstallRequest**](DevicePackageUninstallRequest.md)| Mandatory object with all the informations needed to uninstall a package | 
 **timeout** | **int**| The timeout of the operation | [optional] 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_query**
> DeviceListResult device_query(scope_id, body)

Queries the Devices

Queries the Devices with the given Devices parameter returning all matching Devices

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
body = swagger_client.DeviceQuery() # DeviceQuery | The DeviceQuery to use to filter results.

try:
    # Queries the Devices
    api_response = api_instance.device_query(scope_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **body** | [**DeviceQuery**](DeviceQuery.md)| The DeviceQuery to use to filter results. | 

### Return type

[**DeviceListResult**](DeviceListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_request_send**
> DeviceCommandOutput device_request_send(scope_id, device_id, body, timeout=timeout)

Sends a request

Sends a request message to a device

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device
device_id = 'device_id_example' # str | The id of the device
body = swagger_client.JsonGenericRequestMessage() # JsonGenericRequestMessage | The input request
timeout = 789 # int | The timeout of the request execution (optional)

try:
    # Sends a request
    api_response = api_instance.device_request_send(scope_id, device_id, body, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_request_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device | 
 **device_id** | **str**| The id of the device | 
 **body** | [**JsonGenericRequestMessage**](JsonGenericRequestMessage.md)| The input request | 
 **timeout** | **int**| The timeout of the request execution | [optional] 

### Return type

[**DeviceCommandOutput**](DeviceCommandOutput.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_simple_query**
> DeviceListResult device_simple_query(scope_id, tag_id=tag_id, client_id=client_id, status=status, fetch_attributes=fetch_attributes, offset=offset, limit=limit)

Gets the Device list in the scope

Returns the list of all the devices associated to the current selected scope.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId in which to search results.
tag_id = 'tag_id_example' # str | The tag id to filter results. (optional)
client_id = 'client_id_example' # str | The client id to filter results. (optional)
status = 'status_example' # str | The connection status to filter results. (optional)
fetch_attributes = ['fetch_attributes_example'] # list[str] | Additional attributes to be returned. Allowed values: connection, lastEvent (optional)
offset = 0 # int | The result set offset. (optional) (default to 0)
limit = 50 # int | The result set limit. (optional) (default to 50)

try:
    # Gets the Device list in the scope
    api_response = api_instance.device_simple_query(scope_id, tag_id=tag_id, client_id=client_id, status=status, fetch_attributes=fetch_attributes, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_simple_query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId in which to search results. | 
 **tag_id** | **str**| The tag id to filter results. | [optional] 
 **client_id** | **str**| The client id to filter results. | [optional] 
 **status** | **str**| The connection status to filter results. | [optional] 
 **fetch_attributes** | [**list[str]**](str.md)| Additional attributes to be returned. Allowed values: connection, lastEvent | [optional] 
 **offset** | **int**| The result set offset. | [optional] [default to 0]
 **limit** | **int**| The result set limit. | [optional] [default to 50]

### Return type

[**DeviceListResult**](DeviceListResult.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_snapshot_get**
> DeviceSnapshots device_snapshot_get(scope_id, device_id, timeout=timeout)

Gets a list of snapshots

Returns the list of all the Snapshots available on the device.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device
device_id = 'device_id_example' # str | The id of the device
timeout = 789 # int | The timeout of the operation (optional)

try:
    # Gets a list of snapshots
    api_response = api_instance.device_snapshot_get(scope_id, device_id, timeout=timeout)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_snapshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device | 
 **device_id** | **str**| The id of the device | 
 **timeout** | **int**| The timeout of the operation | [optional] 

### Return type

[**DeviceSnapshots**](DeviceSnapshots.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_snapshot_rollback**
> device_snapshot_rollback(scope_id, device_id, snapshot_id, timeout=timeout)

Gets a list of snapshots

Updates the configuration of a device rolling back a given snapshot ID.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the device
device_id = 'device_id_example' # str | The id of the device
snapshot_id = 'snapshot_id_example' # str | the ID of the snapshot to rollback to
timeout = 789 # int | The timeout of the operation (optional)

try:
    # Gets a list of snapshots
    api_instance.device_snapshot_rollback(scope_id, device_id, snapshot_id, timeout=timeout)
except ApiException as e:
    print("Exception when calling DevicesApi->device_snapshot_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the device | 
 **device_id** | **str**| The id of the device | 
 **snapshot_id** | **str**| the ID of the snapshot to rollback to | 
 **timeout** | **int**| The timeout of the operation | [optional] 

### Return type

void (empty response body)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_update**
> Device device_update(scope_id, device_id, body)

Update a Device

Updates a new Device based on the information provided in the Device parameter.

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
api_instance = swagger_client.DevicesApi(swagger_client.ApiClient(configuration))
scope_id = 'scope_id_example' # str | The ScopeId of the requested Device.
device_id = 'device_id_example' # str | The id of the requested Device
body = swagger_client.Device() # Device | The modified Device whose attributed need to be updated

try:
    # Update a Device
    api_response = api_instance.device_update(scope_id, device_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->device_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **str**| The ScopeId of the requested Device. | 
 **device_id** | **str**| The id of the requested Device | 
 **body** | [**Device**](Device.md)| The modified Device whose attributed need to be updated | 

### Return type

[**Device**](Device.md)

### Authorization

[kapuaAccessToken](../README.md#kapuaAccessToken)

### HTTP request headers

 - **Content-Type**: application/xml, application/json
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

