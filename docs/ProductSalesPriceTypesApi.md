# openapi_client.ProductSalesPriceTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_product_sales_price_types_key**](ProductSalesPriceTypesApi.md#delete_product_sales_price_types_key) | **DELETE** /product_sales_price_types/{key} | Deletes a Product Sales Price Type
[**get_product_sales_price_types**](ProductSalesPriceTypesApi.md#get_product_sales_price_types) | **GET** /product_sales_price_types | Returns all Product Sales Price Types
[**get_product_sales_price_types_key**](ProductSalesPriceTypesApi.md#get_product_sales_price_types_key) | **GET** /product_sales_price_types/{key} | Returns a Product Sales Price Type
[**post_product_sales_price_types**](ProductSalesPriceTypesApi.md#post_product_sales_price_types) | **POST** /product_sales_price_types | Creates a Product Sales Price Type
[**put_product_sales_price_types_key**](ProductSalesPriceTypesApi.md#put_product_sales_price_types_key) | **PUT** /product_sales_price_types/{key} | Updates a Product Sales Price Type


# **delete_product_sales_price_types_key**
> delete_product_sales_price_types_key(key)

Deletes a Product Sales Price Type

Deletes a Product Sales Price Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = openapi_client.ProductSalesPriceTypesApi(api_client)
    key = 'key_example' # str | The Product Sales Price Type Key.

    try:
        # Deletes a Product Sales Price Type
        api_instance.delete_product_sales_price_types_key(key)
    except ApiException as e:
        print("Exception when calling ProductSalesPriceTypesApi->delete_product_sales_price_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Product Sales Price Type Key. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deletes a Product Sales Price Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_sales_price_types**
> list[ProductSalesPriceType] get_product_sales_price_types(active=active, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Product Sales Price Types

Returns all Product Sales Price Types  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = openapi_client.ProductSalesPriceTypesApi(api_client)
    active = True # bool | Use this to only return active or inactive items (optional)
show_legacy_id = True # bool | Display the legacy_id for the Product Prices. (optional)
items_per_page = 20 # int | Returns the given number of Product Prices per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Product Prices (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Product Prices (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Product Sales Price Types
        api_response = api_instance.get_product_sales_price_types(active=active, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductSalesPriceTypesApi->get_product_sales_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active** | **bool**| Use this to only return active or inactive items | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Product Prices. | [optional] 
 **items_per_page** | **int**| Returns the given number of Product Prices per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Product Prices | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Product Prices (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[ProductSalesPriceType]**](ProductSalesPriceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Product Sales Price Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_sales_price_types_key**
> ProductSalesPriceType get_product_sales_price_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Product Sales Price Type

Returns a Product Sales Price Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = openapi_client.ProductSalesPriceTypesApi(api_client)
    key = 'key_example' # str | The Product Sales Price Type Key.
show_legacy_id = True # bool | Display the legacy_id for the Product Price. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Product Price (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Product Sales Price Type
        api_response = api_instance.get_product_sales_price_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductSalesPriceTypesApi->get_product_sales_price_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Product Sales Price Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Product Price. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Product Price (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ProductSalesPriceType**](ProductSalesPriceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Product Sales Price Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_product_sales_price_types**
> ProductSalesPriceType post_product_sales_price_types(product_sales_price_types)

Creates a Product Sales Price Type

Creates a Product Sales Price Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access

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
    api_instance = openapi_client.ProductSalesPriceTypesApi(api_client)
    product_sales_price_types = openapi_client.PostProductSalesPriceTypes() # PostProductSalesPriceTypes | 

    try:
        # Creates a Product Sales Price Type
        api_response = api_instance.post_product_sales_price_types(product_sales_price_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductSalesPriceTypesApi->post_product_sales_price_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_sales_price_types** | [**PostProductSalesPriceTypes**](PostProductSalesPriceTypes.md)|  | 

### Return type

[**ProductSalesPriceType**](ProductSalesPriceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Product Sales Price Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_product_sales_price_types_key**
> ProductSalesPriceType put_product_sales_price_types_key(key, product_sales_price_types)

Updates a Product Sales Price Type

Updates a Product Sales Price Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = openapi_client.ProductSalesPriceTypesApi(api_client)
    key = 'key_example' # str | The Product Sales Price Type Key.
product_sales_price_types = openapi_client.PutProductSalesPriceTypes() # PutProductSalesPriceTypes | 

    try:
        # Updates a Product Sales Price Type
        api_response = api_instance.put_product_sales_price_types_key(key, product_sales_price_types)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProductSalesPriceTypesApi->put_product_sales_price_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Product Sales Price Type Key. | 
 **product_sales_price_types** | [**PutProductSalesPriceTypes**](PutProductSalesPriceTypes.md)|  | 

### Return type

[**ProductSalesPriceType**](ProductSalesPriceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Product Sales Price Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

