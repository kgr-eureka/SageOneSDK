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


class PutFinancialSettingsFinancialSettings(object):
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
        'year_end_date': 'date',
        'year_end_lockdown_date': 'date',
        'accounting_type': 'str',
        'accounts_start_date': 'date',
        'base_currency_id': 'str',
        'multi_currency_enabled': 'bool',
        'use_live_exchange_rates': 'bool',
        'mtd_activation_status': 'str',
        'mtd_connected': 'bool',
        'mtd_authenticated_date': 'date',
        'tax_return_frequency_id': 'str',
        'tax_number': 'str',
        'general_tax_number': 'str',
        'tax_office_id': 'str',
        'default_irpf_rate': 'float',
        'flat_rate_tax_percentage': 'float',
        'sales_tax_calculation': 'str',
        'purchase_tax_calculation': 'str'
    }

    attribute_map = {
        'year_end_date': 'year_end_date',
        'year_end_lockdown_date': 'year_end_lockdown_date',
        'accounting_type': 'accounting_type',
        'accounts_start_date': 'accounts_start_date',
        'base_currency_id': 'base_currency_id',
        'multi_currency_enabled': 'multi_currency_enabled',
        'use_live_exchange_rates': 'use_live_exchange_rates',
        'mtd_activation_status': 'mtd_activation_status',
        'mtd_connected': 'mtd_connected',
        'mtd_authenticated_date': 'mtd_authenticated_date',
        'tax_return_frequency_id': 'tax_return_frequency_id',
        'tax_number': 'tax_number',
        'general_tax_number': 'general_tax_number',
        'tax_office_id': 'tax_office_id',
        'default_irpf_rate': 'default_irpf_rate',
        'flat_rate_tax_percentage': 'flat_rate_tax_percentage',
        'sales_tax_calculation': 'sales_tax_calculation',
        'purchase_tax_calculation': 'purchase_tax_calculation'
    }

    def __init__(self, year_end_date=None, year_end_lockdown_date=None, accounting_type=None, accounts_start_date=None, base_currency_id=None, multi_currency_enabled=None, use_live_exchange_rates=None, mtd_activation_status=None, mtd_connected=None, mtd_authenticated_date=None, tax_return_frequency_id=None, tax_number=None, general_tax_number=None, tax_office_id=None, default_irpf_rate=None, flat_rate_tax_percentage=None, sales_tax_calculation=None, purchase_tax_calculation=None, local_vars_configuration=None):  # noqa: E501
        """PutFinancialSettingsFinancialSettings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._year_end_date = None
        self._year_end_lockdown_date = None
        self._accounting_type = None
        self._accounts_start_date = None
        self._base_currency_id = None
        self._multi_currency_enabled = None
        self._use_live_exchange_rates = None
        self._mtd_activation_status = None
        self._mtd_connected = None
        self._mtd_authenticated_date = None
        self._tax_return_frequency_id = None
        self._tax_number = None
        self._general_tax_number = None
        self._tax_office_id = None
        self._default_irpf_rate = None
        self._flat_rate_tax_percentage = None
        self._sales_tax_calculation = None
        self._purchase_tax_calculation = None
        self.discriminator = None

        if year_end_date is not None:
            self.year_end_date = year_end_date
        if year_end_lockdown_date is not None:
            self.year_end_lockdown_date = year_end_lockdown_date
        if accounting_type is not None:
            self.accounting_type = accounting_type
        if accounts_start_date is not None:
            self.accounts_start_date = accounts_start_date
        if base_currency_id is not None:
            self.base_currency_id = base_currency_id
        if multi_currency_enabled is not None:
            self.multi_currency_enabled = multi_currency_enabled
        if use_live_exchange_rates is not None:
            self.use_live_exchange_rates = use_live_exchange_rates
        if mtd_activation_status is not None:
            self.mtd_activation_status = mtd_activation_status
        if mtd_connected is not None:
            self.mtd_connected = mtd_connected
        if mtd_authenticated_date is not None:
            self.mtd_authenticated_date = mtd_authenticated_date
        if tax_return_frequency_id is not None:
            self.tax_return_frequency_id = tax_return_frequency_id
        if tax_number is not None:
            self.tax_number = tax_number
        if general_tax_number is not None:
            self.general_tax_number = general_tax_number
        if tax_office_id is not None:
            self.tax_office_id = tax_office_id
        if default_irpf_rate is not None:
            self.default_irpf_rate = default_irpf_rate
        if flat_rate_tax_percentage is not None:
            self.flat_rate_tax_percentage = flat_rate_tax_percentage
        if sales_tax_calculation is not None:
            self.sales_tax_calculation = sales_tax_calculation
        if purchase_tax_calculation is not None:
            self.purchase_tax_calculation = purchase_tax_calculation

    @property
    def year_end_date(self):
        """Gets the year_end_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The financial year end date of the business  # noqa: E501

        :return: The year_end_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: date
        """
        return self._year_end_date

    @year_end_date.setter
    def year_end_date(self, year_end_date):
        """Sets the year_end_date of this PutFinancialSettingsFinancialSettings.

        The financial year end date of the business  # noqa: E501

        :param year_end_date: The year_end_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: date
        """

        self._year_end_date = year_end_date

    @property
    def year_end_lockdown_date(self):
        """Gets the year_end_lockdown_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The year end lockdown date of the business  # noqa: E501

        :return: The year_end_lockdown_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: date
        """
        return self._year_end_lockdown_date

    @year_end_lockdown_date.setter
    def year_end_lockdown_date(self, year_end_lockdown_date):
        """Sets the year_end_lockdown_date of this PutFinancialSettingsFinancialSettings.

        The year end lockdown date of the business  # noqa: E501

        :param year_end_lockdown_date: The year_end_lockdown_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: date
        """

        self._year_end_lockdown_date = year_end_lockdown_date

    @property
    def accounting_type(self):
        """Gets the accounting_type of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        Indicates the accounting type of a business, it can be accrual or cash based  # noqa: E501

        :return: The accounting_type of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._accounting_type

    @accounting_type.setter
    def accounting_type(self, accounting_type):
        """Sets the accounting_type of this PutFinancialSettingsFinancialSettings.

        Indicates the accounting type of a business, it can be accrual or cash based  # noqa: E501

        :param accounting_type: The accounting_type of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._accounting_type = accounting_type

    @property
    def accounts_start_date(self):
        """Gets the accounts_start_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The accounts start date of the business  # noqa: E501

        :return: The accounts_start_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: date
        """
        return self._accounts_start_date

    @accounts_start_date.setter
    def accounts_start_date(self, accounts_start_date):
        """Sets the accounts_start_date of this PutFinancialSettingsFinancialSettings.

        The accounts start date of the business  # noqa: E501

        :param accounts_start_date: The accounts_start_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: date
        """

        self._accounts_start_date = accounts_start_date

    @property
    def base_currency_id(self):
        """Gets the base_currency_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The ID of the Base Currency.  # noqa: E501

        :return: The base_currency_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._base_currency_id

    @base_currency_id.setter
    def base_currency_id(self, base_currency_id):
        """Sets the base_currency_id of this PutFinancialSettingsFinancialSettings.

        The ID of the Base Currency.  # noqa: E501

        :param base_currency_id: The base_currency_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._base_currency_id = base_currency_id

    @property
    def multi_currency_enabled(self):
        """Gets the multi_currency_enabled of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        Indicates whether multi-currency is enabled for the business  # noqa: E501

        :return: The multi_currency_enabled of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: bool
        """
        return self._multi_currency_enabled

    @multi_currency_enabled.setter
    def multi_currency_enabled(self, multi_currency_enabled):
        """Sets the multi_currency_enabled of this PutFinancialSettingsFinancialSettings.

        Indicates whether multi-currency is enabled for the business  # noqa: E501

        :param multi_currency_enabled: The multi_currency_enabled of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: bool
        """

        self._multi_currency_enabled = multi_currency_enabled

    @property
    def use_live_exchange_rates(self):
        """Gets the use_live_exchange_rates of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        Indicates whether to use live or business defined exchange rates  # noqa: E501

        :return: The use_live_exchange_rates of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_live_exchange_rates

    @use_live_exchange_rates.setter
    def use_live_exchange_rates(self, use_live_exchange_rates):
        """Sets the use_live_exchange_rates of this PutFinancialSettingsFinancialSettings.

        Indicates whether to use live or business defined exchange rates  # noqa: E501

        :param use_live_exchange_rates: The use_live_exchange_rates of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: bool
        """

        self._use_live_exchange_rates = use_live_exchange_rates

    @property
    def mtd_activation_status(self):
        """Gets the mtd_activation_status of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        Indicates the UK Making Tax Digital for VAT activation status  # noqa: E501

        :return: The mtd_activation_status of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._mtd_activation_status

    @mtd_activation_status.setter
    def mtd_activation_status(self, mtd_activation_status):
        """Sets the mtd_activation_status of this PutFinancialSettingsFinancialSettings.

        Indicates the UK Making Tax Digital for VAT activation status  # noqa: E501

        :param mtd_activation_status: The mtd_activation_status of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._mtd_activation_status = mtd_activation_status

    @property
    def mtd_connected(self):
        """Gets the mtd_connected of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        Indicates whether UK Making Tax Digital for VAT is currently connected  # noqa: E501

        :return: The mtd_connected of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: bool
        """
        return self._mtd_connected

    @mtd_connected.setter
    def mtd_connected(self, mtd_connected):
        """Sets the mtd_connected of this PutFinancialSettingsFinancialSettings.

        Indicates whether UK Making Tax Digital for VAT is currently connected  # noqa: E501

        :param mtd_connected: The mtd_connected of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: bool
        """

        self._mtd_connected = mtd_connected

    @property
    def mtd_authenticated_date(self):
        """Gets the mtd_authenticated_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        Indicates when a UK business enabled UK Making Tax Digital for VAT, nil if not enabled or non-uk  # noqa: E501

        :return: The mtd_authenticated_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: date
        """
        return self._mtd_authenticated_date

    @mtd_authenticated_date.setter
    def mtd_authenticated_date(self, mtd_authenticated_date):
        """Sets the mtd_authenticated_date of this PutFinancialSettingsFinancialSettings.

        Indicates when a UK business enabled UK Making Tax Digital for VAT, nil if not enabled or non-uk  # noqa: E501

        :param mtd_authenticated_date: The mtd_authenticated_date of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: date
        """

        self._mtd_authenticated_date = mtd_authenticated_date

    @property
    def tax_return_frequency_id(self):
        """Gets the tax_return_frequency_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The ID of the Tax Return Frequency.  # noqa: E501

        :return: The tax_return_frequency_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._tax_return_frequency_id

    @tax_return_frequency_id.setter
    def tax_return_frequency_id(self, tax_return_frequency_id):
        """Sets the tax_return_frequency_id of this PutFinancialSettingsFinancialSettings.

        The ID of the Tax Return Frequency.  # noqa: E501

        :param tax_return_frequency_id: The tax_return_frequency_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._tax_return_frequency_id = tax_return_frequency_id

    @property
    def tax_number(self):
        """Gets the tax_number of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The tax number  # noqa: E501

        :return: The tax_number of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this PutFinancialSettingsFinancialSettings.

        The tax number  # noqa: E501

        :param tax_number: The tax_number of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._tax_number = tax_number

    @property
    def general_tax_number(self):
        """Gets the general_tax_number of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The number for various tax report submissions  # noqa: E501

        :return: The general_tax_number of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._general_tax_number

    @general_tax_number.setter
    def general_tax_number(self, general_tax_number):
        """Sets the general_tax_number of this PutFinancialSettingsFinancialSettings.

        The number for various tax report submissions  # noqa: E501

        :param general_tax_number: The general_tax_number of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._general_tax_number = general_tax_number

    @property
    def tax_office_id(self):
        """Gets the tax_office_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The ID of the Tax Office.  # noqa: E501

        :return: The tax_office_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._tax_office_id

    @tax_office_id.setter
    def tax_office_id(self, tax_office_id):
        """Sets the tax_office_id of this PutFinancialSettingsFinancialSettings.

        The ID of the Tax Office.  # noqa: E501

        :param tax_office_id: The tax_office_id of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._tax_office_id = tax_office_id

    @property
    def default_irpf_rate(self):
        """Gets the default_irpf_rate of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The default IRPF rate  # noqa: E501

        :return: The default_irpf_rate of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: float
        """
        return self._default_irpf_rate

    @default_irpf_rate.setter
    def default_irpf_rate(self, default_irpf_rate):
        """Sets the default_irpf_rate of this PutFinancialSettingsFinancialSettings.

        The default IRPF rate  # noqa: E501

        :param default_irpf_rate: The default_irpf_rate of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: float
        """

        self._default_irpf_rate = default_irpf_rate

    @property
    def flat_rate_tax_percentage(self):
        """Gets the flat_rate_tax_percentage of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The tax percentage that applies to flat rate tax schemes.  # noqa: E501

        :return: The flat_rate_tax_percentage of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: float
        """
        return self._flat_rate_tax_percentage

    @flat_rate_tax_percentage.setter
    def flat_rate_tax_percentage(self, flat_rate_tax_percentage):
        """Sets the flat_rate_tax_percentage of this PutFinancialSettingsFinancialSettings.

        The tax percentage that applies to flat rate tax schemes.  # noqa: E501

        :param flat_rate_tax_percentage: The flat_rate_tax_percentage of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: float
        """

        self._flat_rate_tax_percentage = flat_rate_tax_percentage

    @property
    def sales_tax_calculation(self):
        """Gets the sales_tax_calculation of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The method of collection for tax on sales. Allowed values - \"invoice\", \"cash\".  # noqa: E501

        :return: The sales_tax_calculation of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._sales_tax_calculation

    @sales_tax_calculation.setter
    def sales_tax_calculation(self, sales_tax_calculation):
        """Sets the sales_tax_calculation of this PutFinancialSettingsFinancialSettings.

        The method of collection for tax on sales. Allowed values - \"invoice\", \"cash\".  # noqa: E501

        :param sales_tax_calculation: The sales_tax_calculation of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._sales_tax_calculation = sales_tax_calculation

    @property
    def purchase_tax_calculation(self):
        """Gets the purchase_tax_calculation of this PutFinancialSettingsFinancialSettings.  # noqa: E501

        The method of collection for tax on purchases. Allowed values - \"invoice\", \"cash\".  # noqa: E501

        :return: The purchase_tax_calculation of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :rtype: str
        """
        return self._purchase_tax_calculation

    @purchase_tax_calculation.setter
    def purchase_tax_calculation(self, purchase_tax_calculation):
        """Sets the purchase_tax_calculation of this PutFinancialSettingsFinancialSettings.

        The method of collection for tax on purchases. Allowed values - \"invoice\", \"cash\".  # noqa: E501

        :param purchase_tax_calculation: The purchase_tax_calculation of this PutFinancialSettingsFinancialSettings.  # noqa: E501
        :type: str
        """

        self._purchase_tax_calculation = purchase_tax_calculation

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
        if not isinstance(other, PutFinancialSettingsFinancialSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PutFinancialSettingsFinancialSettings):
            return True

        return self.to_dict() != other.to_dict()
