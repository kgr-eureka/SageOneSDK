# openapi_client.MigrationTaxReturnsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_migration_tax_returns**](MigrationTaxReturnsApi.md#get_migration_tax_returns) | **GET** /migration_tax_returns | Returns all Migration Tax Returns
[**get_migration_tax_returns_key**](MigrationTaxReturnsApi.md#get_migration_tax_returns_key) | **GET** /migration_tax_returns/{key} | Returns a Migration Tax Return
[**post_migration_tax_returns**](MigrationTaxReturnsApi.md#post_migration_tax_returns) | **POST** /migration_tax_returns | Creates a Migration Tax Return


# **get_migration_tax_returns**
> list[MigrationTaxReturn] get_migration_tax_returns(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Migration Tax Returns

Returns all Migration Tax Returns  ### Endpoint Availability  * Accounting: 🇬🇧, 🇮🇪 * Accounting Start: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Statutory Reporting`: Full Access

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
    api_instance = openapi_client.MigrationTaxReturnsApi(api_client)
    show_legacy_id = True # bool | Display the legacy_id for the Migration Tax Returns. (optional)
items_per_page = 20 # int | Returns the given number of Migration Tax Returns per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Migration Tax Returns (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Migration Tax Returns (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Migration Tax Returns
        api_response = api_instance.get_migration_tax_returns(show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MigrationTaxReturnsApi->get_migration_tax_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_legacy_id** | **bool**| Display the legacy_id for the Migration Tax Returns. | [optional] 
 **items_per_page** | **int**| Returns the given number of Migration Tax Returns per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Migration Tax Returns | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Migration Tax Returns (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[MigrationTaxReturn]**](MigrationTaxReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Migration Tax Returns |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_migration_tax_returns_key**
> MigrationTaxReturn get_migration_tax_returns_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Migration Tax Return

Returns a Migration Tax Return  ### Endpoint Availability  * Accounting: 🇬🇧, 🇮🇪 * Accounting Start: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Statutory Reporting`: Full Access

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
    api_instance = openapi_client.MigrationTaxReturnsApi(api_client)
    key = 'key_example' # str | The Migration Tax Return Key.
show_legacy_id = True # bool | Display the legacy_id for the Migration Tax Return. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Migration Tax Return (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Migration Tax Return
        api_response = api_instance.get_migration_tax_returns_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MigrationTaxReturnsApi->get_migration_tax_returns_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Migration Tax Return Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Migration Tax Return. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Migration Tax Return (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**MigrationTaxReturn**](MigrationTaxReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Migration Tax Return |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_migration_tax_returns**
> MigrationTaxReturn post_migration_tax_returns(migration_tax_returns)

Creates a Migration Tax Return

Creates a Migration Tax Return  ### Endpoint Availability  * Accounting: 🇬🇧, 🇮🇪 * Accounting Start: 🇬🇧, 🇮🇪  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Statutory Reporting`: Full Access

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
    api_instance = openapi_client.MigrationTaxReturnsApi(api_client)
    migration_tax_returns = openapi_client.PostMigrationTaxReturns() # PostMigrationTaxReturns | 

    try:
        # Creates a Migration Tax Return
        api_response = api_instance.post_migration_tax_returns(migration_tax_returns)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MigrationTaxReturnsApi->post_migration_tax_returns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migration_tax_returns** | [**PostMigrationTaxReturns**](PostMigrationTaxReturns.md)|  | 

### Return type

[**MigrationTaxReturn**](MigrationTaxReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Migration Tax Return |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

