# Address

Updates a Address  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access
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
**bank_account** | [**Base**](Base.md) |  | [optional] 
**contact** | [**Base**](Base.md) |  | [optional] 
**address_type** | [**Base**](Base.md) |  | [optional] 
**name** | **str** | The name of the address | [optional] 
**address_line_1** | **str** | The first line of the address | [optional] 
**address_line_2** | **str** | The second line of the address | [optional] 
**city** | **str** | The address town/city | [optional] 
**region** | **str** | The address state/province/region | [optional] 
**postal_code** | **str** | The address postal code/zipcode | [optional] 
**country** | [**Base**](Base.md) |  | [optional] 
**country_group** | [**Base**](Base.md) |  | [optional] 
**is_main_address** | **bool** | Indicates whether this is a main address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


