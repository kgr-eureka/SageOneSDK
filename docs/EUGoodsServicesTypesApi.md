# openapi_client.EUGoodsServicesTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_eu_goods_services_types**](EUGoodsServicesTypesApi.md#get_eu_goods_services_types) | **GET** /eu_goods_services_types | Returns all EU Goods Services Types
[**get_eu_goods_services_types_key**](EUGoodsServicesTypesApi.md#get_eu_goods_services_types_key) | **GET** /eu_goods_services_types/{key} | Returns a EU Goods Services Type


# **get_eu_goods_services_types**
> list[Base] get_eu_goods_services_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all EU Goods Services Types

Returns all EU Goods Services Types  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.EUGoodsServicesTypesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the EU Goods Services Types. (optional)
items_per_page = 20 # int | Returns the given number of EU Goods Services Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of EU Goods Services Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the EU Goods Services Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all EU Goods Services Types
        api_response = api_instance.get_eu_goods_services_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EUGoodsServicesTypesApi->get_eu_goods_services_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the EU Goods Services Types. | [optional] 
 **items_per_page** | **int**| Returns the given number of EU Goods Services Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of EU Goods Services Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the EU Goods Services Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all EU Goods Services Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_eu_goods_services_types_key**
> Base get_eu_goods_services_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a EU Goods Services Type

Returns a EU Goods Services Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.EUGoodsServicesTypesApi(api_client)
    key = 'key_example' # str | The EU Goods Services Type Key.
show_legacy_id = True # bool | Display the legacy_id for the EU Goods Services Type. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the EU Goods Services Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a EU Goods Services Type
        api_response = api_instance.get_eu_goods_services_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EUGoodsServicesTypesApi->get_eu_goods_services_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The EU Goods Services Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the EU Goods Services Type. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the EU Goods Services Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a EU Goods Services Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

