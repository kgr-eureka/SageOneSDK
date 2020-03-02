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
from openapi_client.models.put_stock_movements_stock_movement import PutStockMovementsStockMovement  # noqa: E501
from openapi_client.rest import ApiException

class TestPutStockMovementsStockMovement(unittest.TestCase):
    """PutStockMovementsStockMovement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutStockMovementsStockMovement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.put_stock_movements_stock_movement.PutStockMovementsStockMovement()  # noqa: E501
        if include_optional :
            return PutStockMovementsStockMovement(
                stock_item_id = '0', 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                quantity = 1.337, 
                cost_price = 1.337, 
                details = '0', 
                movement_number = '0', 
                reference = '0'
            )
        else :
            return PutStockMovementsStockMovement(
        )

    def testPutStockMovementsStockMovement(self):
        """Test PutStockMovementsStockMovement"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
