# LedgerAccount

Creates a Ledger Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_id** | **int** | The legacy ID for the item | [optional] 
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**ledger_account_group** | [**CoaGroupType**](CoaGroupType.md) |  | [optional] 
**name** | **str** | The name for the ledger account. Changes to this field do not propagate to other resources, namely not to the name of the associated bank_account (unlike the behaviour of the UI). | [optional] 
**display_name** | **str** | The display name for the ledger account | [optional] 
**visible_scopes** | **list[str]** | The visible scopes. | [optional] 
**included_in_chart** | **bool** | Indicates whether the ledger account is included in the chart of accounts | [optional] 
**nominal_code** | **int** | The nominal code of the ledger account | [optional] 
**ledger_account_type** | [**Base**](Base.md) |  | [optional] 
**ledger_account_classification** | [**Base**](Base.md) |  | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**fixed_tax_rate** | **bool** | Indicates whether the default tax rate is fixed or may be changed | [optional] 
**visible_in_banking** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_expenses** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_journals** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_other_payments** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_other_receipts** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_reporting** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_sales** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**balance_details** | [**LedgerAccountBalanceDetails**](LedgerAccountBalanceDetails.md) |  | [optional] 
**is_control_account** | **bool** | Indicates whether the ledger account is a control account | [optional] 
**control_name** | **str** | The control name for the ledger account | [optional] 
**display_formatted** | **str** | The display name formatted based on coa_list_order in settings | [optional] 
**tax_recoverable** | **bool** | Indicates that transactions posted to this ledger account have part recoverable taxes (Canada only) | [optional] 
**recoverable_percentage** | **float** | The partial recoverable tax rate (Canada only) | [optional] 
**non_recoverable_ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


