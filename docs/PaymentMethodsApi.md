# openapi_client.PaymentMethodsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payment_methods**](PaymentMethodsApi.md#get_payment_methods) | **GET** /payment_methods | Returns all Payment Methods
[**get_payment_methods_key**](PaymentMethodsApi.md#get_payment_methods_key) | **GET** /payment_methods/{key} | Returns a Payment Method


# **get_payment_methods**
> list[Base] get_payment_methods(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Payment Methods

Returns all Payment Methods  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Payment Types. (optional)
items_per_page = 20 # int | Returns the given number of Payment Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Payment Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Payment Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Payment Methods
        api_response = api_instance.get_payment_methods(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->get_payment_methods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Payment Types. | [optional] 
 **items_per_page** | **int**| Returns the given number of Payment Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Payment Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Payment Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Payment Methods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_methods_key**
> Base get_payment_methods_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Payment Method

Returns a Payment Method  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.PaymentMethodsApi(api_client)
    key = 'key_example' # str | The Payment Method Key.
show_legacy_id = True # bool | Display the legacy_id for the Payment Type. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Payment Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Payment Method
        api_response = api_instance.get_payment_methods_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentMethodsApi->get_payment_methods_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Payment Method Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Payment Type. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Payment Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Payment Method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

