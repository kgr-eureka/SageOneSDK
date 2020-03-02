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
from openapi_client.models.attachment import Attachment  # noqa: E501
from openapi_client.rest import ApiException

class TestAttachment(unittest.TestCase):
    """Attachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Attachment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.attachment.Attachment()  # noqa: E501
        if include_optional :
            return Attachment(
                id = '0', 
                displayed_as = '0', 
                path = '0', 
                deleted_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                file = '0', 
                mime_type = '0', 
                description = '0', 
                file_extension = '0', 
                transaction = openapi_client.models.base.Base(
                    legacy_id = 56, 
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                file_size = 56, 
                file_name = '0', 
                file_path = '0', 
                attachment_context_type = openapi_client.models.base.Base(
                    legacy_id = 56, 
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                attachment_context = openapi_client.models.base.Base(
                    legacy_id = 56, 
                    id = '0', 
                    displayed_as = '0', 
                    __path = '0', ), 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else :
            return Attachment(
        )

    def testAttachment(self):
        """Test Attachment"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
