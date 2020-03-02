# JournalCode

Updates a Journal Code  ### Endpoint Availability  * Accounting: 🇫🇷 * Accounting Start: 🇫🇷  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Settings`: Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_id** | **int** | The legacy ID for the item | [optional] 
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**name** | **str** | The name of the journal code | [optional] 
**code** | **str** | The code of the journal code | [optional] 
**journal_code_type** | [**JournalCodeType**](JournalCodeType.md) |  | [optional] 
**control_name** | **str** | The control name of the journal code | [optional] 
**reserved** | **bool** | Indicates whether the journal code is reserved | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


