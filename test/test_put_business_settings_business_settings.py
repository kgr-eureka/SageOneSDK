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
from openapi_client.models.put_business_settings_business_settings import PutBusinessSettingsBusinessSettings  # noqa: E501
from openapi_client.rest import ApiException

class TestPutBusinessSettingsBusinessSettings(unittest.TestCase):
    """PutBusinessSettingsBusinessSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutBusinessSettingsBusinessSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.put_business_settings_business_settings.PutBusinessSettingsBusinessSettings()  # noqa: E501
        if include_optional :
            return PutBusinessSettingsBusinessSettings(
                siret = '0', 
                management_centre_member = True, 
                rcs_number = '0', 
                share_capital = 1.337, 
                business_activity_type_id = '0', 
                legal_form_type_id = '0', 
                auxiliary_accounts_visible = True, 
                business_type_id = '0', 
                country_of_registration_id = '0', 
                default_ledger_accounts = openapi_client.models.put_business_settings_business_settings_default_ledger_accounts.putBusinessSettings_business_settings_default_ledger_accounts(
                    bank_charges_ledger_account_id = '0', 
                    bank_interest_received_ledger_account_id = '0', 
                    bank_interest_charges_paid_ledger_account_id = '0', 
                    exchange_rate_gains_ledger_account_id = '0', 
                    exchange_rate_losses_ledger_account_id = '0', 
                    sales_ledger_account_id = '0', 
                    sales_discount_ledger_account_id = '0', 
                    purchase_ledger_account_id = '0', 
                    purchase_discount_ledger_account_id = '0', 
                    product_sales_ledger_account_id = '0', 
                    product_purchase_ledger_account_id = '0', 
                    service_sales_ledger_account_id = '0', 
                    service_purchase_ledger_account_id = '0', 
                    stock_purchase_ledger_account_id = '0', 
                    other_receipt_ledger_account_id = '0', 
                    other_payment_ledger_account_id = '0', 
                    customer_receipt_discount_ledger_account_id = '0', 
                    vendor_payment_discount_ledger_account_id = '0', 
                    carriage_ledger_account_id = '0', )
            )
        else :
            return PutBusinessSettingsBusinessSettings(
        )

    def testPutBusinessSettingsBusinessSettings(self):
        """Test PutBusinessSettingsBusinessSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
