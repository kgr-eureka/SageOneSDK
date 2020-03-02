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
from openapi_client.models.put_migrations_migrations import PutMigrationsMigrations  # noqa: E501
from openapi_client.rest import ApiException

class TestPutMigrationsMigrations(unittest.TestCase):
    """PutMigrationsMigrations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PutMigrationsMigrations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.put_migrations_migrations.PutMigrationsMigrations()  # noqa: E501
        if include_optional :
            return PutMigrationsMigrations(
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                source_product = '0', 
                source_product_version = '0', 
                source_license = '0', 
                source_tool = '0', 
                source_tool_version = '0', 
                schema_id = '0'
            )
        else :
            return PutMigrationsMigrations(
        )

    def testPutMigrationsMigrations(self):
        """Test PutMigrationsMigrations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
