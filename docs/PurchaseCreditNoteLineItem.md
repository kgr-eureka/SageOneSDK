# PurchaseCreditNoteLineItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_id** | **int** | The legacy ID for the item | [optional] 
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**is_purchase_for_resale** | **bool** | Identifies whether the line item is for resale. (Ireland Only) | [optional] 
**description** | **str** | The description for the credit note line | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**service** | [**Service**](Service.md) |  | [optional] 
**ledger_account** | [**Base**](Base.md) |  | [optional] 
**trade_of_asset** | **bool** | Whether the line item is marked as trade of asset. | [optional] 
**quantity** | **float** | The quantity for the credit note line | [optional] 
**unit_price** | **float** | The unit price for the credit note line | [optional] 
**net_amount** | **float** | The net amount for the credit note line | [optional] 
**tax_rate** | [**Base**](Base.md) |  | [optional] 
**tax_amount** | **float** | The tax amount for the credit note line\&quot;. This attribute is required in v3.1, unless the tax rate is of a \&quot;zero\&quot;, \&quot;exempt\&quot; or \&quot;no_tax\&quot; type. Then the tax_amount is infered as 0.0. In v3, this attribute is optional, but you should still set, as it defaults to 0.0 in any case. This is not what you want for tax rates with a percentage &gt; 0.0. | [optional] 
**tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the credit note line | [optional] 
**total_amount** | **float** | The total amount for the credit note line | [optional] 
**base_currency_unit_price** | **float** | The unit price for the credit note line in base currency | [optional] 
**unit_price_includes_tax** | **bool** | Defines whether the unit price includes tax | [optional] 
**base_currency_net_amount** | **float** | The net amount for the credit note line in base currency | [optional] 
**base_currency_tax_amount** | **float** | The tax amount for the credit note line in base currency | [optional] 
**base_currency_tax_breakdown** | [**list[TaxBreakdown]**](TaxBreakdown.md) | The tax breakdown for the credit note line in base currency | [optional] 
**base_currency_total_amount** | **float** | The total amount for the credit note line in base currency | [optional] 
**eu_goods_services_type** | [**Base**](Base.md) |  | [optional] 
**gst_amount** | **float** | The gst or hst tax amount for the credit note line | [optional] 
**pst_amount** | **float** | The pst or qst tax amount for the credit note line | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

