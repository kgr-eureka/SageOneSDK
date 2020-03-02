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
from openapi_client.models.put_service_rate_types_service_rate_type import PutServiceRateTypesServiceRateType  # noqa: E501
from openapi_client.rest import ApiException

class TestPutServiceRateTypesServiceRateType(unittest.TestCase):
    """PutServiceRateTypesServiceRateType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutServiceRateTypesServiceRateType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.put_service_rate_types_service_rate_type.PutServiceRateTypesServiceRateType()  # noqa: E501
        if include_optional :
            return PutServiceRateTypesServiceRateType(
                name = '0', 
                active = True
            )
        else :
            return PutServiceRateTypesServiceRateType(
        )

    def testPutServiceRateTypesServiceRateType(self):
        """Test PutServiceRateTypesServiceRateType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
