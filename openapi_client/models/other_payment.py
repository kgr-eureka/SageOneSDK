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


class OtherPayment(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'transaction': 'Base',
        'transaction_type': 'Base',
        'deleted_at': 'datetime',
        'payment_method': 'Base',
        'contact': 'Base',
        'bank_account': 'Base',
        'tax_address_region': 'Base',
        'date': 'date',
        'net_amount': 'float',
        'tax_amount': 'float',
        'total_amount': 'float',
        'reference': 'str',
        'payment_lines': 'list[OtherPaymentLineItem]',
        'editable': 'bool',
        'deletable': 'bool',
        'withholding_tax_rate': 'float',
        'withholding_tax_amount': 'float'
    }

    attribute_map = {
        'legacy_id': 'legacy_id',
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'transaction': 'transaction',
        'transaction_type': 'transaction_type',
        'deleted_at': 'deleted_at',
        'payment_method': 'payment_method',
        'contact': 'contact',
        'bank_account': 'bank_account',
        'tax_address_region': 'tax_address_region',
        'date': 'date',
        'net_amount': 'net_amount',
        'tax_amount': 'tax_amount',
        'total_amount': 'total_amount',
        'reference': 'reference',
        'payment_lines': 'payment_lines',
        'editable': 'editable',
        'deletable': 'deletable',
        'withholding_tax_rate': 'withholding_tax_rate',
        'withholding_tax_amount': 'withholding_tax_amount'
    }

    def __init__(self, legacy_id=None, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, transaction=None, transaction_type=None, deleted_at=None, payment_method=None, contact=None, bank_account=None, tax_address_region=None, date=None, net_amount=None, tax_amount=None, total_amount=None, reference=None, payment_lines=None, editable=None, deletable=None, withholding_tax_rate=None, withholding_tax_amount=None, local_vars_configuration=None):  # noqa: E501
        """OtherPayment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._legacy_id = None
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._transaction = None
        self._transaction_type = None
        self._deleted_at = None
        self._payment_method = None
        self._contact = None
        self._bank_account = None
        self._tax_address_region = None
        self._date = None
        self._net_amount = None
        self._tax_amount = None
        self._total_amount = None
        self._reference = None
        self._payment_lines = None
        self._editable = None
        self._deletable = None
        self._withholding_tax_rate = None
        self._withholding_tax_amount = None
        self.discriminator = None

        if legacy_id is not None:
            self.legacy_id = legacy_id
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if transaction is not None:
            self.transaction = transaction
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if payment_method is not None:
            self.payment_method = payment_method
        if contact is not None:
            self.contact = contact
        if bank_account is not None:
            self.bank_account = bank_account
        if tax_address_region is not None:
            self.tax_address_region = tax_address_region
        if date is not None:
            self.date = date
        if net_amount is not None:
            self.net_amount = net_amount
        if tax_amount is not None:
            self.tax_amount = tax_amount
        if total_amount is not None:
            self.total_amount = total_amount
        if reference is not None:
            self.reference = reference
        if payment_lines is not None:
            self.payment_lines = payment_lines
        if editable is not None:
            self.editable = editable
        if deletable is not None:
            self.deletable = deletable
        if withholding_tax_rate is not None:
            self.withholding_tax_rate = withholding_tax_rate
        if withholding_tax_amount is not None:
            self.withholding_tax_amount = withholding_tax_amount

    @property
    def legacy_id(self):
        """Gets the legacy_id of this OtherPayment.  # noqa: E501

        The legacy ID for the item  # noqa: E501

        :return: The legacy_id of this OtherPayment.  # noqa: E501
        :rtype: int
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """Sets the legacy_id of this OtherPayment.

        The legacy ID for the item  # noqa: E501

        :param legacy_id: The legacy_id of this OtherPayment.  # noqa: E501
        :type: int
        """

        self._legacy_id = legacy_id

    @property
    def id(self):
        """Gets the id of this OtherPayment.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this OtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OtherPayment.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this OtherPayment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this OtherPayment.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this OtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this OtherPayment.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this OtherPayment.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this OtherPayment.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this OtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this OtherPayment.

        The API path for the resource  # noqa: E501

        :param path: The path of this OtherPayment.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this OtherPayment.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this OtherPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OtherPayment.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this OtherPayment.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this OtherPayment.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this OtherPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this OtherPayment.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this OtherPayment.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def transaction(self):
        """Gets the transaction of this OtherPayment.  # noqa: E501


        :return: The transaction of this OtherPayment.  # noqa: E501
        :rtype: Base
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this OtherPayment.


        :param transaction: The transaction of this OtherPayment.  # noqa: E501
        :type: Base
        """

        self._transaction = transaction

    @property
    def transaction_type(self):
        """Gets the transaction_type of this OtherPayment.  # noqa: E501


        :return: The transaction_type of this OtherPayment.  # noqa: E501
        :rtype: Base
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this OtherPayment.


        :param transaction_type: The transaction_type of this OtherPayment.  # noqa: E501
        :type: Base
        """

        self._transaction_type = transaction_type

    @property
    def deleted_at(self):
        """Gets the deleted_at of this OtherPayment.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this OtherPayment.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this OtherPayment.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this OtherPayment.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def payment_method(self):
        """Gets the payment_method of this OtherPayment.  # noqa: E501


        :return: The payment_method of this OtherPayment.  # noqa: E501
        :rtype: Base
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this OtherPayment.


        :param payment_method: The payment_method of this OtherPayment.  # noqa: E501
        :type: Base
        """

        self._payment_method = payment_method

    @property
    def contact(self):
        """Gets the contact of this OtherPayment.  # noqa: E501


        :return: The contact of this OtherPayment.  # noqa: E501
        :rtype: Base
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this OtherPayment.


        :param contact: The contact of this OtherPayment.  # noqa: E501
        :type: Base
        """

        self._contact = contact

    @property
    def bank_account(self):
        """Gets the bank_account of this OtherPayment.  # noqa: E501


        :return: The bank_account of this OtherPayment.  # noqa: E501
        :rtype: Base
        """
        return self._bank_account

    @bank_account.setter
    def bank_account(self, bank_account):
        """Sets the bank_account of this OtherPayment.


        :param bank_account: The bank_account of this OtherPayment.  # noqa: E501
        :type: Base
        """

        self._bank_account = bank_account

    @property
    def tax_address_region(self):
        """Gets the tax_address_region of this OtherPayment.  # noqa: E501


        :return: The tax_address_region of this OtherPayment.  # noqa: E501
        :rtype: Base
        """
        return self._tax_address_region

    @tax_address_region.setter
    def tax_address_region(self, tax_address_region):
        """Sets the tax_address_region of this OtherPayment.


        :param tax_address_region: The tax_address_region of this OtherPayment.  # noqa: E501
        :type: Base
        """

        self._tax_address_region = tax_address_region

    @property
    def date(self):
        """Gets the date of this OtherPayment.  # noqa: E501

        The date of the payment  # noqa: E501

        :return: The date of this OtherPayment.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this OtherPayment.

        The date of the payment  # noqa: E501

        :param date: The date of this OtherPayment.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def net_amount(self):
        """Gets the net_amount of this OtherPayment.  # noqa: E501

        The net amount of the payment  # noqa: E501

        :return: The net_amount of this OtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._net_amount

    @net_amount.setter
    def net_amount(self, net_amount):
        """Sets the net_amount of this OtherPayment.

        The net amount of the payment  # noqa: E501

        :param net_amount: The net_amount of this OtherPayment.  # noqa: E501
        :type: float
        """

        self._net_amount = net_amount

    @property
    def tax_amount(self):
        """Gets the tax_amount of this OtherPayment.  # noqa: E501

        The tax amount of the payment  # noqa: E501

        :return: The tax_amount of this OtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this OtherPayment.

        The tax amount of the payment  # noqa: E501

        :param tax_amount: The tax_amount of this OtherPayment.  # noqa: E501
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def total_amount(self):
        """Gets the total_amount of this OtherPayment.  # noqa: E501

        The total amount of the payment  # noqa: E501

        :return: The total_amount of this OtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this OtherPayment.

        The total amount of the payment  # noqa: E501

        :param total_amount: The total_amount of this OtherPayment.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def reference(self):
        """Gets the reference of this OtherPayment.  # noqa: E501

        A reference of the payment Note: An upper length limit of 25 or 40 characters is imposed conditionally and may not apply in every request. A hard upper limit of 255 characters is imposed by the storage layer, though.  # noqa: E501

        :return: The reference of this OtherPayment.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this OtherPayment.

        A reference of the payment Note: An upper length limit of 25 or 40 characters is imposed conditionally and may not apply in every request. A hard upper limit of 255 characters is imposed by the storage layer, though.  # noqa: E501

        :param reference: The reference of this OtherPayment.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 25):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `25`")  # noqa: E501

        self._reference = reference

    @property
    def payment_lines(self):
        """Gets the payment_lines of this OtherPayment.  # noqa: E501

        The payment lines of the payment  # noqa: E501

        :return: The payment_lines of this OtherPayment.  # noqa: E501
        :rtype: list[OtherPaymentLineItem]
        """
        return self._payment_lines

    @payment_lines.setter
    def payment_lines(self, payment_lines):
        """Sets the payment_lines of this OtherPayment.

        The payment lines of the payment  # noqa: E501

        :param payment_lines: The payment_lines of this OtherPayment.  # noqa: E501
        :type: list[OtherPaymentLineItem]
        """

        self._payment_lines = payment_lines

    @property
    def editable(self):
        """Gets the editable of this OtherPayment.  # noqa: E501

        Indicates whether or not the payment can be edited  # noqa: E501

        :return: The editable of this OtherPayment.  # noqa: E501
        :rtype: bool
        """
        return self._editable

    @editable.setter
    def editable(self, editable):
        """Sets the editable of this OtherPayment.

        Indicates whether or not the payment can be edited  # noqa: E501

        :param editable: The editable of this OtherPayment.  # noqa: E501
        :type: bool
        """

        self._editable = editable

    @property
    def deletable(self):
        """Gets the deletable of this OtherPayment.  # noqa: E501

        Indicates whether or not the payment can be deleted  # noqa: E501

        :return: The deletable of this OtherPayment.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this OtherPayment.

        Indicates whether or not the payment can be deleted  # noqa: E501

        :param deletable: The deletable of this OtherPayment.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

    @property
    def withholding_tax_rate(self):
        """Gets the withholding_tax_rate of this OtherPayment.  # noqa: E501

        IRPF withheld tax rate  # noqa: E501

        :return: The withholding_tax_rate of this OtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._withholding_tax_rate

    @withholding_tax_rate.setter
    def withholding_tax_rate(self, withholding_tax_rate):
        """Sets the withholding_tax_rate of this OtherPayment.

        IRPF withheld tax rate  # noqa: E501

        :param withholding_tax_rate: The withholding_tax_rate of this OtherPayment.  # noqa: E501
        :type: float
        """

        self._withholding_tax_rate = withholding_tax_rate

    @property
    def withholding_tax_amount(self):
        """Gets the withholding_tax_amount of this OtherPayment.  # noqa: E501

        IRPF withheld tax amount  # noqa: E501

        :return: The withholding_tax_amount of this OtherPayment.  # noqa: E501
        :rtype: float
        """
        return self._withholding_tax_amount

    @withholding_tax_amount.setter
    def withholding_tax_amount(self, withholding_tax_amount):
        """Sets the withholding_tax_amount of this OtherPayment.

        IRPF withheld tax amount  # noqa: E501

        :param withholding_tax_amount: The withholding_tax_amount of this OtherPayment.  # noqa: E501
        :type: float
        """

        self._withholding_tax_amount = withholding_tax_amount

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
        if not isinstance(other, OtherPayment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OtherPayment):
            return True

        return self.to_dict() != other.to_dict()
