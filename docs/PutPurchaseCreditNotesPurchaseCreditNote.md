# PutPurchaseCreditNotesPurchaseCreditNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The contact the purchase credit note relates to | [optional] 
**date** | **date** | The date of the credit note | [optional] 
**postponed_accounting** | **bool** | Indicates whether postponed accounting rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer | [optional] 
**_import** | **bool** | Indicates whether import rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer. | [optional] 
**contact_name** | **str** | The name of the contact when the credit note was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the credit note was created | [optional] 
**reference** | **str** | The reference for the credit note | [optional] 
**vendor_reference** | **str** | The vendor reference for the credit note | [optional] 
**notes** | **str** | credit note notes | [optional] 
**total_quantity** | **float** | The total quantity of the credit note | [optional] 
**net_amount** | **float** | The net amount of the credit note | [optional] 
**tax_amount** | **float** | The tax amount of the credit note | [optional] 
**total_amount** | **float** | The total amount of the credit note | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the credit note | [optional] 
**inverse_exchange_rate** | **str** | The inverse exchange rate for the credit note | [optional] 
**base_currency_net_amount** | **float** | The net amount of the credit note in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the credit note in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the credit note in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**credit_note_lines** | [**list[PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines]**](PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


