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
from openapi_client.models.datev_settings import DatevSettings  # noqa: E501
from openapi_client.rest import ApiException

class TestDatevSettings(unittest.TestCase):
    """DatevSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DatevSettings
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.datev_settings.DatevSettings()  # noqa: E501
        if include_optional :
            return DatevSettings(
                path = '0', 
                tax_consultant_number = 56, 
                client_number = 56, 
                next_customer_number = 56, 
                next_supplier_number = 56, 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return DatevSettings(
        )

    def testDatevSettings(self):
        """Test DatevSettings"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()