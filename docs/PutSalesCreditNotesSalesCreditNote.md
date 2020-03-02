# PutSalesCreditNotesSalesCreditNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The contact the sales credit note relates to | [optional] 
**date** | **date** | The date of the credit note | [optional] 
**credit_note_number_prefix** | **str** | The credit note number prefix | [optional] 
**credit_note_number** | **str** | The generated credit note number | [optional] 
**contact_name** | **str** | The name of the contact when the credit note was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the credit note was created | [optional] 
**reference** | **str** | The reference for the credit note | [optional] 
**notes** | **str** | credit note notes | [optional] 
**terms_and_conditions** | **str** | Credit note terms and conditions | [optional] 
**shipping_net_amount** | **float** | The net shipping amount | [optional] 
**shipping_tax_rate_id** | **str** | The ID of the Shipping Tax Rate. | [optional] 
**shipping_tax_amount** | **float** | The tax shipping amount. NOTE: This is not required for POST/PUT requests as the shipping tax is calculated based on the shipping_net_amount and the shipping_tax_rate. | [optional] 
**total_quantity** | **float** | The total quantity of the credit note | [optional] 
**shipping_total_amount** | **float** | The total shipping amount | [optional] 
**net_amount** | **float** | The net amount of the credit note | [optional] 
**tax_amount** | **float** | The tax amount of the credit note | [optional] 
**total_amount** | **float** | The total amount of the credit note | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the credit note | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the credit note | [optional] 
**base_currency_shipping_net_amount** | **float** | The net shipping amount in base currency | [optional] 
**base_currency_shipping_tax_amount** | **float** | The tax shipping amount in base currency | [optional] 
**base_currency_shipping_total_amount** | **float** | The total shipping amount in base currency | [optional] 
**total_discount_amount** | **float** | The discount amount on the credit note | [optional] 
**base_currency_total_discount_amount** | **float** | The discount amount on the credit note in base currency | [optional] 
**base_currency_net_amount** | **float** | The net amount of the credit note in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the credit note in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the credit note in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**sent** | **bool** | Indicates whether the credit note has been sent | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**main_address** | [**PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress**](PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress.md) |  | [optional] 
**delivery_address** | [**PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress**](PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress.md) |  | [optional] 
**credit_note_lines** | [**list[PutSalesCreditNotesSalesCreditNoteCreditNoteLines]**](PutSalesCreditNotesSalesCreditNoteCreditNoteLines.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


