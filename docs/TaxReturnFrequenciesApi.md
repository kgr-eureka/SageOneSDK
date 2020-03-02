# openapi_client.TaxReturnFrequenciesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_return_frequencies**](TaxReturnFrequenciesApi.md#get_tax_return_frequencies) | **GET** /tax_return_frequencies | Returns all Tax Return Frequencies
[**get_tax_return_frequencies_key**](TaxReturnFrequenciesApi.md#get_tax_return_frequencies_key) | **GET** /tax_return_frequencies/{key} | Returns a Tax Return Frequency


# **get_tax_return_frequencies**
> list[Base] get_tax_return_frequencies(tax_type_id=tax_type_id, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Tax Return Frequencies

Returns all Tax Return Frequencies  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸

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
    api_instance = openapi_client.TaxReturnFrequenciesApi(api_client)
    tax_type_id = 'tax_type_id_example' # str | Use this to filter Tax Submission Frequency Types by tax_type_id (Canada only) (optional)
show_legacy_id = True # bool | Display the legacy_id for the Tax Submission Frequency Types. (optional)
items_per_page = 20 # int | Returns the given number of Tax Submission Frequency Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Tax Submission Frequency Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Submission Frequency Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Tax Return Frequencies
        api_response = api_instance.get_tax_return_frequencies(tax_type_id=tax_type_id, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxReturnFrequenciesApi->get_tax_return_frequencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_type_id** | **str**| Use this to filter Tax Submission Frequency Types by tax_type_id (Canada only) | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Tax Submission Frequency Types. | [optional] 
 **items_per_page** | **int**| Returns the given number of Tax Submission Frequency Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Tax Submission Frequency Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Submission Frequency Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[Base]**](Base.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Tax Return Frequencies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_return_frequencies_key**
> Base get_tax_return_frequencies_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Tax Return Frequency

Returns a Tax Return Frequency  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇫🇷, 🇬🇧, 🇮🇪, 🇪🇸

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
    api_instance = openapi_client.TaxReturnFrequenciesApi(api_client)
    key = 'key_example' # str | The Tax Return Frequency Key.
show_legacy_id = True # bool | Display the legacy_id for the Tax Submission Frequency Type. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Submission Frequency Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Tax Return Frequency
        api_response = api_instance.get_tax_return_frequencies_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxReturnFrequenciesApi->get_tax_return_frequencies_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Return Frequency Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Tax Submission Frequency Type. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Submission Frequency Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**Base**](Base.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Tax Return Frequency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

