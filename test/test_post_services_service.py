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
from openapi_client.models.post_services_service import PostServicesService  # noqa: E501
from openapi_client.rest import ApiException

class TestPostServicesService(unittest.TestCase):
    """PostServicesService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostServicesService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.post_services_service.PostServicesService()  # noqa: E501
        if include_optional :
            return PostServicesService(
                description = '0', 
                sales_ledger_account_id = '0', 
                item_code = '0', 
                notes = '0', 
                purchase_ledger_account_id = '0', 
                sales_tax_rate_id = '0', 
                purchase_tax_rate_id = '0', 
                source_guid = '0', 
                purchase_description = '0', 
                usual_supplier_id = '0', 
                active = True, 
                sales_rates = [
                    openapi_client.models.post_services_service_sales_rates.postServices_service_sales_rates(
                        rate_name = '0', 
                        rate = 1.337, 
                        rate_includes_tax = True, 
                        service_rate_type_id = '0', )
                    ]
            )
        else :
            return PostServicesService(
                description = '0',
                sales_ledger_account_id = '0',
        )

    def testPostServicesService(self):
        """Test PostServicesService"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
