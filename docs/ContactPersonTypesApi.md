# openapi_client.ContactPersonTypesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_contact_person_types**](ContactPersonTypesApi.md#get_contact_person_types) | **GET** /contact_person_types | Returns all Contact Person Types
[**get_contact_person_types_key**](ContactPersonTypesApi.md#get_contact_person_types_key) | **GET** /contact_person_types/{key} | Returns a Contact Person Type


# **get_contact_person_types**
> list[ContactPersonType] get_contact_person_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Contact Person Types

Returns all Contact Person Types  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.ContactPersonTypesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Contact Types. (optional)
items_per_page = 20 # int | Returns the given number of Contact Types per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Contact Types (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Contact Types (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Contact Person Types
        api_response = api_instance.get_contact_person_types(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPersonTypesApi->get_contact_person_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Contact Types. | [optional] 
 **items_per_page** | **int**| Returns the given number of Contact Types per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Contact Types | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Contact Types (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[ContactPersonType]**](ContactPersonType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Contact Person Types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_person_types_key**
> ContactPersonType get_contact_person_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Contact Person Type

Returns a Contact Person Type  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.ContactPersonTypesApi(api_client)
    key = 'key_example' # str | The Contact Person Type Key.
show_legacy_id = True # bool | Display the legacy_id for the Contact Type. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Contact Type (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Contact Person Type
        api_response = api_instance.get_contact_person_types_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContactPersonTypesApi->get_contact_person_types_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Contact Person Type Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Contact Type. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Contact Type (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**ContactPersonType**](ContactPersonType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Contact Person Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

