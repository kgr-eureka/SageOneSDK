# openapi_client.LegalFormTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_legal_form_types**](LegalFormTypesApi.md#get_legal_form_types) | **GET** /legal_form_types | Returns all Legal Form Types
[**get_legal_form_types_key**](LegalFormTypesApi.md#get_legal_form_types_key) | **GET** /legal_form_types/{key} | Returns a Legal Form Type


# **get_legal_form_types**
> list[LegalFormType] get_legal_form_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Legal Form Types

Returns all Legal Form Types  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷

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
    api_instance = openapi_client.LegalFormTypesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Business Classifications. (optional)
items_per_page = 20 # int | Returns the given number of Business Classifications per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Business Classifications (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Classifications (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Legal Form Types
        api_response = api_instance.get_legal_form_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LegalFormTypesApi->get_legal_form_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Business Classifications. | [optional] 
 **items_per_page** | **int**| Returns the given number of Business Classifications per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Business Classifications | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Classifications (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[LegalFormType]**](LegalFormType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Legal Form Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_legal_form_types_key**
> LegalFormType get_legal_form_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Legal Form Type

Returns a Legal Form Type  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷

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
    api_instance = openapi_client.LegalFormTypesApi(api_client)
    key = 'key_example' # str | The Legal Form Type Key.
show_legacy_id = True # bool | Display the legacy_id for the Business Classification. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Business Classification (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Legal Form Type
        api_response = api_instance.get_legal_form_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LegalFormTypesApi->get_legal_form_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Legal Form Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Business Classification. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Business Classification (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**LegalFormType**](LegalFormType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Legal Form Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

