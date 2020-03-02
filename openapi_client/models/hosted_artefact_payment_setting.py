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


class HostedArtefactPaymentSetting(object):
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
        'legacy_id': 'int',
        'id': 'str',
        'displayed_as': 'str',
        'path': 'str',
        'object_guid': 'str',
        'disable_payment': 'bool'
    }

    attribute_map = {
        'legacy_id': 'legacy_id',
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'object_guid': 'object_guid',
        'disable_payment': 'disable_payment'
    }

    def __init__(self, legacy_id=None, id=None, displayed_as=None, path=None, object_guid=None, disable_payment=None, local_vars_configuration=None):  # noqa: E501
        """HostedArtefactPaymentSetting - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._legacy_id = None
        self._id = None
        self._displayed_as = None
        self._path = None
        self._object_guid = None
        self._disable_payment = None
        self.discriminator = None

        if legacy_id is not None:
            self.legacy_id = legacy_id
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if object_guid is not None:
            self.object_guid = object_guid
        if disable_payment is not None:
            self.disable_payment = disable_payment

    @property
    def legacy_id(self):
        """Gets the legacy_id of this HostedArtefactPaymentSetting.  # noqa: E501

        The legacy ID for the item  # noqa: E501

        :return: The legacy_id of this HostedArtefactPaymentSetting.  # noqa: E501
        :rtype: int
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """Sets the legacy_id of this HostedArtefactPaymentSetting.

        The legacy ID for the item  # noqa: E501

        :param legacy_id: The legacy_id of this HostedArtefactPaymentSetting.  # noqa: E501
        :type: int
        """

        self._legacy_id = legacy_id

    @property
    def id(self):
        """Gets the id of this HostedArtefactPaymentSetting.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this HostedArtefactPaymentSetting.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HostedArtefactPaymentSetting.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this HostedArtefactPaymentSetting.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this HostedArtefactPaymentSetting.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this HostedArtefactPaymentSetting.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this HostedArtefactPaymentSetting.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this HostedArtefactPaymentSetting.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this HostedArtefactPaymentSetting.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this HostedArtefactPaymentSetting.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this HostedArtefactPaymentSetting.

        The API path for the resource  # noqa: E501

        :param path: The path of this HostedArtefactPaymentSetting.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def object_guid(self):
        """Gets the object_guid of this HostedArtefactPaymentSetting.  # noqa: E501

        The sageone_guid of the object you are disabling card payments for.  # noqa: E501

        :return: The object_guid of this HostedArtefactPaymentSetting.  # noqa: E501
        :rtype: str
        """
        return self._object_guid

    @object_guid.setter
    def object_guid(self, object_guid):
        """Sets the object_guid of this HostedArtefactPaymentSetting.

        The sageone_guid of the object you are disabling card payments for.  # noqa: E501

        :param object_guid: The object_guid of this HostedArtefactPaymentSetting.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                object_guid is not None and len(object_guid) > 32):
            raise ValueError("Invalid value for `object_guid`, length must be less than or equal to `32`")  # noqa: E501

        self._object_guid = object_guid

    @property
    def disable_payment(self):
        """Gets the disable_payment of this HostedArtefactPaymentSetting.  # noqa: E501

        The flag to disable online payments.  # noqa: E501

        :return: The disable_payment of this HostedArtefactPaymentSetting.  # noqa: E501
        :rtype: bool
        """
        return self._disable_payment

    @disable_payment.setter
    def disable_payment(self, disable_payment):
        """Sets the disable_payment of this HostedArtefactPaymentSetting.

        The flag to disable online payments.  # noqa: E501

        :param disable_payment: The disable_payment of this HostedArtefactPaymentSetting.  # noqa: E501
        :type: bool
        """

        self._disable_payment = disable_payment

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
        if not isinstance(other, HostedArtefactPaymentSetting):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HostedArtefactPaymentSetting):
            return True

        return self.to_dict() != other.to_dict()