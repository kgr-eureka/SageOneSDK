# openapi_client.LedgerAccountsApi

All URIs are relative to *https://api.accounting.sage.com/v3.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ledger_accounts**](LedgerAccountsApi.md#get_ledger_accounts) | **GET** /ledger_accounts | Returns all Ledger Accounts
[**get_ledger_accounts_key**](LedgerAccountsApi.md#get_ledger_accounts_key) | **GET** /ledger_accounts/{key} | Returns a Ledger Account
[**post_ledger_accounts**](LedgerAccountsApi.md#post_ledger_accounts) | **POST** /ledger_accounts | Creates a Ledger Account
[**put_ledger_accounts_key**](LedgerAccountsApi.md#put_ledger_accounts_key) | **PUT** /ledger_accounts/{key} | Updates a Ledger Account


# **get_ledger_accounts**
> list[LedgerAccount] get_ledger_accounts(updated_or_created_since=updated_or_created_since, visible_in=visible_in, not_visible_in=not_visible_in, show_included_in_chart=show_included_in_chart, show_control_accounts=show_control_accounts, ledger_account_classification_id=ledger_account_classification_id, show_balance_details=show_balance_details, exclude_deleted_entries=exclude_deleted_entries, from_date=from_date, to_date=to_date, search=search, sort_order_from_user_setting=sort_order_from_user_setting, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes, ledger_account_type_id=ledger_account_type_id)

Returns all Ledger Accounts

Returns all Ledger Accounts  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Full Access, Restricted Access, Read Only * Area: `Purchases`: Full Access, Restricted Access, Read Only * Area: `Products & Services`: Full Access, Restricted Access, Read Only * Area: `Contacts`: Full Access, Restricted Access, Read Only * Area: `Bank`: Full Access, Restricted Access, Read Only * Area: `Journals`: Full Access, Restricted Access, Read Only * Area: `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.LedgerAccountsApi(api_client)
    updated_or_created_since = '2013-10-20T19:20:30+01:00' # datetime | Use this to limit the response to Ledger Accounts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. (optional)
visible_in = 'visible_in_example' # str | Use this to limit the response to ledger account types visible in a specific area. Valid values are: banking, sales, expenses, other_payments, other_receipts, journals and reporting (optional)
not_visible_in = 'not_visible_in_example' # str | Use this to limit the response to ledger account types not visible in a specific area. (optional)
show_included_in_chart = True # bool | Use this to limit the response to ledger accounts that are/are not included in the chart (optional)
show_control_accounts = True # bool | Use this to limit the response to ledger accounts that are/are not control accounts (optional)
ledger_account_classification_id = 'ledger_account_classification_id_example' # str | Use this to filter by ledger account classification id (optional)
show_balance_details = True # bool | Use this to display the balance details for ledger accounts between a date range (requires from_date and to_date). (optional)
exclude_deleted_entries = True # bool | Exclude deleted ledger entries. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Calculate balances from this date. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Calculate balances to this date. (optional)
search = 'search_example' # str | Use this to filter by the item code or description (optional)
sort_order_from_user_setting = True # bool | Use this to enable ordering ledger accounts according to user settings. Defaulted to 'false'. (optional)
show_legacy_id = True # bool | Display the legacy_id for the Ledger Accounts. (optional)
items_per_page = 20 # int | Returns the given number of Ledger Accounts per request. (optional) (default to 20)
page = 1 # int | Go to specific page of Ledger Accounts (optional) (default to 1)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Accounts (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
ledger_account_type_id = 'ledger_account_type_id_example' # str | Use this to filter by ledger account type id (optional)

    try:
        # Returns all Ledger Accounts
        api_response = api_instance.get_ledger_accounts(updated_or_created_since=updated_or_created_since, visible_in=visible_in, not_visible_in=not_visible_in, show_included_in_chart=show_included_in_chart, show_control_accounts=show_control_accounts, ledger_account_classification_id=ledger_account_classification_id, show_balance_details=show_balance_details, exclude_deleted_entries=exclude_deleted_entries, from_date=from_date, to_date=to_date, search=search, sort_order_from_user_setting=sort_order_from_user_setting, show_legacy_id=show_legacy_id, items_per_page=items_per_page, page=page, attributes=attributes, ledger_account_type_id=ledger_account_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountsApi->get_ledger_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updated_or_created_since** | **datetime**| Use this to limit the response to Ledger Accounts changed since a given date (format: YYYY-MM-DDT(+|-)hh:mm) or date-time (format: YYYY-MM-DDThh:mm:ss(+|-)hh:mm). Inclusive of the passed timestamp. | [optional] 
 **visible_in** | **str**| Use this to limit the response to ledger account types visible in a specific area. Valid values are: banking, sales, expenses, other_payments, other_receipts, journals and reporting | [optional] 
 **not_visible_in** | **str**| Use this to limit the response to ledger account types not visible in a specific area. | [optional] 
 **show_included_in_chart** | **bool**| Use this to limit the response to ledger accounts that are/are not included in the chart | [optional] 
 **show_control_accounts** | **bool**| Use this to limit the response to ledger accounts that are/are not control accounts | [optional] 
 **ledger_account_classification_id** | **str**| Use this to filter by ledger account classification id | [optional] 
 **show_balance_details** | **bool**| Use this to display the balance details for ledger accounts between a date range (requires from_date and to_date). | [optional] 
 **exclude_deleted_entries** | **bool**| Exclude deleted ledger entries. | [optional] 
 **from_date** | **datetime**| Calculate balances from this date. | [optional] 
 **to_date** | **datetime**| Calculate balances to this date. | [optional] 
 **search** | **str**| Use this to filter by the item code or description | [optional] 
 **sort_order_from_user_setting** | **bool**| Use this to enable ordering ledger accounts according to user settings. Defaulted to &#39;false&#39;. | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Ledger Accounts. | [optional] 
 **items_per_page** | **int**| Returns the given number of Ledger Accounts per request. | [optional] [default to 20]
 **page** | **int**| Go to specific page of Ledger Accounts | [optional] [default to 1]
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Accounts (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **ledger_account_type_id** | **str**| Use this to filter by ledger account type id | [optional] 

### Return type

[**list[LedgerAccount]**](LedgerAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns all Ledger Accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ledger_accounts_key**
> LedgerAccount get_ledger_accounts_key(key, nested_attributes=nested_attributes, show_balance_details=show_balance_details, exclude_deleted_entries=exclude_deleted_entries, from_date=from_date, to_date=to_date, show_legacy_id=show_legacy_id, attributes=attributes)

Returns a Ledger Account

Returns a Ledger Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Sales`: Full Access, Restricted Access, Read Only * Area: `Purchases`: Full Access, Restricted Access, Read Only * Area: `Products & Services`: Full Access, Restricted Access, Read Only * Area: `Contacts`: Full Access, Restricted Access, Read Only * Area: `Bank`: Full Access, Restricted Access, Read Only * Area: `Journals`: Full Access, Restricted Access, Read Only * Area: `Settings`: Full Access, Read Only

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
    api_instance = openapi_client.LedgerAccountsApi(api_client)
    key = 'key_example' # str | The Ledger Account Key.
nested_attributes = 'nested_attributes_example' # str | Specify the attributes that you want to expose for nested entities of the Ledger Account (expose all nested attributes with 'all'). These are in addition to the base attributes (name, path) (optional)
show_balance_details = True # bool | Use this to display the balance details for ledger accounts between a date range (requires from_date and to_date). (optional)
exclude_deleted_entries = True # bool | Exclude deleted ledger entries. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Calculate balances from this date. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Calculate balances to this date. (optional)
show_legacy_id = True # bool | Display the legacy_id for the Ledger Account. (optional)
attributes = 'attributes_example' # str | Specify the attributes that you want to expose for the Ledger Account (expose all attributes with 'all'). These are in addition to the base attributes (name, path) (optional)

    try:
        # Returns a Ledger Account
        api_response = api_instance.get_ledger_accounts_key(key, nested_attributes=nested_attributes, show_balance_details=show_balance_details, exclude_deleted_entries=exclude_deleted_entries, from_date=from_date, to_date=to_date, show_legacy_id=show_legacy_id, attributes=attributes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountsApi->get_ledger_accounts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Key. | 
 **nested_attributes** | **str**| Specify the attributes that you want to expose for nested entities of the Ledger Account (expose all nested attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 
 **show_balance_details** | **bool**| Use this to display the balance details for ledger accounts between a date range (requires from_date and to_date). | [optional] 
 **exclude_deleted_entries** | **bool**| Exclude deleted ledger entries. | [optional] 
 **from_date** | **datetime**| Calculate balances from this date. | [optional] 
 **to_date** | **datetime**| Calculate balances to this date. | [optional] 
 **show_legacy_id** | **bool**| Display the legacy_id for the Ledger Account. | [optional] 
 **attributes** | **str**| Specify the attributes that you want to expose for the Ledger Account (expose all attributes with &#39;all&#39;). These are in addition to the base attributes (name, path) | [optional] 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a Ledger Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ledger_accounts**
> LedgerAccount post_ledger_accounts(ledger_accounts)

Creates a Ledger Account

Creates a Ledger Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.LedgerAccountsApi(api_client)
    ledger_accounts = openapi_client.PostLedgerAccounts() # PostLedgerAccounts | 

    try:
        # Creates a Ledger Account
        api_response = api_instance.post_ledger_accounts(ledger_accounts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountsApi->post_ledger_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_accounts** | [**PostLedgerAccounts**](PostLedgerAccounts.md)|  | 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Creates a Ledger Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ledger_accounts_key**
> LedgerAccount put_ledger_accounts_key(key, ledger_accounts)

Updates a Ledger Account

Updates a Ledger Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access

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
    api_instance = openapi_client.LedgerAccountsApi(api_client)
    key = 'key_example' # str | The Ledger Account Key.
ledger_accounts = openapi_client.PutLedgerAccounts() # PutLedgerAccounts | 

    try:
        # Updates a Ledger Account
        api_response = api_instance.put_ledger_accounts_key(key, ledger_accounts)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LedgerAccountsApi->put_ledger_accounts_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The Ledger Account Key. | 
 **ledger_accounts** | [**PutLedgerAccounts**](PutLedgerAccounts.md)|  | 

### Return type

[**LedgerAccount**](LedgerAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updates a Ledger Account |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

