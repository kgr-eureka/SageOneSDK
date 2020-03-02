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


class PostJournalsJournalJournalLines(object):
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
        'ledger_account_id': 'str',
        'debit': 'float',
        'credit': 'float',
        'details': 'str',
        'include_on_tax_return': 'bool',
        'tax_reconciled': 'bool',
        'cleared': 'bool',
        'bank_reconciled': 'bool'
    }

    attribute_map = {
        'ledger_account_id': 'ledger_account_id',
        'debit': 'debit',
        'credit': 'credit',
        'details': 'details',
        'include_on_tax_return': 'include_on_tax_return',
        'tax_reconciled': 'tax_reconciled',
        'cleared': 'cleared',
        'bank_reconciled': 'bank_reconciled'
    }

    def __init__(self, ledger_account_id=None, debit=None, credit=None, details=None, include_on_tax_return=None, tax_reconciled=None, cleared=None, bank_reconciled=None, local_vars_configuration=None):  # noqa: E501
        """PostJournalsJournalJournalLines - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ledger_account_id = None
        self._debit = None
        self._credit = None
        self._details = None
        self._include_on_tax_return = None
        self._tax_reconciled = None
        self._cleared = None
        self._bank_reconciled = None
        self.discriminator = None

        self.ledger_account_id = ledger_account_id
        self.debit = debit
        self.credit = credit
        if details is not None:
            self.details = details
        if include_on_tax_return is not None:
            self.include_on_tax_return = include_on_tax_return
        if tax_reconciled is not None:
            self.tax_reconciled = tax_reconciled
        if cleared is not None:
            self.cleared = cleared
        if bank_reconciled is not None:
            self.bank_reconciled = bank_reconciled

    @property
    def ledger_account_id(self):
        """Gets the ledger_account_id of this PostJournalsJournalJournalLines.  # noqa: E501

        The ID of the Ledger Account.  # noqa: E501

        :return: The ledger_account_id of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: str
        """
        return self._ledger_account_id

    @ledger_account_id.setter
    def ledger_account_id(self, ledger_account_id):
        """Sets the ledger_account_id of this PostJournalsJournalJournalLines.

        The ID of the Ledger Account.  # noqa: E501

        :param ledger_account_id: The ledger_account_id of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and ledger_account_id is None:  # noqa: E501
            raise ValueError("Invalid value for `ledger_account_id`, must not be `None`")  # noqa: E501

        self._ledger_account_id = ledger_account_id

    @property
    def debit(self):
        """Gets the debit of this PostJournalsJournalJournalLines.  # noqa: E501

        The debit amount of the journal line  # noqa: E501

        :return: The debit of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: float
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this PostJournalsJournalJournalLines.

        The debit amount of the journal line  # noqa: E501

        :param debit: The debit of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and debit is None:  # noqa: E501
            raise ValueError("Invalid value for `debit`, must not be `None`")  # noqa: E501

        self._debit = debit

    @property
    def credit(self):
        """Gets the credit of this PostJournalsJournalJournalLines.  # noqa: E501

        The credit amount of the journal line  # noqa: E501

        :return: The credit of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this PostJournalsJournalJournalLines.

        The credit amount of the journal line  # noqa: E501

        :param credit: The credit of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and credit is None:  # noqa: E501
            raise ValueError("Invalid value for `credit`, must not be `None`")  # noqa: E501

        self._credit = credit

    @property
    def details(self):
        """Gets the details of this PostJournalsJournalJournalLines.  # noqa: E501

        A description of the journal line  # noqa: E501

        :return: The details of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this PostJournalsJournalJournalLines.

        A description of the journal line  # noqa: E501

        :param details: The details of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: str
        """

        self._details = details

    @property
    def include_on_tax_return(self):
        """Gets the include_on_tax_return of this PostJournalsJournalJournalLines.  # noqa: E501

        Indicates whether the journal line should affect the tax return  # noqa: E501

        :return: The include_on_tax_return of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: bool
        """
        return self._include_on_tax_return

    @include_on_tax_return.setter
    def include_on_tax_return(self, include_on_tax_return):
        """Sets the include_on_tax_return of this PostJournalsJournalJournalLines.

        Indicates whether the journal line should affect the tax return  # noqa: E501

        :param include_on_tax_return: The include_on_tax_return of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: bool
        """

        self._include_on_tax_return = include_on_tax_return

    @property
    def tax_reconciled(self):
        """Gets the tax_reconciled of this PostJournalsJournalJournalLines.  # noqa: E501

        Indicates if the journal line is tax reconciled or not.  # noqa: E501

        :return: The tax_reconciled of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: bool
        """
        return self._tax_reconciled

    @tax_reconciled.setter
    def tax_reconciled(self, tax_reconciled):
        """Sets the tax_reconciled of this PostJournalsJournalJournalLines.

        Indicates if the journal line is tax reconciled or not.  # noqa: E501

        :param tax_reconciled: The tax_reconciled of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: bool
        """

        self._tax_reconciled = tax_reconciled

    @property
    def cleared(self):
        """Gets the cleared of this PostJournalsJournalJournalLines.  # noqa: E501

        Indicates if the journal line is cleared or not.  # noqa: E501

        :return: The cleared of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: bool
        """
        return self._cleared

    @cleared.setter
    def cleared(self, cleared):
        """Sets the cleared of this PostJournalsJournalJournalLines.

        Indicates if the journal line is cleared or not.  # noqa: E501

        :param cleared: The cleared of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: bool
        """

        self._cleared = cleared

    @property
    def bank_reconciled(self):
        """Gets the bank_reconciled of this PostJournalsJournalJournalLines.  # noqa: E501

        Indicates if the journal line is bank reconciled or not.  # noqa: E501

        :return: The bank_reconciled of this PostJournalsJournalJournalLines.  # noqa: E501
        :rtype: bool
        """
        return self._bank_reconciled

    @bank_reconciled.setter
    def bank_reconciled(self, bank_reconciled):
        """Sets the bank_reconciled of this PostJournalsJournalJournalLines.

        Indicates if the journal line is bank reconciled or not.  # noqa: E501

        :param bank_reconciled: The bank_reconciled of this PostJournalsJournalJournalLines.  # noqa: E501
        :type: bool
        """

        self._bank_reconciled = bank_reconciled

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
        if not isinstance(other, PostJournalsJournalJournalLines):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostJournalsJournalJournalLines):
            return True

        return self.to_dict() != other.to_dict()
