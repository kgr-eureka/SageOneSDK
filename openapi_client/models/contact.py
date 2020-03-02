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


class Contact(object):
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
        'links': 'list[Link]',
        'deleted_at': 'datetime',
        'balance': 'float',
        'contact_types': 'list[Base]',
        'name': 'str',
        'reference': 'str',
        'default_sales_ledger_account': 'LedgerAccount',
        'default_sales_tax_rate': 'Base',
        'default_purchase_ledger_account': 'LedgerAccount',
        'tax_number': 'str',
        'notes': 'str',
        'locale': 'str',
        'main_address': 'Address',
        'delivery_address': 'Address',
        'main_contact_person': 'ContactPerson',
        'bank_account_details': 'BankAccountDetails',
        'credit_limit': 'float',
        'credit_days': 'int',
        'credit_terms_and_conditions': 'str',
        'product_sales_price_type': 'Base',
        'source_guid': 'str',
        'currency': 'Base',
        'aux_reference': 'str',
        'registered_number': 'str',
        'deletable': 'bool',
        'tax_treatment': 'ContactTaxTreatment',
        'email': 'str',
        'tax_calculation': 'str',
        'auxiliary_account': 'str',
        'gdpr_obfuscated': 'bool',
        'system': 'bool'
    }

    attribute_map = {
        'legacy_id': 'legacy_id',
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': 'links',
        'deleted_at': 'deleted_at',
        'balance': 'balance',
        'contact_types': 'contact_types',
        'name': 'name',
        'reference': 'reference',
        'default_sales_ledger_account': 'default_sales_ledger_account',
        'default_sales_tax_rate': 'default_sales_tax_rate',
        'default_purchase_ledger_account': 'default_purchase_ledger_account',
        'tax_number': 'tax_number',
        'notes': 'notes',
        'locale': 'locale',
        'main_address': 'main_address',
        'delivery_address': 'delivery_address',
        'main_contact_person': 'main_contact_person',
        'bank_account_details': 'bank_account_details',
        'credit_limit': 'credit_limit',
        'credit_days': 'credit_days',
        'credit_terms_and_conditions': 'credit_terms_and_conditions',
        'product_sales_price_type': 'product_sales_price_type',
        'source_guid': 'source_guid',
        'currency': 'currency',
        'aux_reference': 'aux_reference',
        'registered_number': 'registered_number',
        'deletable': 'deletable',
        'tax_treatment': 'tax_treatment',
        'email': 'email',
        'tax_calculation': 'tax_calculation',
        'auxiliary_account': 'auxiliary_account',
        'gdpr_obfuscated': 'gdpr_obfuscated',
        'system': 'system'
    }

    def __init__(self, legacy_id=None, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, links=None, deleted_at=None, balance=None, contact_types=None, name=None, reference=None, default_sales_ledger_account=None, default_sales_tax_rate=None, default_purchase_ledger_account=None, tax_number=None, notes=None, locale=None, main_address=None, delivery_address=None, main_contact_person=None, bank_account_details=None, credit_limit=None, credit_days=None, credit_terms_and_conditions=None, product_sales_price_type=None, source_guid=None, currency=None, aux_reference=None, registered_number=None, deletable=None, tax_treatment=None, email=None, tax_calculation=None, auxiliary_account=None, gdpr_obfuscated=None, system=None, local_vars_configuration=None):  # noqa: E501
        """Contact - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._legacy_id = None
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self._deleted_at = None
        self._balance = None
        self._contact_types = None
        self._name = None
        self._reference = None
        self._default_sales_ledger_account = None
        self._default_sales_tax_rate = None
        self._default_purchase_ledger_account = None
        self._tax_number = None
        self._notes = None
        self._locale = None
        self._main_address = None
        self._delivery_address = None
        self._main_contact_person = None
        self._bank_account_details = None
        self._credit_limit = None
        self._credit_days = None
        self._credit_terms_and_conditions = None
        self._product_sales_price_type = None
        self._source_guid = None
        self._currency = None
        self._aux_reference = None
        self._registered_number = None
        self._deletable = None
        self._tax_treatment = None
        self._email = None
        self._tax_calculation = None
        self._auxiliary_account = None
        self._gdpr_obfuscated = None
        self._system = None
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
        if links is not None:
            self.links = links
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if balance is not None:
            self.balance = balance
        if contact_types is not None:
            self.contact_types = contact_types
        if name is not None:
            self.name = name
        if reference is not None:
            self.reference = reference
        if default_sales_ledger_account is not None:
            self.default_sales_ledger_account = default_sales_ledger_account
        if default_sales_tax_rate is not None:
            self.default_sales_tax_rate = default_sales_tax_rate
        if default_purchase_ledger_account is not None:
            self.default_purchase_ledger_account = default_purchase_ledger_account
        if tax_number is not None:
            self.tax_number = tax_number
        if notes is not None:
            self.notes = notes
        if locale is not None:
            self.locale = locale
        if main_address is not None:
            self.main_address = main_address
        if delivery_address is not None:
            self.delivery_address = delivery_address
        if main_contact_person is not None:
            self.main_contact_person = main_contact_person
        if bank_account_details is not None:
            self.bank_account_details = bank_account_details
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if credit_days is not None:
            self.credit_days = credit_days
        if credit_terms_and_conditions is not None:
            self.credit_terms_and_conditions = credit_terms_and_conditions
        if product_sales_price_type is not None:
            self.product_sales_price_type = product_sales_price_type
        if source_guid is not None:
            self.source_guid = source_guid
        if currency is not None:
            self.currency = currency
        if aux_reference is not None:
            self.aux_reference = aux_reference
        if registered_number is not None:
            self.registered_number = registered_number
        if deletable is not None:
            self.deletable = deletable
        if tax_treatment is not None:
            self.tax_treatment = tax_treatment
        if email is not None:
            self.email = email
        if tax_calculation is not None:
            self.tax_calculation = tax_calculation
        if auxiliary_account is not None:
            self.auxiliary_account = auxiliary_account
        if gdpr_obfuscated is not None:
            self.gdpr_obfuscated = gdpr_obfuscated
        if system is not None:
            self.system = system

    @property
    def legacy_id(self):
        """Gets the legacy_id of this Contact.  # noqa: E501

        The legacy ID for the item  # noqa: E501

        :return: The legacy_id of this Contact.  # noqa: E501
        :rtype: int
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """Sets the legacy_id of this Contact.

        The legacy ID for the item  # noqa: E501

        :param legacy_id: The legacy_id of this Contact.  # noqa: E501
        :type: int
        """

        self._legacy_id = legacy_id

    @property
    def id(self):
        """Gets the id of this Contact.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Contact.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this Contact.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this Contact.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this Contact.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this Contact.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this Contact.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Contact.

        The API path for the resource  # noqa: E501

        :param path: The path of this Contact.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this Contact.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this Contact.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Contact.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this Contact.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Contact.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this Contact.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Contact.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this Contact.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this Contact.  # noqa: E501

        Links for the resource  # noqa: E501

        :return: The links of this Contact.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Contact.

        Links for the resource  # noqa: E501

        :param links: The links of this Contact.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def deleted_at(self):
        """Gets the deleted_at of this Contact.  # noqa: E501

        The datetime when the item was deleted  # noqa: E501

        :return: The deleted_at of this Contact.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this Contact.

        The datetime when the item was deleted  # noqa: E501

        :param deleted_at: The deleted_at of this Contact.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def balance(self):
        """Gets the balance of this Contact.  # noqa: E501

        The contact balance  # noqa: E501

        :return: The balance of this Contact.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Contact.

        The contact balance  # noqa: E501

        :param balance: The balance of this Contact.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def contact_types(self):
        """Gets the contact_types of this Contact.  # noqa: E501

        The contact types for the contact  # noqa: E501

        :return: The contact_types of this Contact.  # noqa: E501
        :rtype: list[Base]
        """
        return self._contact_types

    @contact_types.setter
    def contact_types(self, contact_types):
        """Sets the contact_types of this Contact.

        The contact types for the contact  # noqa: E501

        :param contact_types: The contact_types of this Contact.  # noqa: E501
        :type: list[Base]
        """

        self._contact_types = contact_types

    @property
    def name(self):
        """Gets the name of this Contact.  # noqa: E501

        The name of the contact  # noqa: E501

        :return: The name of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Contact.

        The name of the contact  # noqa: E501

        :param name: The name of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def reference(self):
        """Gets the reference of this Contact.  # noqa: E501

        The reference for the contact  # noqa: E501

        :return: The reference of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Contact.

        The reference for the contact  # noqa: E501

        :param reference: The reference of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                reference is not None and len(reference) > 10):
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `10`")  # noqa: E501

        self._reference = reference

    @property
    def default_sales_ledger_account(self):
        """Gets the default_sales_ledger_account of this Contact.  # noqa: E501


        :return: The default_sales_ledger_account of this Contact.  # noqa: E501
        :rtype: LedgerAccount
        """
        return self._default_sales_ledger_account

    @default_sales_ledger_account.setter
    def default_sales_ledger_account(self, default_sales_ledger_account):
        """Sets the default_sales_ledger_account of this Contact.


        :param default_sales_ledger_account: The default_sales_ledger_account of this Contact.  # noqa: E501
        :type: LedgerAccount
        """

        self._default_sales_ledger_account = default_sales_ledger_account

    @property
    def default_sales_tax_rate(self):
        """Gets the default_sales_tax_rate of this Contact.  # noqa: E501


        :return: The default_sales_tax_rate of this Contact.  # noqa: E501
        :rtype: Base
        """
        return self._default_sales_tax_rate

    @default_sales_tax_rate.setter
    def default_sales_tax_rate(self, default_sales_tax_rate):
        """Sets the default_sales_tax_rate of this Contact.


        :param default_sales_tax_rate: The default_sales_tax_rate of this Contact.  # noqa: E501
        :type: Base
        """

        self._default_sales_tax_rate = default_sales_tax_rate

    @property
    def default_purchase_ledger_account(self):
        """Gets the default_purchase_ledger_account of this Contact.  # noqa: E501


        :return: The default_purchase_ledger_account of this Contact.  # noqa: E501
        :rtype: LedgerAccount
        """
        return self._default_purchase_ledger_account

    @default_purchase_ledger_account.setter
    def default_purchase_ledger_account(self, default_purchase_ledger_account):
        """Sets the default_purchase_ledger_account of this Contact.


        :param default_purchase_ledger_account: The default_purchase_ledger_account of this Contact.  # noqa: E501
        :type: LedgerAccount
        """

        self._default_purchase_ledger_account = default_purchase_ledger_account

    @property
    def tax_number(self):
        """Gets the tax_number of this Contact.  # noqa: E501

        The tax number for the contact  # noqa: E501

        :return: The tax_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this Contact.

        The tax number for the contact  # noqa: E501

        :param tax_number: The tax_number of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tax_number is not None and len(tax_number) > 255):
            raise ValueError("Invalid value for `tax_number`, length must be less than or equal to `255`")  # noqa: E501

        self._tax_number = tax_number

    @property
    def notes(self):
        """Gets the notes of this Contact.  # noqa: E501

        The notes for the contact  # noqa: E501

        :return: The notes of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this Contact.

        The notes for the contact  # noqa: E501

        :param notes: The notes of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                notes is not None and len(notes) > 4000):
            raise ValueError("Invalid value for `notes`, length must be less than or equal to `4000`")  # noqa: E501

        self._notes = notes

    @property
    def locale(self):
        """Gets the locale of this Contact.  # noqa: E501

        The locale for the contact  # noqa: E501

        :return: The locale of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this Contact.

        The locale for the contact  # noqa: E501

        :param locale: The locale of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                locale is not None and len(locale) > 10):
            raise ValueError("Invalid value for `locale`, length must be less than or equal to `10`")  # noqa: E501

        self._locale = locale

    @property
    def main_address(self):
        """Gets the main_address of this Contact.  # noqa: E501


        :return: The main_address of this Contact.  # noqa: E501
        :rtype: Address
        """
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        """Sets the main_address of this Contact.


        :param main_address: The main_address of this Contact.  # noqa: E501
        :type: Address
        """

        self._main_address = main_address

    @property
    def delivery_address(self):
        """Gets the delivery_address of this Contact.  # noqa: E501


        :return: The delivery_address of this Contact.  # noqa: E501
        :rtype: Address
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this Contact.


        :param delivery_address: The delivery_address of this Contact.  # noqa: E501
        :type: Address
        """

        self._delivery_address = delivery_address

    @property
    def main_contact_person(self):
        """Gets the main_contact_person of this Contact.  # noqa: E501


        :return: The main_contact_person of this Contact.  # noqa: E501
        :rtype: ContactPerson
        """
        return self._main_contact_person

    @main_contact_person.setter
    def main_contact_person(self, main_contact_person):
        """Sets the main_contact_person of this Contact.


        :param main_contact_person: The main_contact_person of this Contact.  # noqa: E501
        :type: ContactPerson
        """

        self._main_contact_person = main_contact_person

    @property
    def bank_account_details(self):
        """Gets the bank_account_details of this Contact.  # noqa: E501


        :return: The bank_account_details of this Contact.  # noqa: E501
        :rtype: BankAccountDetails
        """
        return self._bank_account_details

    @bank_account_details.setter
    def bank_account_details(self, bank_account_details):
        """Sets the bank_account_details of this Contact.


        :param bank_account_details: The bank_account_details of this Contact.  # noqa: E501
        :type: BankAccountDetails
        """

        self._bank_account_details = bank_account_details

    @property
    def credit_limit(self):
        """Gets the credit_limit of this Contact.  # noqa: E501

        Custom credit limit amount for the contact  # noqa: E501

        :return: The credit_limit of this Contact.  # noqa: E501
        :rtype: float
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this Contact.

        Custom credit limit amount for the contact  # noqa: E501

        :param credit_limit: The credit_limit of this Contact.  # noqa: E501
        :type: float
        """

        self._credit_limit = credit_limit

    @property
    def credit_days(self):
        """Gets the credit_days of this Contact.  # noqa: E501

        Custom credit days for the contact If returned as null in a GET response, you may want to GET /invoice_settings and use 'vendor_credit_days' as default/fallback according to your use case.   # noqa: E501

        :return: The credit_days of this Contact.  # noqa: E501
        :rtype: int
        """
        return self._credit_days

    @credit_days.setter
    def credit_days(self, credit_days):
        """Sets the credit_days of this Contact.

        Custom credit days for the contact If returned as null in a GET response, you may want to GET /invoice_settings and use 'vendor_credit_days' as default/fallback according to your use case.   # noqa: E501

        :param credit_days: The credit_days of this Contact.  # noqa: E501
        :type: int
        """

        self._credit_days = credit_days

    @property
    def credit_terms_and_conditions(self):
        """Gets the credit_terms_and_conditions of this Contact.  # noqa: E501

        Custom terms and conditions for the contact (Customers only)  # noqa: E501

        :return: The credit_terms_and_conditions of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._credit_terms_and_conditions

    @credit_terms_and_conditions.setter
    def credit_terms_and_conditions(self, credit_terms_and_conditions):
        """Sets the credit_terms_and_conditions of this Contact.

        Custom terms and conditions for the contact (Customers only)  # noqa: E501

        :param credit_terms_and_conditions: The credit_terms_and_conditions of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                credit_terms_and_conditions is not None and len(credit_terms_and_conditions) > 2000):
            raise ValueError("Invalid value for `credit_terms_and_conditions`, length must be less than or equal to `2000`")  # noqa: E501

        self._credit_terms_and_conditions = credit_terms_and_conditions

    @property
    def product_sales_price_type(self):
        """Gets the product_sales_price_type of this Contact.  # noqa: E501


        :return: The product_sales_price_type of this Contact.  # noqa: E501
        :rtype: Base
        """
        return self._product_sales_price_type

    @product_sales_price_type.setter
    def product_sales_price_type(self, product_sales_price_type):
        """Sets the product_sales_price_type of this Contact.


        :param product_sales_price_type: The product_sales_price_type of this Contact.  # noqa: E501
        :type: Base
        """

        self._product_sales_price_type = product_sales_price_type

    @property
    def source_guid(self):
        """Gets the source_guid of this Contact.  # noqa: E501

        Used when importing contacts from external sources  # noqa: E501

        :return: The source_guid of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._source_guid

    @source_guid.setter
    def source_guid(self, source_guid):
        """Sets the source_guid of this Contact.

        Used when importing contacts from external sources  # noqa: E501

        :param source_guid: The source_guid of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                source_guid is not None and len(source_guid) > 255):
            raise ValueError("Invalid value for `source_guid`, length must be less than or equal to `255`")  # noqa: E501

        self._source_guid = source_guid

    @property
    def currency(self):
        """Gets the currency of this Contact.  # noqa: E501


        :return: The currency of this Contact.  # noqa: E501
        :rtype: Base
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Contact.


        :param currency: The currency of this Contact.  # noqa: E501
        :type: Base
        """

        self._currency = currency

    @property
    def aux_reference(self):
        """Gets the aux_reference of this Contact.  # noqa: E501

        Auxiliary reference. Used for German \"Kreditorennummer\" and \"Debitorennummer\"  # noqa: E501

        :return: The aux_reference of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._aux_reference

    @aux_reference.setter
    def aux_reference(self, aux_reference):
        """Sets the aux_reference of this Contact.

        Auxiliary reference. Used for German \"Kreditorennummer\" and \"Debitorennummer\"  # noqa: E501

        :param aux_reference: The aux_reference of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                aux_reference is not None and len(aux_reference) > 4):
            raise ValueError("Invalid value for `aux_reference`, length must be less than or equal to `4`")  # noqa: E501

        self._aux_reference = aux_reference

    @property
    def registered_number(self):
        """Gets the registered_number of this Contact.  # noqa: E501

        The registered number of the contact's business. Only used for German businesses and represents the \"Steuernummer\" there (not the \"USt-ID\").  # noqa: E501

        :return: The registered_number of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._registered_number

    @registered_number.setter
    def registered_number(self, registered_number):
        """Sets the registered_number of this Contact.

        The registered number of the contact's business. Only used for German businesses and represents the \"Steuernummer\" there (not the \"USt-ID\").  # noqa: E501

        :param registered_number: The registered_number of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                registered_number is not None and len(registered_number) > 25):
            raise ValueError("Invalid value for `registered_number`, length must be less than or equal to `25`")  # noqa: E501

        self._registered_number = registered_number

    @property
    def deletable(self):
        """Gets the deletable of this Contact.  # noqa: E501

        Indicates whether the ledger entry has been deleted or not  # noqa: E501

        :return: The deletable of this Contact.  # noqa: E501
        :rtype: bool
        """
        return self._deletable

    @deletable.setter
    def deletable(self, deletable):
        """Sets the deletable of this Contact.

        Indicates whether the ledger entry has been deleted or not  # noqa: E501

        :param deletable: The deletable of this Contact.  # noqa: E501
        :type: bool
        """

        self._deletable = deletable

    @property
    def tax_treatment(self):
        """Gets the tax_treatment of this Contact.  # noqa: E501


        :return: The tax_treatment of this Contact.  # noqa: E501
        :rtype: ContactTaxTreatment
        """
        return self._tax_treatment

    @tax_treatment.setter
    def tax_treatment(self, tax_treatment):
        """Sets the tax_treatment of this Contact.


        :param tax_treatment: The tax_treatment of this Contact.  # noqa: E501
        :type: ContactTaxTreatment
        """

        self._tax_treatment = tax_treatment

    @property
    def email(self):
        """Gets the email of this Contact.  # noqa: E501

        The email address for the given contact  # noqa: E501

        :return: The email of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Contact.

        The email address for the given contact  # noqa: E501

        :param email: The email of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 100):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `100`")  # noqa: E501

        self._email = email

    @property
    def tax_calculation(self):
        """Gets the tax_calculation of this Contact.  # noqa: E501

        The tax calculation method - used for French VAT & Recargo  # noqa: E501

        :return: The tax_calculation of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._tax_calculation

    @tax_calculation.setter
    def tax_calculation(self, tax_calculation):
        """Sets the tax_calculation of this Contact.

        The tax calculation method - used for French VAT & Recargo  # noqa: E501

        :param tax_calculation: The tax_calculation of this Contact.  # noqa: E501
        :type: str
        """

        self._tax_calculation = tax_calculation

    @property
    def auxiliary_account(self):
        """Gets the auxiliary_account of this Contact.  # noqa: E501

        Auxiliary account - used when auxiliary accounting is enabled in business settings  # noqa: E501

        :return: The auxiliary_account of this Contact.  # noqa: E501
        :rtype: str
        """
        return self._auxiliary_account

    @auxiliary_account.setter
    def auxiliary_account(self, auxiliary_account):
        """Sets the auxiliary_account of this Contact.

        Auxiliary account - used when auxiliary accounting is enabled in business settings  # noqa: E501

        :param auxiliary_account: The auxiliary_account of this Contact.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                auxiliary_account is not None and len(auxiliary_account) > 25):
            raise ValueError("Invalid value for `auxiliary_account`, length must be less than or equal to `25`")  # noqa: E501

        self._auxiliary_account = auxiliary_account

    @property
    def gdpr_obfuscated(self):
        """Gets the gdpr_obfuscated of this Contact.  # noqa: E501

        General Data Protection Regulation (GDPR) came into effect on 25th May 2018. It introduces new rules for how business owners manage their contacts' personal data. When this field returns 'true', means that the contact has been requested to be obfuscated and you can not create any artifact (sales invoices, purchase invoices, ...) but you can still check previously created artifacts.  # noqa: E501

        :return: The gdpr_obfuscated of this Contact.  # noqa: E501
        :rtype: bool
        """
        return self._gdpr_obfuscated

    @gdpr_obfuscated.setter
    def gdpr_obfuscated(self, gdpr_obfuscated):
        """Sets the gdpr_obfuscated of this Contact.

        General Data Protection Regulation (GDPR) came into effect on 25th May 2018. It introduces new rules for how business owners manage their contacts' personal data. When this field returns 'true', means that the contact has been requested to be obfuscated and you can not create any artifact (sales invoices, purchase invoices, ...) but you can still check previously created artifacts.  # noqa: E501

        :param gdpr_obfuscated: The gdpr_obfuscated of this Contact.  # noqa: E501
        :type: bool
        """

        self._gdpr_obfuscated = gdpr_obfuscated

    @property
    def system(self):
        """Gets the system of this Contact.  # noqa: E501

        Identifies a contact as being a system contact used for processing specific transaction types and reserved specifically for those transaction types such as tax return payments/refunds.  # noqa: E501

        :return: The system of this Contact.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Contact.

        Identifies a contact as being a system contact used for processing specific transaction types and reserved specifically for those transaction types such as tax return payments/refunds.  # noqa: E501

        :param system: The system of this Contact.  # noqa: E501
        :type: bool
        """

        self._system = system

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
        if not isinstance(other, Contact):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Contact):
            return True

        return self.to_dict() != other.to_dict()
