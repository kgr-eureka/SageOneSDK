# PutPurchaseInvoicesPurchaseInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The contact the purchase invoice relates to | [optional] 
**date** | **date** | The date of the invoice | [optional] 
**due_date** | **date** | The due date of the invoice | [optional] 
**postponed_accounting** | **bool** | Indicates whether postponed accounting rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer | [optional] 
**_import** | **bool** | Indicates whether import rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer. | [optional] 
**contact_name** | **str** | The name of the contact when the invoice was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the invoice was created | [optional] 
**reference** | **str** | The reference for the invoice | [optional] 
**vendor_reference** | **str** | The vendor reference for the invoice | [optional] 
**notes** | **str** | Invoice notes | [optional] 
**total_quantity** | **float** | The total quantity of the invoice | [optional] 
**net_amount** | **float** | The net amount of the invoice | [optional] 
**tax_amount** | **float** | The tax amount of the invoice | [optional] 
**total_amount** | **float** | The total amount of the invoice | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the invoice | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the invoice | [optional] 
**base_currency_net_amount** | **float** | The net amount of the invoice in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the invoice in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the invoice in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**withholding_tax_rate** | **float** | IRPF withheld Tax Rate (Spain only) | [optional] 
**withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) | [optional] 
**base_currency_withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) in the base currency | [optional] 
**invoice_lines** | [**list[PutPurchaseInvoicesPurchaseInvoiceInvoiceLines]**](PutPurchaseInvoicesPurchaseInvoiceInvoiceLines.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


