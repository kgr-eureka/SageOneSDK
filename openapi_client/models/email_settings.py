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


class EmailSettings(object):
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
        'default_messages': 'list[DefaultMessages]',
        'pdf_attached': 'bool',
        'send_bcc': 'bool',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'default_messages': 'default_messages',
        'pdf_attached': 'pdf_attached',
        'send_bcc': 'send_bcc',
        'updated_at': 'updated_at'
    }

    def __init__(self, default_messages=None, pdf_attached=None, send_bcc=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """EmailSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._default_messages = None
        self._pdf_attached = None
        self._send_bcc = None
        self._updated_at = None
        self.discriminator = None

        if default_messages is not None:
            self.default_messages = default_messages
        if pdf_attached is not None:
            self.pdf_attached = pdf_attached
        if send_bcc is not None:
            self.send_bcc = send_bcc
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def default_messages(self):
        """Gets the default_messages of this EmailSettings.  # noqa: E501

        The default email messages for the businesses per message type and locale.  # noqa: E501

        :return: The default_messages of this EmailSettings.  # noqa: E501
        :rtype: list[DefaultMessages]
        """
        return self._default_messages

    @default_messages.setter
    def default_messages(self, default_messages):
        """Sets the default_messages of this EmailSettings.

        The default email messages for the businesses per message type and locale.  # noqa: E501

        :param default_messages: The default_messages of this EmailSettings.  # noqa: E501
        :type: list[DefaultMessages]
        """

        self._default_messages = default_messages

    @property
    def pdf_attached(self):
        """Gets the pdf_attached of this EmailSettings.  # noqa: E501

        Indicates whether PDFs are always attached as part of sending emails for a business  # noqa: E501

        :return: The pdf_attached of this EmailSettings.  # noqa: E501
        :rtype: bool
        """
        return self._pdf_attached

    @pdf_attached.setter
    def pdf_attached(self, pdf_attached):
        """Sets the pdf_attached of this EmailSettings.

        Indicates whether PDFs are always attached as part of sending emails for a business  # noqa: E501

        :param pdf_attached: The pdf_attached of this EmailSettings.  # noqa: E501
        :type: bool
        """

        self._pdf_attached = pdf_attached

    @property
    def send_bcc(self):
        """Gets the send_bcc of this EmailSettings.  # noqa: E501

        Indicates whether the user should always be sent a copy when sending a document via email  # noqa: E501

        :return: The send_bcc of this EmailSettings.  # noqa: E501
        :rtype: bool
        """
        return self._send_bcc

    @send_bcc.setter
    def send_bcc(self, send_bcc):
        """Sets the send_bcc of this EmailSettings.

        Indicates whether the user should always be sent a copy when sending a document via email  # noqa: E501

        :param send_bcc: The send_bcc of this EmailSettings.  # noqa: E501
        :type: bool
        """

        self._send_bcc = send_bcc

    @property
    def updated_at(self):
        """Gets the updated_at of this EmailSettings.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this EmailSettings.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EmailSettings.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this EmailSettings.  # noqa: E501
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
        if not isinstance(other, EmailSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmailSettings):
            return True

        return self.to_dict() != other.to_dict()
