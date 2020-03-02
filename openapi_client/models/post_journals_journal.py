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


class PostJournalsJournal(object):
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
        'date': 'date',
        'reference': 'str',
        'description': 'str',
        'total': 'float',
        'journal_lines': 'list[PostJournalsJournalJournalLines]',
        'journal_code': 'PostJournalsJournalJournalCode'
    }

    attribute_map = {
        'date': 'date',
        'reference': 'reference',
        'description': 'description',
        'total': 'total',
        'journal_lines': 'journal_lines',
        'journal_code': 'journal_code'
    }

    def __init__(self, date=None, reference=None, description=None, total=None, journal_lines=None, journal_code=None, local_vars_configuration=None):  # noqa: E501
        """PostJournalsJournal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._date = None
        self._reference = None
        self._description = None
        self._total = None
        self._journal_lines = None
        self._journal_code = None
        self.discriminator = None

        self.date = date
        self.reference = reference
        if description is not None:
            self.description = description
        if total is not None:
            self.total = total
        self.journal_lines = journal_lines
        if journal_code is not None:
            self.journal_code = journal_code

    @property
    def date(self):
        """Gets the date of this PostJournalsJournal.  # noqa: E501

        The date of the journal  # noqa: E501

        :return: The date of this PostJournalsJournal.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PostJournalsJournal.

        The date of the journal  # noqa: E501

        :param date: The date of this PostJournalsJournal.  # noqa: E501
        :type: date
        """
        if self.local_vars_configuration.client_side_validation and date is None:  # noqa: E501
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def reference(self):
        """Gets the reference of this PostJournalsJournal.  # noqa: E501

        A reference for the journal  # noqa: E501

        :return: The reference of this PostJournalsJournal.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PostJournalsJournal.

        A reference for the journal  # noqa: E501

        :param reference: The reference of this PostJournalsJournal.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reference is None:  # noqa: E501
            raise ValueError("Invalid value for `reference`, must not be `None`")  # noqa: E501

        self._reference = reference

    @property
    def description(self):
        """Gets the description of this PostJournalsJournal.  # noqa: E501

        A description of the journal  # noqa: E501

        :return: The description of this PostJournalsJournal.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostJournalsJournal.

        A description of the journal  # noqa: E501

        :param description: The description of this PostJournalsJournal.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def total(self):
        """Gets the total of this PostJournalsJournal.  # noqa: E501

        The total for the journal  # noqa: E501

        :return: The total of this PostJournalsJournal.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PostJournalsJournal.

        The total for the journal  # noqa: E501

        :param total: The total of this PostJournalsJournal.  # noqa: E501
        :type: float
        """

        self._total = total

    @property
    def journal_lines(self):
        """Gets the journal_lines of this PostJournalsJournal.  # noqa: E501


        :return: The journal_lines of this PostJournalsJournal.  # noqa: E501
        :rtype: list[PostJournalsJournalJournalLines]
        """
        return self._journal_lines

    @journal_lines.setter
    def journal_lines(self, journal_lines):
        """Sets the journal_lines of this PostJournalsJournal.


        :param journal_lines: The journal_lines of this PostJournalsJournal.  # noqa: E501
        :type: list[PostJournalsJournalJournalLines]
        """
        if self.local_vars_configuration.client_side_validation and journal_lines is None:  # noqa: E501
            raise ValueError("Invalid value for `journal_lines`, must not be `None`")  # noqa: E501

        self._journal_lines = journal_lines

    @property
    def journal_code(self):
        """Gets the journal_code of this PostJournalsJournal.  # noqa: E501


        :return: The journal_code of this PostJournalsJournal.  # noqa: E501
        :rtype: PostJournalsJournalJournalCode
        """
        return self._journal_code

    @journal_code.setter
    def journal_code(self, journal_code):
        """Sets the journal_code of this PostJournalsJournal.


        :param journal_code: The journal_code of this PostJournalsJournal.  # noqa: E501
        :type: PostJournalsJournalJournalCode
        """

        self._journal_code = journal_code

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
        if not isinstance(other, PostJournalsJournal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostJournalsJournal):
            return True

        return self.to_dict() != other.to_dict()
