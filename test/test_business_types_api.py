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
from openapi_client.api.business_types_api import BusinessTypesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestBusinessTypesApi(unittest.TestCase):
    """BusinessTypesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.business_types_api.BusinessTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_types(self):
        """Test case for get_business_types

        Returns all Business Types  # noqa: E501
        """
        pass

    def test_get_business_types_key(self):
        """Test case for get_business_types_key

        Returns a Business Type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()