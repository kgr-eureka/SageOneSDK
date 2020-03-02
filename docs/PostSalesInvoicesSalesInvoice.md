# PostSalesInvoicesSalesInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** | The contact the sales invoice relates to | 
**date** | **date** | The date of the invoice | 
**invoice_number_prefix** | **str** | The invoice number prefix | [optional] 
**invoice_number** | **str** | The generated invoice number | [optional] 
**contact_name** | **str** | The name of the contact when the invoice was created | [optional] 
**contact_reference** | **str** | The reference of the contact when the invoice was created | [optional] 
**due_date** | **date** | The due date of the invoice | [optional] 
**reference** | **str** | The reference for the invoice | [optional] 
**notes** | **str** | Invoice notes | [optional] 
**terms_and_conditions** | **str** | Invoice terms and conditions | [optional] 
**shipping_net_amount** | **float** | The net shipping amount | [optional] 
**shipping_tax_rate_id** | **str** | The ID of the Shipping Tax Rate. | [optional] 
**shipping_tax_amount** | **float** | The tax shipping amount. NOTE: This is not required for POST/PUT requests as the shipping tax is calculated based on the shipping_net_amount and the shipping_tax_rate. | [optional] 
**shipping_total_amount** | **float** | The total shipping amount | [optional] 
**net_amount** | **float** | The net amount of the invoice | [optional] 
**tax_amount** | **float** | The tax amount of the invoice | [optional] 
**total_amount** | **float** | The total amount of the invoice | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**exchange_rate** | **float** | The exchange rate for the invoice | [optional] 
**inverse_exchange_rate** | **float** | The inverse exchange rate for the invoice | [optional] 
**base_currency_shipping_net_amount** | **float** | The net shipping amount in base currency | [optional] 
**base_currency_shipping_tax_amount** | **float** | The tax shipping amount in base currency | [optional] 
**base_currency_shipping_total_amount** | **float** | The total shipping amount in base currency | [optional] 
**total_quantity** | **float** | The total quantity of the invoice | [optional] 
**total_discount_amount** | **float** | The discount amount on the invoice | [optional] 
**base_currency_total_discount_amount** | **float** | The discount amount on the invoice in base currency | [optional] 
**base_currency_net_amount** | **float** | The net amount of the invoice in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount of the invoice in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount of the invoice in base currency | [optional] 
**status_id** | **str** | The ID of the Status. | [optional] 
**sent** | **bool** | Indicates whether the invoice has been sent | [optional] 
**tax_address_region_id** | **str** | The ID of the Tax Address Region. (Canada only) | [optional] 
**delivery_performance_date** | **str** | Delivery/Performance Date (Germany only) | [optional] 
**withholding_tax_rate** | **float** | IRPF withheld Tax Rate (Spain only) | [optional] 
**withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) | [optional] 
**base_currency_withholding_tax_amount** | **float** | IRPF withheld Tax Amount (Spain only) in the base currency | [optional] 
**invoice_lines** | [**list[PostSalesCreditNotesSalesCreditNoteCreditNoteLines]**](PostSalesCreditNotesSalesCreditNoteCreditNoteLines.md) |  | 
**main_address** | [**PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress**](PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress.md) |  | [optional] 
**delivery_address** | [**PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress**](PostSalesCorrectiveInvoicesSalesCorrectiveInvoiceMainAddress.md) |  | [optional] 
**tax_analysis** | [**list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]**](PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


