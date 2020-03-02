# openapi_client.ArtefactStatusesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_artefact_statuses**](ArtefactStatusesApi.md#get_artefact_statuses) | **GET** /artefact_statuses | Returns all Artefact Statuses
[**get_artefact_statuses_key**](ArtefactStatusesApi.md#get_artefact_statuses_key) | **GET** /artefact_statuses/{key} | Returns a Artefact Status


# **get_artefact_statuses**
> list[Base] get_artefact_statuses(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Artefact Statuses

Returns all Artefact Statuses  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.ArtefactStatusesApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Artefact Statuses. (optional)
items_per_page = 20 # int | Returns the given number of Artefact Statuses per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Artefact Statuses (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Artefact Statuses (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Artefact Statuses
        api_response = api_instance.get_artefact_statuses(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtefactStatusesApi->get_artefact_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Artefact Statuses. | [optional] 
 **items_per_page** | **int**| Returns the given number of Artefact Statuses per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Artefact Statuses | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Artefact Statuses (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Artefact Statuses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artefact_statuses_key**
> Base get_artefact_statuses_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Artefact Status

Returns a Artefact Status  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.ArtefactStatusesApi(api_client)
    key = 'key_example' # str | The Artefact Status Key.
show_legacy_id = True # bool | Display the legacy_id for the Artefact Status. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Artefact Status (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Artefact Status
        api_response = api_instance.get_artefact_statuses_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ArtefactStatusesApi->get_artefact_statuses_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Artefact Status Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Artefact Status. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Artefact Status (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Artefact Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

