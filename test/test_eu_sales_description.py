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
from openapi_client.models.eu_sales_description import EuSalesDescription  # noqa: E501
from openapi_client.rest import ApiException

class TestEuSalesDescription(unittest.TestCase):
    """EuSalesDescription unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EuSalesDescription
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.eu_sales_description.EuSalesDescription()  # noqa: E501
        if include_optional :
            return EuSalesDescription(
                legacy_id = 56, 
                id = '0', 
                displayed_as = '0', 
                path = '0'
            )
        else :
            return EuSalesDescription(
        )

    def testEuSalesDescription(self):
        """Test EuSalesDescription"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
