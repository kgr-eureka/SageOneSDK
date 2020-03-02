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


class TaxProfile(object):
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
        'tax_type': 'Base',
        'tax_number': 'str',
        'tax_number_suffix': 'str',
        'collect_tax': 'bool',
        'tax_return_frequency': 'Base',
        'address_region': 'AddressRegion'
    }

    attribute_map = {
        'legacy_id': 'legacy_id',
        'id': 'id',
        'displayed_as': 'displayed_as',
        'path': '$path',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'tax_type': 'tax_type',
        'tax_number': 'tax_number',
        'tax_number_suffix': 'tax_number_suffix',
        'collect_tax': 'collect_tax',
        'tax_return_frequency': 'tax_return_frequency',
        'address_region': 'address_region'
    }

    def __init__(self, legacy_id=None, id=None, displayed_as=None, path=None, created_at=None, updated_at=None, tax_type=None, tax_number=None, tax_number_suffix=None, collect_tax=None, tax_return_frequency=None, address_region=None, local_vars_configuration=None):  # noqa: E501
        """TaxProfile - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._legacy_id = None
        self._id = None
        self._displayed_as = None
        self._path = None
        self._created_at = None
        self._updated_at = None
        self._tax_type = None
        self._tax_number = None
        self._tax_number_suffix = None
        self._collect_tax = None
        self._tax_return_frequency = None
        self._address_region = None
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
        if tax_type is not None:
            self.tax_type = tax_type
        if tax_number is not None:
            self.tax_number = tax_number
        if tax_number_suffix is not None:
            self.tax_number_suffix = tax_number_suffix
        if collect_tax is not None:
            self.collect_tax = collect_tax
        if tax_return_frequency is not None:
            self.tax_return_frequency = tax_return_frequency
        if address_region is not None:
            self.address_region = address_region

    @property
    def legacy_id(self):
        """Gets the legacy_id of this TaxProfile.  # noqa: E501

        The legacy ID for the item  # noqa: E501

        :return: The legacy_id of this TaxProfile.  # noqa: E501
        :rtype: int
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """Sets the legacy_id of this TaxProfile.

        The legacy ID for the item  # noqa: E501

        :param legacy_id: The legacy_id of this TaxProfile.  # noqa: E501
        :type: int
        """

        self._legacy_id = legacy_id

    @property
    def id(self):
        """Gets the id of this TaxProfile.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this TaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaxProfile.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this TaxProfile.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this TaxProfile.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this TaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this TaxProfile.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this TaxProfile.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def path(self):
        """Gets the path of this TaxProfile.  # noqa: E501

        The API path for the resource  # noqa: E501

        :return: The path of this TaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this TaxProfile.

        The API path for the resource  # noqa: E501

        :param path: The path of this TaxProfile.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def created_at(self):
        """Gets the created_at of this TaxProfile.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this TaxProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaxProfile.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this TaxProfile.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaxProfile.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this TaxProfile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaxProfile.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this TaxProfile.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def tax_type(self):
        """Gets the tax_type of this TaxProfile.  # noqa: E501


        :return: The tax_type of this TaxProfile.  # noqa: E501
        :rtype: Base
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this TaxProfile.


        :param tax_type: The tax_type of this TaxProfile.  # noqa: E501
        :type: Base
        """

        self._tax_type = tax_type

    @property
    def tax_number(self):
        """Gets the tax_number of this TaxProfile.  # noqa: E501

        The tax number  # noqa: E501

        :return: The tax_number of this TaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._tax_number

    @tax_number.setter
    def tax_number(self, tax_number):
        """Sets the tax_number of this TaxProfile.

        The tax number  # noqa: E501

        :param tax_number: The tax_number of this TaxProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tax_number is not None and len(tax_number) > 255):
            raise ValueError("Invalid value for `tax_number`, length must be less than or equal to `255`")  # noqa: E501

        self._tax_number = tax_number

    @property
    def tax_number_suffix(self):
        """Gets the tax_number_suffix of this TaxProfile.  # noqa: E501

        The tax number suffix  # noqa: E501

        :return: The tax_number_suffix of this TaxProfile.  # noqa: E501
        :rtype: str
        """
        return self._tax_number_suffix

    @tax_number_suffix.setter
    def tax_number_suffix(self, tax_number_suffix):
        """Sets the tax_number_suffix of this TaxProfile.

        The tax number suffix  # noqa: E501

        :param tax_number_suffix: The tax_number_suffix of this TaxProfile.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                tax_number_suffix is not None and len(tax_number_suffix) > 255):
            raise ValueError("Invalid value for `tax_number_suffix`, length must be less than or equal to `255`")  # noqa: E501

        self._tax_number_suffix = tax_number_suffix

    @property
    def collect_tax(self):
        """Gets the collect_tax of this TaxProfile.  # noqa: E501

        Indicates whether tax is collected for this tax type  # noqa: E501

        :return: The collect_tax of this TaxProfile.  # noqa: E501
        :rtype: bool
        """
        return self._collect_tax

    @collect_tax.setter
    def collect_tax(self, collect_tax):
        """Sets the collect_tax of this TaxProfile.

        Indicates whether tax is collected for this tax type  # noqa: E501

        :param collect_tax: The collect_tax of this TaxProfile.  # noqa: E501
        :type: bool
        """

        self._collect_tax = collect_tax

    @property
    def tax_return_frequency(self):
        """Gets the tax_return_frequency of this TaxProfile.  # noqa: E501


        :return: The tax_return_frequency of this TaxProfile.  # noqa: E501
        :rtype: Base
        """
        return self._tax_return_frequency

    @tax_return_frequency.setter
    def tax_return_frequency(self, tax_return_frequency):
        """Sets the tax_return_frequency of this TaxProfile.


        :param tax_return_frequency: The tax_return_frequency of this TaxProfile.  # noqa: E501
        :type: Base
        """

        self._tax_return_frequency = tax_return_frequency

    @property
    def address_region(self):
        """Gets the address_region of this TaxProfile.  # noqa: E501


        :return: The address_region of this TaxProfile.  # noqa: E501
        :rtype: AddressRegion
        """
        return self._address_region

    @address_region.setter
    def address_region(self, address_region):
        """Sets the address_region of this TaxProfile.


        :param address_region: The address_region of this TaxProfile.  # noqa: E501
        :type: AddressRegion
        """

        self._address_region = address_region

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
        if not isinstance(other, TaxProfile):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TaxProfile):
            return True

        return self.to_dict() != other.to_dict()
