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
from openapi_client.api.currencies_api import CurrenciesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestCurrenciesApi(unittest.TestCase):
    """CurrenciesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.currencies_api.CurrenciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_currencies(self):
        """Test case for get_currencies

        Returns all Currencies  # noqa: E501
        """
        pass

    def test_get_currencies_key(self):
        """Test case for get_currencies_key

        Returns a Currency  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
