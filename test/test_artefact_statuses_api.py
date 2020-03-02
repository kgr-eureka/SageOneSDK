# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.artefact_statuses_api import ArtefactStatusesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestArtefactStatusesApi(unittest.TestCase):
    """ArtefactStatusesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.artefact_statuses_api.ArtefactStatusesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_artefact_statuses(self):
        """Test case for get_artefact_statuses

        Returns all Artefact Statuses  # noqa: E501
        """
        pass

    def test_get_artefact_statuses_key(self):
        """Test case for get_artefact_statuses_key

        Returns a Artefact Status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
