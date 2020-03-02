# openapi_client.JournalCodesApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_journal_codes_key**](JournalCodesApi.md#delete_journal_codes_key) | **DELETE** /journal_codes/{key} | Deletes a Journal Code
[**get_journal_codes**](JournalCodesApi.md#get_journal_codes) | **GET** /journal_codes | Returns all Journal Codes
[**get_journal_codes_key**](JournalCodesApi.md#get_journal_codes_key) | **GET** /journal_codes/{key} | Returns a Journal Code
[**post_journal_codes**](JournalCodesApi.md#post_journal_codes) | **POST** /journal_codes | Creates a Journal Code
[**put_journal_codes_key**](JournalCodesApi.md#put_journal_codes_key) | **PUT** /journal_codes/{key} | Updates a Journal Code


# **delete_journal_codes_key**
> delete_journal_codes_key(key)

Deletes a Journal Code

Deletes a Journal Code  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.JournalCodesApi(api_client)
    key = 'key_example' # str | The Journal Code Key.

    try:
        # Deletes a Journal Code
        api_instance.delete_journal_codes_key(key)
    except ApiException as e:
        print("Exception when calling JournalCodesApi->delete_journal_codes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Journal Code Key. | 

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
**204** | Deletes a Journal Code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_codes**
> list[JournalCode] get_journal_codes(updated_or_created_since=updated_or_created_since, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Journal Codes

Returns all Journal Codes  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Journals`: Full Access, Read Only * Area: `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.JournalCodesApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Journal Codes changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
show_legacy_id = True # bool | Display the legacy_id for the Journal Codes. (optional)
items_per_page = 20 # int | Returns the given number of Journal Codes per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Journal Codes (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Journal Codes (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Journal Codes
        api_response = api_instance.get_journal_codes(updated_or_created_since=updated_or_created_since, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalCodesApi->get_journal_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Journal Codes changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Journal Codes. | [optional] 
 **items_per_page** | **int**| Returns the given number of Journal Codes per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Journal Codes | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Journal Codes (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[JournalCode]**](JournalCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Journal Codes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_journal_codes_key**
> JournalCode get_journal_codes_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Journal Code

Returns a Journal Code  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Journals`: Full Access, Read Only * Area: `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.JournalCodesApi(api_client)
    key = 'key_example' # str | The Journal Code Key.
show_legacy_id = True # bool | Display the legacy_id for the Journal Code. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Journal Code (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Journal Code
        api_response = api_instance.get_journal_codes_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalCodesApi->get_journal_codes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Journal Code Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Journal Code. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Journal Code (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**JournalCode**](JournalCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Journal Code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_journal_codes**
> JournalCode post_journal_codes(journal_codes)

Creates a Journal Code

Creates a Journal Code  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.JournalCodesApi(api_client)
    journal_codes = openapi_client.PostJournalCodes() # PostJournalCodes | 

    try:
        # Creates a Journal Code
        api_response = api_instance.post_journal_codes(journal_codes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalCodesApi->post_journal_codes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **journal_codes** | [**PostJournalCodes**](PostJournalCodes.md)|  | 

### Return type

[**JournalCode**](JournalCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Journal Code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_journal_codes_key**
> JournalCode put_journal_codes_key(key, journal_codes)

Updates a Journal Code

Updates a Journal Code  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.JournalCodesApi(api_client)
    key = 'key_example' # str | The Journal Code Key.
journal_codes = openapi_client.PutJournalCodes() # PutJournalCodes | 

    try:
        # Updates a Journal Code
        api_response = api_instance.put_journal_codes_key(key, journal_codes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JournalCodesApi->put_journal_codes_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Journal Code Key. | 
 **journal_codes** | [**PutJournalCodes**](PutJournalCodes.md)|  | 

### Return type

[**JournalCode**](JournalCode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Journal Code |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

