# openapi_client.TaxTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tax_types**](TaxTypesApi.md#get_tax_types) | **GET** /tax_types | Returns all Tax Types
[**get_tax_types_key**](TaxTypesApi.md#get_tax_types_key) | **GET** /tax_types/{key} | Returns a Tax Type


# **get_tax_types**
> list[TaxType] get_tax_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Tax Types

Returns all Tax Types  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.TaxTypesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Tax Types. (optional)
items_per_page = 20 # int | Returns the given number of Tax Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Tax Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Tax Types
        api_response = api_instance.get_tax_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxTypesApi->get_tax_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Tax Types. | [optional] 
 **items_per_page** | **int**| Returns the given number of Tax Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Tax Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[TaxType]**](TaxType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Tax Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tax_types_key**
> TaxType get_tax_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Tax Type

Returns a Tax Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.TaxTypesApi(api_client)
    key = 'key_example' # str | The Tax Type Key.
show_legacy_id = True # bool | Display the legacy_id for the Tax Type. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Tax Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Tax Type
        api_response = api_instance.get_tax_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TaxTypesApi->get_tax_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Tax Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Tax Type. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Tax Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**TaxType**](TaxType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Tax Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

