# openapi_client.CoaAccountsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_coa_accounts**](CoaAccountsApi.md#get_coa_accounts) | **GET** /coa_accounts | Returns all Coa Accounts
[**get_coa_accounts_key**](CoaAccountsApi.md#get_coa_accounts_key) | **GET** /coa_accounts/{key} | Returns a Coa Account


# **get_coa_accounts**
> list[CoaAccount] get_coa_accounts(coa_template_id=coa_template_id, updated_or_created_since=updated_or_created_since, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)

Returns all Coa Accounts

Returns all Coa Accounts  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.CoaAccountsApi(api_client)
    coa_template_id = 'coa_template_id_example' # str | Use this to filter by COA Template (optional)
updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Coa Accounts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
show_legacy_id = True # bool | Display the legacy_id for the Coa Accounts. (optional)
items_per_page = 20 # int | Returns the given number of Coa Accounts per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Coa Accounts (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Coa Accounts (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns all Coa Accounts
        api_response = api_instance.get_coa_accounts(coa_template_id=coa_template_id, updated_or_created_since=updated_or_created_since, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoaAccountsApi->get_coa_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coa_template_id** | **str**| Use this to filter by COA Template | [optional] 
 **updated_or_created_since** | **datetime**| Use this to limit the response to Coa Accounts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Coa Accounts. | [optional] 
 **items_per_page** | **int**| Returns the given number of Coa Accounts per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Coa Accounts | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Coa Accounts (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**list[CoaAccount]**](CoaAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Coa Accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_coa_accounts_key**
> CoaAccount get_coa_accounts_key(key, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Coa Account

Returns a Coa Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸

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
    api_instance = openapi_client.CoaAccountsApi(api_client)
    key = 'key_example' # str | The Coa Account Key.
show_legacy_id = True # bool | Display the legacy_id for the Coa Account. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Coa Account (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Coa Account
        api_response = api_instance.get_coa_accounts_key(key, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CoaAccountsApi->get_coa_accounts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Coa Account Key. | 
 **show_legacy_id** | **bool**| Display the legacy_id for the Coa Account. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Coa Account (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**CoaAccount**](CoaAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Coa Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

