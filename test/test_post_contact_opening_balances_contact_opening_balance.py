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
from openapi_client.models.post_contact_opening_balances_contact_opening_balance import PostContactOpeningBalancesContactOpeningBalance  # noqa: E501
from openapi_client.rest import ApiException

class TestPostContactOpeningBalancesContactOpeningBalance(unittest.TestCase):
    """PostContactOpeningBalancesContactOpeningBalance unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostContactOpeningBalancesContactOpeningBalance
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.post_contact_opening_balances_contact_opening_balance.PostContactOpeningBalancesContactOpeningBalance()  # noqa: E501
        if include_optional :
            return PostContactOpeningBalancesContactOpeningBalance(
                contact_opening_balance_type_id = '0', 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                contact_id = '0', 
                reference = '0', 
                total_amount = 1.337, 
                transaction_type_id = '0', 
                details = '0', 
                net_amount = 1.337, 
                tax_rate_id = '0', 
                tax_amount = 1.337, 
                currency_id = '0', 
                exchange_rate = 1.337, 
                base_currency_net_amount = 1.337, 
                base_currency_tax_amount = 1.337, 
                base_currency_total_amount = 1.337
            )
        else :
            return PostContactOpeningBalancesContactOpeningBalance(
                contact_opening_balance_type_id = '0',
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                contact_id = '0',
                reference = '0',
                total_amount = 1.337,
        )

    def testPostContactOpeningBalancesContactOpeningBalance(self):
        """Test PostContactOpeningBalancesContactOpeningBalance"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
