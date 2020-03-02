# openapi_client.ExchangeRatesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_exchange_rates**](ExchangeRatesApi.md#get_exchange_rates) | **GET** /exchange_rates | Returns all Exchange Rates
[**get_exchange_rates_key**](ExchangeRatesApi.md#get_exchange_rates_key) | **GET** /exchange_rates/{key} | Returns a Exchange Rate


# **get_exchange_rates**
> list[ExchangeRate] get_exchange_rates(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Exchange Rates

Returns all Exchange Rates  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.ExchangeRatesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Currencies. (optional)
items_per_page = 20 # int | Returns the given number of Currencies per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Currencies (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Currencies (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Exchange Rates
        api_response = api_instance.get_exchange_rates(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangeRatesApi->get_exchange_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Currencies. | [optional] 
 **items_per_page** | **int**| Returns the given number of Currencies per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Currencies | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Currencies (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[ExchangeRate]**](ExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Exchange Rates |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exchange_rates_key**
> ExchangeRate get_exchange_rates_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Exchange Rate

Returns a Exchange Rate  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.ExchangeRatesApi(api_client)
    key = 'key_example' # str | The Exchange Rate Key.
show_legacy_id = True # bool | Display the legacy_id for the Currency. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Currency (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Exchange Rate
        api_response = api_instance.get_exchange_rates_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ExchangeRatesApi->get_exchange_rates_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Exchange Rate Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Currency. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Currency (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ExchangeRate**](ExchangeRate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Exchange Rate |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

