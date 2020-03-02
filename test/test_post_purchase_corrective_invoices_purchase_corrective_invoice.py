# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.post_purchase_corrective_invoices_purchase_corrective_invoice import PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice  # noqa: E501
from openapi_client.rest import ApiException

class TestPostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice(unittest.TestCase):
    """PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.post_purchase_corrective_invoices_purchase_corrective_invoice.PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice()  # noqa: E501
        if include_optional :
            return PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice(
                postponed_accounting = True, 
                contact_id = '0', 
                contact_name = '0', 
                contact_reference = '0', 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                due_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                reference = '0', 
                vendor_reference = '0', 
                notes = '0', 
                total_quantity = 1.337, 
                net_amount = 1.337, 
                tax_amount = 1.337, 
                total_amount = 1.337, 
                currency_id = '0', 
                exchange_rate = 1.337, 
                inverse_exchange_rate = '0', 
                base_currency_net_amount = 1.337, 
                base_currency_tax_amount = 1.337, 
                base_currency_total_amount = 1.337, 
                status_id = '0', 
                withholding_tax_rate = 1.337, 
                withholding_tax_amount = 1.337, 
                base_currency_withholding_tax_amount = 1.337, 
                original_invoice_number = '0', 
                original_invoice_date = '0', 
                invoice_lines = [
                    openapi_client.models.post_purchase_corrective_invoices_purchase_corrective_invoice_invoice_lines.postPurchaseCorrectiveInvoices_purchase_corrective_invoice_invoice_lines(
                        is_purchase_for_resale = True, 
                        description = '0', 
                        product_id = '0', 
                        service_id = '0', 
                        ledger_account_id = '0', 
                        trade_of_asset = True, 
                        quantity = 1.337, 
                        unit_price = 1.337, 
                        net_amount = 1.337, 
                        tax_rate_id = '0', 
                        tax_amount = 1.337, 
                        total_amount = 1.337, 
                        base_currency_unit_price = 1.337, 
                        unit_price_includes_tax = True, 
                        base_currency_net_amount = 1.337, 
                        base_currency_tax_amount = 1.337, 
                        base_currency_total_amount = 1.337, 
                        eu_goods_services_type_id = '0', 
                        gst_amount = 1.337, 
                        pst_amount = 1.337, )
                    ], 
                tax_analysis = [
                    openapi_client.models.post_purchase_corrective_invoices_purchase_corrective_invoice_tax_analysis.postPurchaseCorrectiveInvoices_purchase_corrective_invoice_tax_analysis(
                        tax_rate_id = '0', 
                        net_amount = 1.337, 
                        tax_amount = 1.337, 
                        total_amount = 1.337, 
                        goods_amount = 1.337, 
                        service_amount = 1.337, )
                    ]
            )
        else :
            return PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice(
        )

    def testPostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice(self):
        """Test PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoice"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
