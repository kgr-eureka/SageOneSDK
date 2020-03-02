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


class PutInvoiceSettingsInvoiceSettingsFooterDetails(object):
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
        'column_1': 'str',
        'column_2': 'str',
        'column_3': 'str'
    }

    attribute_map = {
        'column_1': 'column_1',
        'column_2': 'column_2',
        'column_3': 'column_3'
    }

    def __init__(self, column_1=None, column_2=None, column_3=None, local_vars_configuration=None):  # noqa: E501
        """PutInvoiceSettingsInvoiceSettingsFooterDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._column_1 = None
        self._column_2 = None
        self._column_3 = None
        self.discriminator = None

        if column_1 is not None:
            self.column_1 = column_1
        if column_2 is not None:
            self.column_2 = column_2
        if column_3 is not None:
            self.column_3 = column_3

    @property
    def column_1(self):
        """Gets the column_1 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501

        The pdf footer details for column 1  # noqa: E501

        :return: The column_1 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501
        :rtype: str
        """
        return self._column_1

    @column_1.setter
    def column_1(self, column_1):
        """Sets the column_1 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.

        The pdf footer details for column 1  # noqa: E501

        :param column_1: The column_1 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501
        :type: str
        """

        self._column_1 = column_1

    @property
    def column_2(self):
        """Gets the column_2 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501

        The pdf footer details for column 2  # noqa: E501

        :return: The column_2 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501
        :rtype: str
        """
        return self._column_2

    @column_2.setter
    def column_2(self, column_2):
        """Sets the column_2 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.

        The pdf footer details for column 2  # noqa: E501

        :param column_2: The column_2 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501
        :type: str
        """

        self._column_2 = column_2

    @property
    def column_3(self):
        """Gets the column_3 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501

        The pdf footer details for column 3  # noqa: E501

        :return: The column_3 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501
        :rtype: str
        """
        return self._column_3

    @column_3.setter
    def column_3(self, column_3):
        """Sets the column_3 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.

        The pdf footer details for column 3  # noqa: E501

        :param column_3: The column_3 of this PutInvoiceSettingsInvoiceSettingsFooterDetails.  # noqa: E501
        :type: str
        """

        self._column_3 = column_3

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
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsFooterDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutInvoiceSettingsInvoiceSettingsFooterDetails):
            return True

        return self.to_dict() != other.to_dict()
