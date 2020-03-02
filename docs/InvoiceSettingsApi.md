# openapi_client.InvoiceSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_settings**](InvoiceSettingsApi.md#get_invoice_settings) | **GET** /invoice_settings | Returns all Invoice Settings
[**put_invoice_settings**](InvoiceSettingsApi.md#put_invoice_settings) | **PUT** /invoice_settings | Updates a Invoice Settings


# **get_invoice_settings**
> InvoiceSettings get_invoice_settings(show_legacy_id=show_legacy_id)

Returns all Invoice Settings

Returns all Invoice Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.InvoiceSettingsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Invoice Settings. (optional)

    try:
        # Returns all Invoice Settings
        api_response = api_instance.get_invoice_settings(show_legacy_id=show_legacy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvoiceSettingsApi->get_invoice_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Invoice Settings. | [optional] 

### Return type

[**InvoiceSettings**](InvoiceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Invoice Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_invoice_settings**
> InvoiceSettings put_invoice_settings(invoice_settings)

Updates a Invoice Settings

Updates a Invoice Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.InvoiceSettingsApi(api_client)
    invoice_settings = openapi_client.PutInvoiceSettings() # PutInvoiceSettings | 

    try:
        # Updates a Invoice Settings
        api_response = api_instance.put_invoice_settings(invoice_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InvoiceSettingsApi->put_invoice_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_settings** | [**PutInvoiceSettings**](PutInvoiceSettings.md)|  | 

### Return type

[**InvoiceSettings**](InvoiceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Invoice Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

