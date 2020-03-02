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


class PutPurchaseCreditNotesPurchaseCreditNote(object):
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
        'contact_id': 'str',
        'date': 'date',
        'postponed_accounting': 'bool',
        '_import': 'bool',
        'contact_name': 'str',
        'contact_reference': 'str',
        'reference': 'str',
        'vendor_reference': 'str',
        'notes': 'str',
        'total_quantity': 'float',
        'net_amount': 'float',
        'tax_amount': 'float',
        'total_amount': 'float',
        'currency_id': 'str',
        'exchange_rate': 'float',
        'inverse_exchange_rate': 'str',
        'base_currency_net_amount': 'float',
        'base_currency_tax_amount': 'float',
        'base_currency_total_amount': 'float',
        'status_id': 'str',
        'tax_address_region_id': 'str',
        'credit_note_lines': 'list[PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines]',
        'tax_analysis': 'list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]'
    }

    attribute_map = {
        'contact_id': 'contact_id',
        'date': 'date',
        'postponed_accounting': 'postponed_accounting',
        '_import': 'import',
        'contact_name': 'contact_name',
        'contact_reference': 'contact_reference',
        'reference': 'reference',
        'vendor_reference': 'vendor_reference',
        'notes': 'notes',
        'total_quantity': 'total_quantity',
        'net_amount': 'net_amount',
        'tax_amount': 'tax_amount',
        'total_amount': 'total_amount',
        'currency_id': 'currency_id',
        'exchange_rate': 'exchange_rate',
        'inverse_exchange_rate': 'inverse_exchange_rate',
        'base_currency_net_amount': 'base_currency_net_amount',
        'base_currency_tax_amount': 'base_currency_tax_amount',
        'base_currency_total_amount': 'base_currency_total_amount',
        'status_id': 'status_id',
        'tax_address_region_id': 'tax_address_region_id',
        'credit_note_lines': 'credit_note_lines',
        'tax_analysis': 'tax_analysis'
    }

    def __init__(self, contact_id=None, date=None, postponed_accounting=None, _import=None, contact_name=None, contact_reference=None, reference=None, vendor_reference=None, notes=None, total_quantity=None, net_amount=None, tax_amount=None, total_amount=None, currency_id=None, exchange_rate=None, inverse_exchange_rate=None, base_currency_net_amount=None, base_currency_tax_amount=None, base_currency_total_amount=None, status_id=None, tax_address_region_id=None, credit_note_lines=None, tax_analysis=None, local_vars_configuration=None):  # noqa: E501
        """PutPurchaseCreditNotesPurchaseCreditNote - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._contact_id = None
        self._date = None
        self._postponed_accounting = None
        self.__import = None
        self._contact_name = None
        self._contact_reference = None
        self._reference = None
        self._vendor_reference = None
        self._notes = None
        self._total_quantity = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._currency_id = None
        self._exchange_rate = None
        self._inverse_exchange_rate = None
        self._base_currency_net_amount = None
        self._base_currency_tax_amount = None
        self._base_currency_total_amount = None
        self._status_id = None
        self._tax_address_region_id = None
        self._credit_note_lines = None
        self._tax_analysis = None
        self.discriminator = None

        if contact_id is not None:
            self.contact_id = contact_id
        if date is not None:
            self.date = date
        if postponed_accounting is not None:
            self.postponed_accounting = postponed_accounting
        if _import is not None:
            self._import = _import
        if contact_name is not None:
            self.contact_name = contact_name
        if contact_reference is not None:
            self.contact_reference = contact_reference
        if reference is not None:
            self.reference = reference
        if vendor_reference is not None:
            self.vendor_reference = vendor_reference
        if notes is not None:
            self.notes = notes
        if total_quantity is not None:
            self.total_quantity = total_quantity
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if currency_id is not None:
            self.currency_id = currency_id
        if exchange_rate is not None:
            self.exchange_rate = exchange_rate
        if inverse_exchange_rate is not None:
            self.inverse_exchange_rate = inverse_exchange_rate
        if base_currency_net_amount is not None:
            self.base_currency_net_amount = base_currency_net_amount
        if base_currency_tax_amount is not None:
            self.base_currency_tax_amount = base_currency_tax_amount
        if base_currency_total_amount is not None:
            self.base_currency_total_amount = base_currency_total_amount
        if status_id is not None:
            self.status_id = status_id
        if tax_address_region_id is not None:
            self.tax_address_region_id = tax_address_region_id
        if credit_note_lines is not None:
            self.credit_note_lines = credit_note_lines
        if tax_analysis is not None:
            self.tax_analysis = tax_analysis

    @property
    def contact_id(self):
        """Gets the contact_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The contact the purchase credit note relates to  # noqa: E501

        :return: The contact_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._contact_id

    @contact_id.setter
    def contact_id(self, contact_id):
        """Sets the contact_id of this PutPurchaseCreditNotesPurchaseCreditNote.

        The contact the purchase credit note relates to  # noqa: E501

        :param contact_id: The contact_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._contact_id = contact_id

    @property
    def date(self):
        """Gets the date of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The date of the credit note  # noqa: E501

        :return: The date of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this PutPurchaseCreditNotesPurchaseCreditNote.

        The date of the credit note  # noqa: E501

        :param date: The date of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def postponed_accounting(self):
        """Gets the postponed_accounting of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        Indicates whether postponed accounting rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer  # noqa: E501

        :return: The postponed_accounting of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: bool
        """
        return self._postponed_accounting

    @postponed_accounting.setter
    def postponed_accounting(self, postponed_accounting):
        """Sets the postponed_accounting of this PutPurchaseCreditNotesPurchaseCreditNote.

        Indicates whether postponed accounting rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer  # noqa: E501

        :param postponed_accounting: The postponed_accounting of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: bool
        """

        self._postponed_accounting = postponed_accounting

    @property
    def _import(self):
        """Gets the _import of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        Indicates whether import rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer.  # noqa: E501

        :return: The _import of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: bool
        """
        return self.__import

    @_import.setter
    def _import(self, _import):
        """Sets the _import of this PutPurchaseCreditNotesPurchaseCreditNote.

        Indicates whether import rules are applied to the artefact. Only used for UK and IE accounting businesses, where the supplier is flagged as importer.  # noqa: E501

        :param _import: The _import of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: bool
        """

        self.__import = _import

    @property
    def contact_name(self):
        """Gets the contact_name of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The name of the contact when the credit note was created  # noqa: E501

        :return: The contact_name of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this PutPurchaseCreditNotesPurchaseCreditNote.

        The name of the contact when the credit note was created  # noqa: E501

        :param contact_name: The contact_name of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def contact_reference(self):
        """Gets the contact_reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The reference of the contact when the credit note was created  # noqa: E501

        :return: The contact_reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._contact_reference

    @contact_reference.setter
    def contact_reference(self, contact_reference):
        """Sets the contact_reference of this PutPurchaseCreditNotesPurchaseCreditNote.

        The reference of the contact when the credit note was created  # noqa: E501

        :param contact_reference: The contact_reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._contact_reference = contact_reference

    @property
    def reference(self):
        """Gets the reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The reference for the credit note  # noqa: E501

        :return: The reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PutPurchaseCreditNotesPurchaseCreditNote.

        The reference for the credit note  # noqa: E501

        :param reference: The reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def vendor_reference(self):
        """Gets the vendor_reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The vendor reference for the credit note  # noqa: E501

        :return: The vendor_reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._vendor_reference

    @vendor_reference.setter
    def vendor_reference(self, vendor_reference):
        """Sets the vendor_reference of this PutPurchaseCreditNotesPurchaseCreditNote.

        The vendor reference for the credit note  # noqa: E501

        :param vendor_reference: The vendor_reference of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._vendor_reference = vendor_reference

    @property
    def notes(self):
        """Gets the notes of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        credit note notes  # noqa: E501

        :return: The notes of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this PutPurchaseCreditNotesPurchaseCreditNote.

        credit note notes  # noqa: E501

        :param notes: The notes of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def total_quantity(self):
        """Gets the total_quantity of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The total quantity of the credit note  # noqa: E501

        :return: The total_quantity of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._total_quantity

    @total_quantity.setter
    def total_quantity(self, total_quantity):
        """Sets the total_quantity of this PutPurchaseCreditNotesPurchaseCreditNote.

        The total quantity of the credit note  # noqa: E501

        :param total_quantity: The total_quantity of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._total_quantity = total_quantity

    @property
    def net_amount(self):
        """Gets the net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The net amount of the credit note  # noqa: E501

        :return: The net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.

        The net amount of the credit note  # noqa: E501

        :param net_amount: The net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The tax amount of the credit note  # noqa: E501

        :return: The tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.

        The tax amount of the credit note  # noqa: E501

        :param tax_amount: The tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The total amount of the credit note  # noqa: E501

        :return: The total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.

        The total amount of the credit note  # noqa: E501

        :param total_amount: The total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def currency_id(self):
        """Gets the currency_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The ID of the Currency.  # noqa: E501

        :return: The currency_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this PutPurchaseCreditNotesPurchaseCreditNote.

        The ID of the Currency.  # noqa: E501

        :param currency_id: The currency_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._currency_id = currency_id

    @property
    def exchange_rate(self):
        """Gets the exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The exchange rate for the credit note  # noqa: E501

        :return: The exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        """Sets the exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.

        The exchange rate for the credit note  # noqa: E501

        :param exchange_rate: The exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._exchange_rate = exchange_rate

    @property
    def inverse_exchange_rate(self):
        """Gets the inverse_exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The inverse exchange rate for the credit note  # noqa: E501

        :return: The inverse_exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._inverse_exchange_rate

    @inverse_exchange_rate.setter
    def inverse_exchange_rate(self, inverse_exchange_rate):
        """Sets the inverse_exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.

        The inverse exchange rate for the credit note  # noqa: E501

        :param inverse_exchange_rate: The inverse_exchange_rate of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._inverse_exchange_rate = inverse_exchange_rate

    @property
    def base_currency_net_amount(self):
        """Gets the base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The net amount of the credit note in base currency  # noqa: E501

        :return: The base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_net_amount

    @base_currency_net_amount.setter
    def base_currency_net_amount(self, base_currency_net_amount):
        """Sets the base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.

        The net amount of the credit note in base currency  # noqa: E501

        :param base_currency_net_amount: The base_currency_net_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._base_currency_net_amount = base_currency_net_amount

    @property
    def base_currency_tax_amount(self):
        """Gets the base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The tax amount of the credit note in base currency  # noqa: E501

        :return: The base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_tax_amount

    @base_currency_tax_amount.setter
    def base_currency_tax_amount(self, base_currency_tax_amount):
        """Sets the base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.

        The tax amount of the credit note in base currency  # noqa: E501

        :param base_currency_tax_amount: The base_currency_tax_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._base_currency_tax_amount = base_currency_tax_amount

    @property
    def base_currency_total_amount(self):
        """Gets the base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The total amount of the credit note in base currency  # noqa: E501

        :return: The base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: float
        """
        return self._base_currency_total_amount

    @base_currency_total_amount.setter
    def base_currency_total_amount(self, base_currency_total_amount):
        """Sets the base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.

        The total amount of the credit note in base currency  # noqa: E501

        :param base_currency_total_amount: The base_currency_total_amount of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: float
        """

        self._base_currency_total_amount = base_currency_total_amount

    @property
    def status_id(self):
        """Gets the status_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The ID of the Status.  # noqa: E501

        :return: The status_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._status_id

    @status_id.setter
    def status_id(self, status_id):
        """Sets the status_id of this PutPurchaseCreditNotesPurchaseCreditNote.

        The ID of the Status.  # noqa: E501

        :param status_id: The status_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._status_id = status_id

    @property
    def tax_address_region_id(self):
        """Gets the tax_address_region_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501

        The ID of the Tax Address Region. (Canada only)  # noqa: E501

        :return: The tax_address_region_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: str
        """
        return self._tax_address_region_id

    @tax_address_region_id.setter
    def tax_address_region_id(self, tax_address_region_id):
        """Sets the tax_address_region_id of this PutPurchaseCreditNotesPurchaseCreditNote.

        The ID of the Tax Address Region. (Canada only)  # noqa: E501

        :param tax_address_region_id: The tax_address_region_id of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: str
        """

        self._tax_address_region_id = tax_address_region_id

    @property
    def credit_note_lines(self):
        """Gets the credit_note_lines of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501


        :return: The credit_note_lines of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: list[PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines]
        """
        return self._credit_note_lines

    @credit_note_lines.setter
    def credit_note_lines(self, credit_note_lines):
        """Sets the credit_note_lines of this PutPurchaseCreditNotesPurchaseCreditNote.


        :param credit_note_lines: The credit_note_lines of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: list[PutPurchaseCreditNotesPurchaseCreditNoteCreditNoteLines]
        """

        self._credit_note_lines = credit_note_lines

    @property
    def tax_analysis(self):
        """Gets the tax_analysis of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501


        :return: The tax_analysis of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :rtype: list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]
        """
        return self._tax_analysis

    @tax_analysis.setter
    def tax_analysis(self, tax_analysis):
        """Sets the tax_analysis of this PutPurchaseCreditNotesPurchaseCreditNote.


        :param tax_analysis: The tax_analysis of this PutPurchaseCreditNotesPurchaseCreditNote.  # noqa: E501
        :type: list[PostPurchaseCorrectiveInvoicesPurchaseCorrectiveInvoiceTaxAnalysis]
        """

        self._tax_analysis = tax_analysis

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
        if not isinstance(other, PutPurchaseCreditNotesPurchaseCreditNote):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutPurchaseCreditNotesPurchaseCreditNote):
            return True

        return self.to_dict() != other.to_dict()
