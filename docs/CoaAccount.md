# CoaAccount

Returns a Coa Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸
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
**name** | **str** | The name for the COA account | [optional] 
**control_name** | **str** | The system control name for the COA account | [optional] 
**nominal_code** | **int** | The nominal code of the COA account | [optional] 
**ledger_account_type** | [**Base**](Base.md) |  | [optional] 
**ledger_account_classification** | [**Base**](Base.md) |  | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**fixed_tax_rate** | **bool** | Indicates whether the default tax rate is fixed or may be changed | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


