# openapi_client.BusinessTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_types**](BusinessTypesApi.md#get_business_types) | **GET** /business_types | Returns all Business Types
[**get_business_types_key**](BusinessTypesApi.md#get_business_types_key) | **GET** /business_types/{key} | Returns a Business Type


# **get_business_types**
> list[BusinessType] get_business_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Business Types

Returns all Business Types  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.BusinessTypesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the For Business Types. (optional)
items_per_page = 20 # int | Returns the given number of For Business Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of For Business Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the For Business Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Business Types
        api_response = api_instance.get_business_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessTypesApi->get_business_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the For Business Types. | [optional] 
 **items_per_page** | **int**| Returns the given number of For Business Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of For Business Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the For Business Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[BusinessType]**](BusinessType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Business Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_types_key**
> BusinessType get_business_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Business Type

Returns a Business Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.BusinessTypesApi(api_client)
    key = 'key_example' # str | The Business Type Key.
show_legacy_id = True # bool | Display the legacy_id for the For Business Type. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the For Business Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Business Type
        api_response = api_instance.get_business_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessTypesApi->get_business_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Business Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the For Business Type. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the For Business Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**BusinessType**](BusinessType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Business Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

