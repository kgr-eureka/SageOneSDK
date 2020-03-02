# openapi_client.EmailSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_email_settings**](EmailSettingsApi.md#get_email_settings) | **GET** /email_settings | Returns all Email Settings
[**put_email_settings**](EmailSettingsApi.md#put_email_settings) | **PUT** /email_settings | Updates a Email Settings


# **get_email_settings**
> EmailSettings get_email_settings(show_legacy_id=show_legacy_id)

Returns all Email Settings

Returns all Email Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.EmailSettingsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Email Settings. (optional)

    try:
        # Returns all Email Settings
        api_response = api_instance.get_email_settings(show_legacy_id=show_legacy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailSettingsApi->get_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Email Settings. | [optional] 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Email Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_email_settings**
> EmailSettings put_email_settings(email_settings)

Updates a Email Settings

Updates a Email Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.EmailSettingsApi(api_client)
    email_settings = openapi_client.PutEmailSettings() # PutEmailSettings | 

    try:
        # Updates a Email Settings
        api_response = api_instance.put_email_settings(email_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EmailSettingsApi->put_email_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_settings** | [**PutEmailSettings**](PutEmailSettings.md)|  | 

### Return type

[**EmailSettings**](EmailSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Email Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

