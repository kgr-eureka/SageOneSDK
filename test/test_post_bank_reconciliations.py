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
from openapi_client.models.post_bank_reconciliations import PostBankReconciliations  # noqa: E501
from openapi_client.rest import ApiException

class TestPostBankReconciliations(unittest.TestCase):
    """PostBankReconciliations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostBankReconciliations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.post_bank_reconciliations.PostBankReconciliations()  # noqa: E501
        if include_optional :
            return PostBankReconciliations(
                bank_reconciliation = openapi_client.models.post_bank_reconciliations_bank_reconciliation.postBankReconciliations_bank_reconciliation(
                    bank_account_id = '0', 
                    statement_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    statement_end_balance = 1.337, 
                    reference = '0', 
                    total_received = 1.337, 
                    total_paid = 1.337, 
                    starting_balance = 1.337, 
                    closing_balance = 1.337, 
                    reconciled_balance = 1.337, 
                    balance_difference = 1.337, )
            )
        else :
            return PostBankReconciliations(
        )

    def testPostBankReconciliations(self):
        """Test PostBankReconciliations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
