# openapi_client.BusinessActivityTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_business_activity_types**](BusinessActivityTypesApi.md#get_business_activity_types) | **GET** /business_activity_types | Returns all Business Activity Types
[**get_business_activity_types_key**](BusinessActivityTypesApi.md#get_business_activity_types_key) | **GET** /business_activity_types/{key} | Returns a Business Activity Type


# **get_business_activity_types**
> list[BusinessActivityType] get_business_activity_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Business Activity Types

Returns all Business Activity Types  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷

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
    api_instance = openapi_client.BusinessActivityTypesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Business Classifications. (optional)
items_per_page = 20 # int | Returns the given number of Business Classifications per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Business Classifications (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Classifications (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Business Activity Types
        api_response = api_instance.get_business_activity_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessActivityTypesApi->get_business_activity_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Business Classifications. | [optional] 
 **items_per_page** | **int**| Returns the given number of Business Classifications per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Business Classifications | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Classifications (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[BusinessActivityType]**](BusinessActivityType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Business Activity Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_business_activity_types_key**
> BusinessActivityType get_business_activity_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Business Activity Type

Returns a Business Activity Type  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷

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
    api_instance = openapi_client.BusinessActivityTypesApi(api_client)
    key = 'key_example' # str | The Business Activity Type Key.
show_legacy_id = True # bool | Display the legacy_id for the Business Classification. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Classification (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Business Activity Type
        api_response = api_instance.get_business_activity_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BusinessActivityTypesApi->get_business_activity_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Business Activity Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Business Classification. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Classification (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**BusinessActivityType**](BusinessActivityType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Business Activity Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

