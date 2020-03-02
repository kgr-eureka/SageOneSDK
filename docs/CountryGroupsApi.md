# openapi_client.CountryGroupsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_country_groups**](CountryGroupsApi.md#get_country_groups) | **GET** /country_groups | Returns all Country Groups
[**get_country_groups_key**](CountryGroupsApi.md#get_country_groups_key) | **GET** /country_groups/{key} | Returns a Country Group


# **get_country_groups**
> list[Base] get_country_groups(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Country Groups

Returns all Country Groups  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.CountryGroupsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Country Groups. (optional)
items_per_page = 20 # int | Returns the given number of Country Groups per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Country Groups (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Country Groups (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Country Groups
        api_response = api_instance.get_country_groups(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountryGroupsApi->get_country_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Country Groups. | [optional] 
 **items_per_page** | **int**| Returns the given number of Country Groups per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Country Groups | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Country Groups (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns all Country Groups |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country_groups_key**
> Base get_country_groups_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Country Group

Returns a Country Group  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.CountryGroupsApi(api_client)
    key = 'key_example' # str | The Country Group Key.
show_legacy_id = True # bool | Display the legacy_id for the Country Group. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Country Group (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Country Group
        api_response = api_instance.get_country_groups_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CountryGroupsApi->get_country_groups_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Country Group Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Country Group. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Country Group (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

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
**200** | Returns a Country Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

