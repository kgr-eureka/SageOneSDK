# PostLedgerAccountsLedgerAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ledger_account_type_id** | **str** | The ledger account type for the ledger account | 
**included_in_chart** | **bool** | Indicates whether the ledger account is included in the chart of accounts | 
**name** | **str** | The name for the ledger account. Changes to this field do not propagate to other resources, namely not to the name of the associated bank_account (unlike the behaviour of the UI). | 
**display_name** | **str** | The display name for the ledger account | 
**nominal_code** | **int** | The nominal code of the ledger account | 
**ledger_account_classification_id** | **str** | The ID of the Ledger Account Classification. | [optional] 
**tax_rate_id** | **str** | The ID of the Tax Rate. | [optional] 
**fixed_tax_rate** | **bool** | Indicates whether the default tax rate is fixed or may be changed | [optional] 
**visible_in_banking** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_expenses** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_journals** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_other_payments** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_other_receipts** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_reporting** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**visible_in_sales** | **bool** | Indicates whether the ledger account is displayed in this area of the application | [optional] 
**is_control_account** | **bool** | Indicates whether the ledger account is a control account | [optional] 
**control_name** | **str** | The control name for the ledger account | [optional] 
**tax_recoverable** | **bool** | Indicates that transactions posted to this ledger account have part recoverable taxes (Canada only) | [optional] 
**recoverable_percentage** | **float** | The partial recoverable tax rate (Canada only) | [optional] 
**non_recoverable_ledger_account_id** | **str** | The ID of the Non Recoverable Ledger Account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


