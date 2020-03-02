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
from openapi_client.api.sales_estimates_api import SalesEstimatesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestSalesEstimatesApi(unittest.TestCase):
    """SalesEstimatesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.sales_estimates_api.SalesEstimatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_sales_estimates_key(self):
        """Test case for delete_sales_estimates_key

        Deletes a Sales Estimate  # noqa: E501
        """
        pass

    def test_get_sales_estimates(self):
        """Test case for get_sales_estimates

        Returns all Sales Estimates  # noqa: E501
        """
        pass

    def test_get_sales_estimates_key(self):
        """Test case for get_sales_estimates_key

        Returns a Sales Estimate  # noqa: E501
        """
        pass

    def test_post_sales_estimates(self):
        """Test case for post_sales_estimates

        Creates a Sales Estimate  # noqa: E501
        """
        pass

    def test_put_sales_estimates_key(self):
        """Test case for put_sales_estimates_key

        Updates a Sales Estimate  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()