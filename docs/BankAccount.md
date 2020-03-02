# BankAccount

Updates a Bank Account  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any of the following roles in the area `Bank`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_id** | **int** | The legacy ID for the item | [optional] 
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**bank_account_details** | [**BankAccountDetails**](BankAccountDetails.md) |  | [optional] 
**ledger_account** | [**Base**](Base.md) |  | [optional] 
**bank_account_type** | [**Base**](Base.md) |  | [optional] 
**balance** | **float** | The bank account balance | [optional] 
**main_address** | [**Address**](Address.md) |  | [optional] 
**main_contact_person** | [**BankAccountContact**](BankAccountContact.md) |  | [optional] 
**nominal_code** | **int** | The nominal code of the bank account | [optional] 
**editable** | **bool** | Indicates whether or not the bank account can be edited | [optional] 
**deletable** | **bool** | Indicates whether or not the bank account can be deleted | [optional] 
**journal_code** | [**JournalCode**](JournalCode.md) |  | [optional] 
**default_payment_method** | [**Base**](Base.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


