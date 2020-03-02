# Contact

Updates a Contact  ### Endpoint Availability  * Accounting: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸 * Accounting Start: 🇨🇦, 🇩🇪, 🇪🇸, 🇫🇷, 🇬🇧, 🇮🇪, 🇺🇸  ### Access Control Restrictions  Requires the authenticated user to have any mentioned role in one of the listed areas: * Area: `Contacts`: Restricted Access, Full Access
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_id** | **int** | The legacy ID for the item | [optional] 
**id** | **str** | The unique identifier for the item | [optional] 
**displayed_as** | **str** | The name of the resource | [optional] 
**path** | **str** | The API path for the resource | [optional] 
**created_at** | **datetime** | The datetime when the item was created | [optional] 
**updated_at** | **datetime** | The datetime when the item was last updated | [optional] 
**links** | [**list[Link]**](Link.md) | Links for the resource | [optional] 
**deleted_at** | **datetime** | The datetime when the item was deleted | [optional] 
**balance** | **float** | The contact balance | [optional] 
**contact_types** | [**list[Base]**](Base.md) | The contact types for the contact | [optional] 
**name** | **str** | The name of the contact | [optional] 
**reference** | **str** | The reference for the contact | [optional] 
**default_sales_ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**default_sales_tax_rate** | [**Base**](Base.md) |  | [optional] 
**default_purchase_ledger_account** | [**LedgerAccount**](LedgerAccount.md) |  | [optional] 
**tax_number** | **str** | The tax number for the contact | [optional] 
**notes** | **str** | The notes for the contact | [optional] 
**locale** | **str** | The locale for the contact | [optional] 
**main_address** | [**Address**](Address.md) |  | [optional] 
**delivery_address** | [**Address**](Address.md) |  | [optional] 
**main_contact_person** | [**ContactPerson**](ContactPerson.md) |  | [optional] 
**bank_account_details** | [**BankAccountDetails**](BankAccountDetails.md) |  | [optional] 
**credit_limit** | **float** | Custom credit limit amount for the contact | [optional] 
**credit_days** | **int** | Custom credit days for the contact If returned as null in a GET response, you may want to GET /invoice_settings and use &#39;vendor_credit_days&#39; as default/fallback according to your use case.  | [optional] 
**credit_terms_and_conditions** | **str** | Custom terms and conditions for the contact (Customers only) | [optional] 
**product_sales_price_type** | [**Base**](Base.md) |  | [optional] 
**source_guid** | **str** | Used when importing contacts from external sources | [optional] 
**currency** | [**Base**](Base.md) |  | [optional] 
**aux_reference** | **str** | Auxiliary reference. Used for German \&quot;Kreditorennummer\&quot; and \&quot;Debitorennummer\&quot; | [optional] 
**registered_number** | **str** | The registered number of the contact&#39;s business. Only used for German businesses and represents the \&quot;Steuernummer\&quot; there (not the \&quot;USt-ID\&quot;). | [optional] 
**deletable** | **bool** | Indicates whether the ledger entry has been deleted or not | [optional] 
**tax_treatment** | [**ContactTaxTreatment**](ContactTaxTreatment.md) |  | [optional] 
**email** | **str** | The email address for the given contact | [optional] 
**tax_calculation** | **str** | The tax calculation method - used for French VAT &amp; Recargo | [optional] 
**auxiliary_account** | **str** | Auxiliary account - used when auxiliary accounting is enabled in business settings | [optional] 
**gdpr_obfuscated** | **bool** | General Data Protection Regulation (GDPR) came into effect on 25th May 2018. It introduces new rules for how business owners manage their contacts&#39; personal data. When this field returns &#39;true&#39;, means that the contact has been requested to be obfuscated and you can not create any artifact (sales invoices, purchase invoices, ...) but you can still check previously created artifacts. | [optional] 
**system** | **bool** | Identifies a contact as being a system contact used for processing specific transaction types and reserved specifically for those transaction types such as tax return payments/refunds. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


