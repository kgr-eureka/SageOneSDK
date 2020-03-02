# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.bank_opening_balances_api import BankOpeningBalancesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestBankOpeningBalancesApi(unittest.TestCase):
    """BankOpeningBalancesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.bank_opening_balances_api.BankOpeningBalancesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_bank_opening_balances_key(self):
        """Test case for delete_bank_opening_balances_key

        Deletes a Bank Opening Balance  # noqa: E501
        """
        pass

    def test_get_bank_opening_balances(self):
        """Test case for get_bank_opening_balances

        Returns all Bank Opening Balances  # noqa: E501
        """
        pass

    def test_get_bank_opening_balances_key(self):
        """Test case for get_bank_opening_balances_key

        Returns a Bank Opening Balance  # noqa: E501
        """
        pass

    def test_post_bank_opening_balances(self):
        """Test case for post_bank_opening_balances

        Creates a Bank Opening Balance  # noqa: E501
        """
        pass

    def test_put_bank_opening_balances_key(self):
        """Test case for put_bank_opening_balances_key

        Updates a Bank Opening Balance  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
