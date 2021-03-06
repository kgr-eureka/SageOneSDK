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
from openapi_client.models.generic import Generic  # noqa: E501
from openapi_client.rest import ApiException

class TestGeneric(unittest.TestCase):
    """Generic unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Generic
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.generic.Generic()  # noqa: E501
        if include_optional :
            return Generic(
                legacy_id = 56, 
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                links = [
                    openapi_client.models.link.Link(
                        href = '0', 
                        rel = '0', 
                        type = '0', )
                    ]
            )
        else :
            return Generic(
        )

    def testGeneric(self):
        """Test Generic"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
