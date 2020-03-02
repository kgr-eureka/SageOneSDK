# openapi_client.BusinessSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_settings**](BusinessSettingsApi.md#get_business_settings) | **GET** /business_settings | Returns all Business Settings
[**put_business_settings**](BusinessSettingsApi.md#put_business_settings) | **PUT** /business_settings | Updates a Business Settings


# **get_business_settings**
> BusinessSettings get_business_settings(show_legacy_id=show_legacy_id)

Returns all Business Settings

Returns all Business Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.BusinessSettingsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Business Settings. (optional)

    try:
        # Returns all Business Settings
        api_response = api_instance.get_business_settings(show_legacy_id=show_legacy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessSettingsApi->get_business_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Business Settings. | [optional] 

### Return type

[**BusinessSettings**](BusinessSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Business Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_business_settings**
> BusinessSettings put_business_settings(business_settings)

Updates a Business Settings

Updates a Business Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Settings`: Full Access

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
    api_instance = openapi_client.BusinessSettingsApi(api_client)
    business_settings = openapi_client.PutBusinessSettings() # PutBusinessSettings | 

    try:
        # Updates a Business Settings
        api_response = api_instance.put_business_settings(business_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessSettingsApi->put_business_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_settings** | [**PutBusinessSettings**](PutBusinessSettings.md)|  | 

### Return type

[**BusinessSettings**](BusinessSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Business Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

