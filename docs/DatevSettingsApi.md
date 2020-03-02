# openapi_client.DatevSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_datev_settings**](DatevSettingsApi.md#get_datev_settings) | **GET** /datev_settings | Returns all Datev Settings
[**put_datev_settings**](DatevSettingsApi.md#put_datev_settings) | **PUT** /datev_settings | Updates a Datev Settings


# **get_datev_settings**
> DatevSettings get_datev_settings(show_legacy_id=show_legacy_id)

Returns all Datev Settings

Returns all Datev Settings  ### Endpoint Availability  * Accounting: 🇩🇪 * Accounting Start: 🇩🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access, Read Only

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatevSettingsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Datev Settings. (optional)

    try:
        # Returns all Datev Settings
        api_response = api_instance.get_datev_settings(show_legacy_id=show_legacy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatevSettingsApi->get_datev_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Datev Settings. | [optional] 

### Return type

[**DatevSettings**](DatevSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Datev Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_datev_settings**
> DatevSettings put_datev_settings(datev_settings)

Updates a Datev Settings

Updates a Datev Settings  ### Endpoint Availability  * Accounting: 🇩🇪 * Accounting Start: 🇩🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatevSettingsApi(api_client)
    datev_settings = openapi_client.PutDatevSettings() # PutDatevSettings | 

    try:
        # Updates a Datev Settings
        api_response = api_instance.put_datev_settings(datev_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatevSettingsApi->put_datev_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datev_settings** | [**PutDatevSettings**](PutDatevSettings.md)|  | 

### Return type

[**DatevSettings**](DatevSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Datev Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

