# openapi_client.UnallocatedArtefactsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_unallocated_artefacts**](UnallocatedArtefactsApi.md#get_unallocated_artefacts) | **GET** /unallocated_artefacts | Returns all Unallocated Artefacts
[**get_unallocated_artefacts_key**](UnallocatedArtefactsApi.md#get_unallocated_artefacts_key) | **GET** /unallocated_artefacts/{key} | Returns a Unallocated Artefact


# **get_unallocated_artefacts**
> list[UnallocatedArtefact] get_unallocated_artefacts(contact_id=contact_id, search=search, attributes=attributes, items_per_page=items_per_page, page=page, show_legacy_id=show_legacy_id)

Returns all Unallocated Artefacts

Returns all Unallocated Artefacts  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.UnallocatedArtefactsApi(api_client)
    contact_id = 'contact_id_example' # str | Use this to filter by contact id (optional)
search = 'search_example' # str | Use this to filter by the contact identifier. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Base Artefacts (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
items_per_page = 20 # int | Returns the given number of Base Artefacts per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Base Artefacts (optional) (default to 1)
show_legacy_id = True # bool | Display the legacy_id for the Base Artefacts. (optional)

    try:
        # Returns all Unallocated Artefacts
        api_response = api_instance.get_unallocated_artefacts(contact_id=contact_id, search=search, attributes=attributes, items_per_page=items_per_page, page=page, show_legacy_id=show_legacy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UnallocatedArtefactsApi->get_unallocated_artefacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_id** | **str**| Use this to filter by contact id | [optional] 
 **search** | **str**| Use this to filter by the contact identifier. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Base Artefacts (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **items_per_page** | **int**| Returns the given number of Base Artefacts per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Base Artefacts | [optional] [default to 1]
 **show_legacy_id** | **bool**| Display the legacy_id for the Base Artefacts. | [optional] 

### Return type

[**list[UnallocatedArtefact]**](UnallocatedArtefact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Unallocated Artefacts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unallocated_artefacts_key**
> UnallocatedArtefact get_unallocated_artefacts_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Unallocated Artefact

Returns a Unallocated Artefact  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.UnallocatedArtefactsApi(api_client)
    key = 'key_example' # str | The Unallocated Artefact Key.
show_legacy_id = True # bool | Display the legacy_id for the Base Artefact. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Base Artefact (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Unallocated Artefact
        api_response = api_instance.get_unallocated_artefacts_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UnallocatedArtefactsApi->get_unallocated_artefacts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Unallocated Artefact Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Base Artefact. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Base Artefact (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**UnallocatedArtefact**](UnallocatedArtefact.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Unallocated Artefact |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

