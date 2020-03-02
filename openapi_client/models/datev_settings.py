# coding: utf-8

"""
    Sage Business Cloud Accounting - Accounts

    Documentation of the Sage Business Cloud Accounting API.  # noqa: E501

    The version of the OpenAPI document: 3.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class DatevSettings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'path': 'str',
        'tax_consultant_number': 'int',
        'client_number': 'int',
        'next_customer_number': 'int',
        'next_supplier_number': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'path': '$path',
        'tax_consultant_number': 'tax_consultant_number',
        'client_number': 'client_number',
        'next_customer_number': 'next_customer_number',
        'next_supplier_number': 'next_supplier_number',
        'updated_at': 'updated_at'
    }

    def __init__(self, path=None, tax_consultant_number=None, client_number=None, next_customer_number=None, next_supplier_number=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """DatevSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._tax_consultant_number = None
        self._client_number = None
        self._next_customer_number = None
        self._next_supplier_number = None
        self._updated_at = None
        self.discriminator = None

        if path is not None:
            self.path = path
        if tax_consultant_number is not None:
            self.tax_consultant_number = tax_consultant_number
        if client_number is not None:
            self.client_number = client_number
        if next_customer_number is not None:
            self.next_customer_number = next_customer_number
        if next_supplier_number is not None:
            self.next_supplier_number = next_supplier_number
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def path(self):
        """Gets the path of this DatevSettings.  # noqa: E501

        The api path for this item  # noqa: E501

        :return: The path of this DatevSettings.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this DatevSettings.

        The api path for this item  # noqa: E501

        :param path: The path of this DatevSettings.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def tax_consultant_number(self):
        """Gets the tax_consultant_number of this DatevSettings.  # noqa: E501

        Registration number of the Accountant  # noqa: E501

        :return: The tax_consultant_number of this DatevSettings.  # noqa: E501
        :rtype: int
        """
        return self._tax_consultant_number

    @tax_consultant_number.setter
    def tax_consultant_number(self, tax_consultant_number):
        """Sets the tax_consultant_number of this DatevSettings.

        Registration number of the Accountant  # noqa: E501

        :param tax_consultant_number: The tax_consultant_number of this DatevSettings.  # noqa: E501
        :type: int
        """

        self._tax_consultant_number = tax_consultant_number

    @property
    def client_number(self):
        """Gets the client_number of this DatevSettings.  # noqa: E501

        The users registration number  # noqa: E501

        :return: The client_number of this DatevSettings.  # noqa: E501
        :rtype: int
        """
        return self._client_number

    @client_number.setter
    def client_number(self, client_number):
        """Sets the client_number of this DatevSettings.

        The users registration number  # noqa: E501

        :param client_number: The client_number of this DatevSettings.  # noqa: E501
        :type: int
        """

        self._client_number = client_number

    @property
    def next_customer_number(self):
        """Gets the next_customer_number of this DatevSettings.  # noqa: E501

        The next unique customer number  # noqa: E501

        :return: The next_customer_number of this DatevSettings.  # noqa: E501
        :rtype: int
        """
        return self._next_customer_number

    @next_customer_number.setter
    def next_customer_number(self, next_customer_number):
        """Sets the next_customer_number of this DatevSettings.

        The next unique customer number  # noqa: E501

        :param next_customer_number: The next_customer_number of this DatevSettings.  # noqa: E501
        :type: int
        """

        self._next_customer_number = next_customer_number

    @property
    def next_supplier_number(self):
        """Gets the next_supplier_number of this DatevSettings.  # noqa: E501

        The next unique supplier number  # noqa: E501

        :return: The next_supplier_number of this DatevSettings.  # noqa: E501
        :rtype: int
        """
        return self._next_supplier_number

    @next_supplier_number.setter
    def next_supplier_number(self, next_supplier_number):
        """Sets the next_supplier_number of this DatevSettings.

        The next unique supplier number  # noqa: E501

        :param next_supplier_number: The next_supplier_number of this DatevSettings.  # noqa: E501
        :type: int
        """

        self._next_supplier_number = next_supplier_number

    @property
    def updated_at(self):
        """Gets the updated_at of this DatevSettings.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this DatevSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DatevSettings.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this DatevSettings.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DatevSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DatevSettings):
            return True

        return self.to_dict() != other.to_dict()
