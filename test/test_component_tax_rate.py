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
from openapi_client.models.component_tax_rate import ComponentTaxRate  # noqa: E501
from openapi_client.rest import ApiException

class TestComponentTaxRate(unittest.TestCase):
    """ComponentTaxRate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ComponentTaxRate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.component_tax_rate.ComponentTaxRate()  # noqa: E501
        if include_optional :
            return ComponentTaxRate(
                legacy_id = 56, 
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                name = '0', 
                agency = '0', 
                percentage = 1.337, 
                percentages = [
                    openapi_client.models.tax_rate_percentage.TaxRatePercentage(
                        percentage = 1.337, 
                        from_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        to_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), )
                    ], 
                is_visible = True, 
                retailer = True, 
                editable = True, 
                deletable = True, 
                is_combined_rate = True
            )
        else :
            return ComponentTaxRate(
        )

    def testComponentTaxRate(self):
        """Test ComponentTaxRate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
