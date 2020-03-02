# openapi_client.FinancialSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_financial_settings**](FinancialSettingsApi.md#get_financial_settings) | **GET** /financial_settings | Returns all Financial Settings
[**put_financial_settings**](FinancialSettingsApi.md#put_financial_settings) | **PUT** /financial_settings | Updates a Financial Settings


# **get_financial_settings**
> FinancialSettings get_financial_settings(show_legacy_id=show_legacy_id)

Returns all Financial Settings

Returns all Financial Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.FinancialSettingsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Financial Settings. (optional)

    try:
        # Returns all Financial Settings
        api_response = api_instance.get_financial_settings(show_legacy_id=show_legacy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialSettingsApi->get_financial_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Financial Settings. | [optional] 

### Return type

[**FinancialSettings**](FinancialSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Financial Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_financial_settings**
> FinancialSettings put_financial_settings(financial_settings)

Updates a Financial Settings

Updates a Financial Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.FinancialSettingsApi(api_client)
    financial_settings = openapi_client.PutFinancialSettings() # PutFinancialSettings | 

    try:
        # Updates a Financial Settings
        api_response = api_instance.put_financial_settings(financial_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FinancialSettingsApi->put_financial_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **financial_settings** | [**PutFinancialSettings**](PutFinancialSettings.md)|  | 

### Return type

[**FinancialSettings**](FinancialSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Financial Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

