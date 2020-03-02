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


class PostPurchaseQuickEntries(object):
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
        'purchase_quick_entry': 'PostPurchaseQuickEntriesPurchaseQuickEntry'
    }

    attribute_map = {
        'purchase_quick_entry': 'purchase_quick_entry'
    }

    def __init__(self, purchase_quick_entry=None, local_vars_configuration=None):  # noqa: E501
        """PostPurchaseQuickEntries - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._purchase_quick_entry = None
        self.discriminator = None

        if purchase_quick_entry is not None:
            self.purchase_quick_entry = purchase_quick_entry

    @property
    def purchase_quick_entry(self):
        """Gets the purchase_quick_entry of this PostPurchaseQuickEntries.  # noqa: E501


        :return: The purchase_quick_entry of this PostPurchaseQuickEntries.  # noqa: E501
        :rtype: PostPurchaseQuickEntriesPurchaseQuickEntry
        """
        return self._purchase_quick_entry

    @purchase_quick_entry.setter
    def purchase_quick_entry(self, purchase_quick_entry):
        """Sets the purchase_quick_entry of this PostPurchaseQuickEntries.


        :param purchase_quick_entry: The purchase_quick_entry of this PostPurchaseQuickEntries.  # noqa: E501
        :type: PostPurchaseQuickEntriesPurchaseQuickEntry
        """

        self._purchase_quick_entry = purchase_quick_entry

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
        if not isinstance(other, PostPurchaseQuickEntries):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostPurchaseQuickEntries):
            return True

        return self.to_dict() != other.to_dict()
