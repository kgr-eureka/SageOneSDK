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
from openapi_client.models.post_bank_accounts_bank_account_main_contact_person import PostBankAccountsBankAccountMainContactPerson  # noqa: E501
from openapi_client.rest import ApiException

class TestPostBankAccountsBankAccountMainContactPerson(unittest.TestCase):
    """PostBankAccountsBankAccountMainContactPerson unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostBankAccountsBankAccountMainContactPerson
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.post_bank_accounts_bank_account_main_contact_person.PostBankAccountsBankAccountMainContactPerson()  # noqa: E501
        if include_optional :
            return PostBankAccountsBankAccountMainContactPerson(
                name = '0', 
                job_title = '0', 
                telephone = '0', 
                mobile = '0', 
                email = '0', 
                fax = '0'
            )
        else :
            return PostBankAccountsBankAccountMainContactPerson(
        )

    def testPostBankAccountsBankAccountMainContactPerson(self):
        """Test PostBankAccountsBankAccountMainContactPerson"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
