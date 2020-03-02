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
from openapi_client.api.quick_entry_types_api import QuickEntryTypesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestQuickEntryTypesApi(unittest.TestCase):
    """QuickEntryTypesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.quick_entry_types_api.QuickEntryTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_quick_entry_types(self):
        """Test case for get_quick_entry_types

        Returns all Quick Entry Types  # noqa: E501
        """
        pass

    def test_get_quick_entry_types_key(self):
        """Test case for get_quick_entry_types_key

        Returns a Quick Entry Type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()