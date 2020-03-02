# openapi_client.TaxSchemesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_schemes**](TaxSchemesApi.md#get_tax_schemes) | **GET** /tax_schemes | Returns all Tax Schemes
[**get_tax_schemes_key**](TaxSchemesApi.md#get_tax_schemes_key) | **GET** /tax_schemes/{key} | Returns a Tax Scheme


# **get_tax_schemes**
> list[TaxScheme] get_tax_schemes(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Tax Schemes

Returns all Tax Schemes  ### Endpoint Availability  * Accounting: 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸 * Accounting Start: 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸

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
    api_instance = openapi_client.TaxSchemesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Tax Schemes. (optional)
items_per_page = 20 # int | Returns the given number of Tax Schemes per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Tax Schemes (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Schemes (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Tax Schemes
        api_response = api_instance.get_tax_schemes(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxSchemesApi->get_tax_schemes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Tax Schemes. | [optional] 
 **items_per_page** | **int**| Returns the given number of Tax Schemes per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Tax Schemes | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Schemes (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[TaxScheme]**](TaxScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Tax Schemes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_schemes_key**
> TaxScheme get_tax_schemes_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Tax Scheme

Returns a Tax Scheme  ### Endpoint Availability  * Accounting: 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸 * Accounting Start: 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸

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
    api_instance = openapi_client.TaxSchemesApi(api_client)
    key = 'key_example' # str | The Tax Scheme Key.
show_legacy_id = True # bool | Display the legacy_id for the Tax Scheme. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Scheme (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Tax Scheme
        api_response = api_instance.get_tax_schemes_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxSchemesApi->get_tax_schemes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Scheme Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Tax Scheme. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Scheme (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**TaxScheme**](TaxScheme.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Tax Scheme |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

