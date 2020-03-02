# openapi_client.CountriesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](CountriesApi.md#get_countries) | **GET** /countries | Returns all Countries
[**get_countries_key**](CountriesApi.md#get_countries_key) | **GET** /countries/{key} | Returns a Country


# **get_countries**
> list[Base] get_countries(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Countries

Returns all Countries  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.CountriesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Countries. (optional)
items_per_page = 20 # int | Returns the given number of Countries per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Countries (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Countries (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Countries
        api_response = api_instance.get_countries(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountriesApi->get_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Countries. | [optional] 
 **items_per_page** | **int**| Returns the given number of Countries per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Countries | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Countries (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Countries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries_key**
> Base get_countries_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Country

Returns a Country  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.CountriesApi(api_client)
    key = 'key_example' # str | The Country Key.
show_legacy_id = True # bool | Display the legacy_id for the Country. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Country (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Country
        api_response = api_instance.get_countries_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountriesApi->get_countries_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Country Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Country. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Country (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Country |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

