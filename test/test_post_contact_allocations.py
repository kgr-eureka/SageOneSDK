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
from openapi_client.models.post_contact_allocations import PostContactAllocations  # noqa: E501
from openapi_client.rest import ApiException

class TestPostContactAllocations(unittest.TestCase):
    """PostContactAllocations unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostContactAllocations
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.post_contact_allocations.PostContactAllocations()  # noqa: E501
        if include_optional :
            return PostContactAllocations(
                contact_allocation = openapi_client.models.post_contact_allocations_contact_allocation.postContactAllocations_contact_allocation(
                    transaction_type_id = '0', 
                    contact_id = '0', 
                    date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    allocated_artefacts = [
                        openapi_client.models.post_contact_allocations_contact_allocation_allocated_artefacts.postContactAllocations_contact_allocation_allocated_artefacts(
                            artefact_id = '0', 
                            amount = 1.337, )
                        ], )
            )
        else :
            return PostContactAllocations(
        )

    def testPostContactAllocations(self):
        """Test PostContactAllocations"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
