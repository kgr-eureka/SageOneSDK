# openapi_client.HostedArtefactPaymentSettingsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_hosted_artefact_payment_settings_key**](HostedArtefactPaymentSettingsApi.md#delete_hosted_artefact_payment_settings_key) | **DELETE** /hosted_artefact_payment_settings/{key} | Deletes a Hosted Artefact Payment Setting
[**get_hosted_artefact_payment_settings**](HostedArtefactPaymentSettingsApi.md#get_hosted_artefact_payment_settings) | **GET** /hosted_artefact_payment_settings | Returns all Hosted Artefact Payment Settings
[**get_hosted_artefact_payment_settings_key**](HostedArtefactPaymentSettingsApi.md#get_hosted_artefact_payment_settings_key) | **GET** /hosted_artefact_payment_settings/{key} | Returns a Hosted Artefact Payment Setting
[**post_hosted_artefact_payment_settings**](HostedArtefactPaymentSettingsApi.md#post_hosted_artefact_payment_settings) | **POST** /hosted_artefact_payment_settings | Creates a Hosted Artefact Payment Setting


# **delete_hosted_artefact_payment_settings_key**
> delete_hosted_artefact_payment_settings_key(key)

Deletes a Hosted Artefact Payment Setting

Deletes a Hosted Artefact Payment Setting  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access

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
    api_instance = openapi_client.HostedArtefactPaymentSettingsApi(api_client)
    key = 'key_example' # str | The Hosted Artefact Payment Setting Key.

    try:
        # Deletes a Hosted Artefact Payment Setting
        api_instance.delete_hosted_artefact_payment_settings_key(key)
    except ApiException as e:
        print("Exception when calling HostedArtefactPaymentSettingsApi->delete_hosted_artefact_payment_settings_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Hosted Artefact Payment Setting Key. | 

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
**204** | Deletes a Hosted Artefact Payment Setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_artefact_payment_settings**
> list[HostedArtefactPaymentSetting] get_hosted_artefact_payment_settings(object_guid=object_guid, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Hosted Artefact Payment Settings

Returns all Hosted Artefact Payment Settings  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = openapi_client.HostedArtefactPaymentSettingsApi(api_client)
    object_guid = 'object_guid_example' # str | Use this to filter out hosted artefact payment settings by the guid of the object it is associated to. (optional)
show_legacy_id = True # bool | Display the legacy_id for the Hosted Artefact Payment Settings. (optional)
items_per_page = 20 # int | Returns the given number of Hosted Artefact Payment Settings per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Hosted Artefact Payment Settings (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Hosted Artefact Payment Settings (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Hosted Artefact Payment Settings
        api_response = api_instance.get_hosted_artefact_payment_settings(object_guid=object_guid, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostedArtefactPaymentSettingsApi->get_hosted_artefact_payment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_guid** | **str**| Use this to filter out hosted artefact payment settings by the guid of the object it is associated to. | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Hosted Artefact Payment Settings. | [optional] 
 **items_per_page** | **int**| Returns the given number of Hosted Artefact Payment Settings per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Hosted Artefact Payment Settings | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Hosted Artefact Payment Settings (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[HostedArtefactPaymentSetting]**](HostedArtefactPaymentSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Hosted Artefact Payment Settings |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_artefact_payment_settings_key**
> HostedArtefactPaymentSetting get_hosted_artefact_payment_settings_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Hosted Artefact Payment Setting

Returns a Hosted Artefact Payment Setting  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Read Only, Restricted Access

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
    api_instance = openapi_client.HostedArtefactPaymentSettingsApi(api_client)
    key = 'key_example' # str | The Hosted Artefact Payment Setting Key.
show_legacy_id = True # bool | Display the legacy_id for the Hosted Artefact Payment Setting. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Hosted Artefact Payment Setting (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Hosted Artefact Payment Setting
        api_response = api_instance.get_hosted_artefact_payment_settings_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostedArtefactPaymentSettingsApi->get_hosted_artefact_payment_settings_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Hosted Artefact Payment Setting Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Hosted Artefact Payment Setting. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Hosted Artefact Payment Setting (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**HostedArtefactPaymentSetting**](HostedArtefactPaymentSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Hosted Artefact Payment Setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_hosted_artefact_payment_settings**
> HostedArtefactPaymentSetting post_hosted_artefact_payment_settings(hosted_artefact_payment_settings)

Creates a Hosted Artefact Payment Setting

Creates a Hosted Artefact Payment Setting  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Sales`: Full Access, Restricted Access

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
    api_instance = openapi_client.HostedArtefactPaymentSettingsApi(api_client)
    hosted_artefact_payment_settings = openapi_client.PostHostedArtefactPaymentSettings() # PostHostedArtefactPaymentSettings | 

    try:
        # Creates a Hosted Artefact Payment Setting
        api_response = api_instance.post_hosted_artefact_payment_settings(hosted_artefact_payment_settings)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HostedArtefactPaymentSettingsApi->post_hosted_artefact_payment_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hosted_artefact_payment_settings** | [**PostHostedArtefactPaymentSettings**](PostHostedArtefactPaymentSettings.md)|  | 

### Return type

[**HostedArtefactPaymentSetting**](HostedArtefactPaymentSetting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Hosted Artefact Payment Setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

