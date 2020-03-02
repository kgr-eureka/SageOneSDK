# PostContactsContact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the contact | 
**contact_type_ids** | **list[str]** | The IDs of the Contact Types. | 
**reference** | **str** | The reference for the contact | [optional] 
**default_sales_ledger_account_id** | **str** | The ID of the Default Sales Ledger Account. | [optional] 
**default_sales_tax_rate_id** | **str** | The ID of the Default Sales Tax Rate. | [optional] 
**default_purchase_ledger_account_id** | **str** | The ID of the Default Purchase Ledger Account. | [optional] 
**tax_number** | **str** | The tax number for the contact | [optional] 
**notes** | **str** | The notes for the contact | [optional] 
**locale** | **str** | The locale for the contact | [optional] 
**credit_limit** | **float** | Custom credit limit amount for the contact | [optional] 
**credit_days** | **int** | Custom credit days for the contact If returned as null in a GET response, you may want to GET /invoice_settings and use &#39;vendor_credit_days&#39; as default/fallback according to your use case.  | [optional] 
**credit_terms_and_conditions** | **str** | Custom terms and conditions for the contact (Customers only) | [optional] 
**product_sales_price_type_id** | **str** | The ID of the Product Sales Price Type. | [optional] 
**source_guid** | **str** | Used when importing contacts from external sources | [optional] 
**currency_id** | **str** | The ID of the Currency. | [optional] 
**aux_reference** | **str** | Auxiliary reference. Used for German \&quot;Kreditorennummer\&quot; and \&quot;Debitorennummer\&quot; | [optional] 
**registered_number** | **str** | The registered number of the contact&#39;s business. Only used for German businesses and represents the \&quot;Steuernummer\&quot; there (not the \&quot;USt-ID\&quot;). | [optional] 
**email** | **str** | The email address for the given contact | [optional] 
**tax_calculation** | **str** | The tax calculation method - used for French VAT &amp; Recargo | [optional] 
**auxiliary_account** | **str** | Auxiliary account - used when auxiliary accounting is enabled in business settings | [optional] 
**main_address** | [**PostBankAccountsBankAccountMainAddress**](PostBankAccountsBankAccountMainAddress.md) |  | [optional] 
**delivery_address** | [**PostBankAccountsBankAccountMainAddress**](PostBankAccountsBankAccountMainAddress.md) |  | [optional] 
**main_contact_person** | [**PostContactsContactMainContactPerson**](PostContactsContactMainContactPerson.md) |  | [optional] 
**bank_account_details** | [**PutBankAccountsBankAccountBankAccountDetails**](PutBankAccountsBankAccountBankAccountDetails.md) |  | [optional] 
**tax_treatment** | [**PostContactsContactTaxTreatment**](PostContactsContactTaxTreatment.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


