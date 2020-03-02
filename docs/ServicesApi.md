# openapi_client.ServicesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_services_key**](ServicesApi.md#delete_services_key) | **DELETE** /services/{key} | Deletes a Service
[**get_services**](ServicesApi.md#get_services) | **GET** /services | Returns all Services
[**get_services_key**](ServicesApi.md#get_services_key) | **GET** /services/{key} | Returns a Service
[**post_services**](ServicesApi.md#post_services) | **POST** /services | Creates a Service
[**put_services_key**](ServicesApi.md#put_services_key) | **PUT** /services/{key} | Updates a Service


# **delete_services_key**
> delete_services_key(key)

Deletes a Service

Deletes a Service  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Full Access

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
    api_instance = openapi_client.ServicesApi(api_client)
    key = 'key_example' # str | The Service Key.

    try:
        # Deletes a Service
        api_instance.delete_services_key(key)
    except ApiException as e:
        print("Exception when calling ServicesApi->delete_services_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Service Key. | 

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
**204** | Deletes a Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services**
> list[Service] get_services(search=search, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, active=active, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Services

Returns all Services  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = openapi_client.ServicesApi(api_client)
    search = 'search_example' # str | Use this to filter by the item code or description. (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Services changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
deleted_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Services deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. (optional)
active = True # bool | Use this to only return active or inactive items (optional)
show_legacy_id = True # bool | Display the legacy_id for the Services. (optional)
items_per_page = 20 # int | Returns the given number of Services per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Services (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Services (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Services
        api_response = api_instance.get_services(search=search, updated_or_created_since=updated_or_created_since, deleted_since=deleted_since, active=active, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServicesApi->get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Use this to filter by the item code or description. | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Services changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **deleted_since** | **datetime**| Use this to limit the response to Services deleted since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Not inclusive of the passed timestamp. | [optional] 
 **active** | **bool**| Use this to only return active or inactive items | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Services. | [optional] 
 **items_per_page** | **int**| Returns the given number of Services per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Services | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Services (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[Service]**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Services |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_services_key**
> Service get_services_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Service

Returns a Service  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Read Only, Restricted Access, Full Access * Area: `Sales`: Read Only, Restricted Access, Full Access * Area: `Purchases`: Read Only, Restricted Access, Full Access

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
    api_instance = openapi_client.ServicesApi(api_client)
    key = 'key_example' # str | The Service Key.
show_legacy_id = True # bool | Display the legacy_id for the Service. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Service (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Service
        api_response = api_instance.get_services_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServicesApi->get_services_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Service Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Service. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Service (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_services**
> Service post_services(services)

Creates a Service

Creates a Service  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access

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
    api_instance = openapi_client.ServicesApi(api_client)
    services = openapi_client.PostServices() # PostServices | 

    try:
        # Creates a Service
        api_response = api_instance.post_services(services)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServicesApi->post_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **services** | [**PostServices**](PostServices.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_services_key**
> Service put_services_key(key, services)

Updates a Service

Updates a Service  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Products & Services`: Restricted Access, Full Access

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
    api_instance = openapi_client.ServicesApi(api_client)
    key = 'key_example' # str | The Service Key.
services = openapi_client.PutServices() # PutServices | 

    try:
        # Updates a Service
        api_response = api_instance.put_services_key(key, services)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ServicesApi->put_services_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Service Key. | 
 **services** | [**PutServices**](PutServices.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Service |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

