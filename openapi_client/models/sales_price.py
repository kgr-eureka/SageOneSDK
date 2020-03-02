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


class SalesPrice(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'price_name': 'str',
        'price': 'float',
        'price_includes_tax': 'bool',
        'product_sales_price_type': 'Base'
    }

    attribute_map = {
        'legacy_id': 'legacy_id',
        'id': 'id',
        'displayed_as': 'displayed_as',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'price_name': 'price_name',
        'price': 'price',
        'price_includes_tax': 'price_includes_tax',
        'product_sales_price_type': 'product_sales_price_type'
    }

    def __init__(self, legacy_id=None, id=None, displayed_as=None, created_at=None, updated_at=None, price_name=None, price=None, price_includes_tax=None, product_sales_price_type=None, local_vars_configuration=None):  # noqa: E501
        """SalesPrice - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._legacy_id = None
        self._id = None
        self._displayed_as = None
        self._created_at = None
        self._updated_at = None
        self._price_name = None
        self._price = None
        self._price_includes_tax = None
        self._product_sales_price_type = None
        self.discriminator = None

        if legacy_id is not None:
            self.legacy_id = legacy_id
        if id is not None:
            self.id = id
        if displayed_as is not None:
            self.displayed_as = displayed_as
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if price_name is not None:
            self.price_name = price_name
        if price is not None:
            self.price = price
        if price_includes_tax is not None:
            self.price_includes_tax = price_includes_tax
        if product_sales_price_type is not None:
            self.product_sales_price_type = product_sales_price_type

    @property
    def legacy_id(self):
        """Gets the legacy_id of this SalesPrice.  # noqa: E501

        The legacy ID for the item  # noqa: E501

        :return: The legacy_id of this SalesPrice.  # noqa: E501
        :rtype: int
        """
        return self._legacy_id

    @legacy_id.setter
    def legacy_id(self, legacy_id):
        """Sets the legacy_id of this SalesPrice.

        The legacy ID for the item  # noqa: E501

        :param legacy_id: The legacy_id of this SalesPrice.  # noqa: E501
        :type: int
        """

        self._legacy_id = legacy_id

    @property
    def id(self):
        """Gets the id of this SalesPrice.  # noqa: E501

        The unique identifier for the item  # noqa: E501

        :return: The id of this SalesPrice.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SalesPrice.

        The unique identifier for the item  # noqa: E501

        :param id: The id of this SalesPrice.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def displayed_as(self):
        """Gets the displayed_as of this SalesPrice.  # noqa: E501

        The name of the resource  # noqa: E501

        :return: The displayed_as of this SalesPrice.  # noqa: E501
        :rtype: str
        """
        return self._displayed_as

    @displayed_as.setter
    def displayed_as(self, displayed_as):
        """Sets the displayed_as of this SalesPrice.

        The name of the resource  # noqa: E501

        :param displayed_as: The displayed_as of this SalesPrice.  # noqa: E501
        :type: str
        """

        self._displayed_as = displayed_as

    @property
    def created_at(self):
        """Gets the created_at of this SalesPrice.  # noqa: E501

        The datetime when the item was created  # noqa: E501

        :return: The created_at of this SalesPrice.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SalesPrice.

        The datetime when the item was created  # noqa: E501

        :param created_at: The created_at of this SalesPrice.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SalesPrice.  # noqa: E501

        The datetime when the item was last updated  # noqa: E501

        :return: The updated_at of this SalesPrice.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SalesPrice.

        The datetime when the item was last updated  # noqa: E501

        :param updated_at: The updated_at of this SalesPrice.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def price_name(self):
        """Gets the price_name of this SalesPrice.  # noqa: E501

        The name of the product sales price  # noqa: E501

        :return: The price_name of this SalesPrice.  # noqa: E501
        :rtype: str
        """
        return self._price_name

    @price_name.setter
    def price_name(self, price_name):
        """Sets the price_name of this SalesPrice.

        The name of the product sales price  # noqa: E501

        :param price_name: The price_name of this SalesPrice.  # noqa: E501
        :type: str
        """

        self._price_name = price_name

    @property
    def price(self):
        """Gets the price of this SalesPrice.  # noqa: E501

        The sales price amount  # noqa: E501

        :return: The price of this SalesPrice.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this SalesPrice.

        The sales price amount  # noqa: E501

        :param price: The price of this SalesPrice.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def price_includes_tax(self):
        """Gets the price_includes_tax of this SalesPrice.  # noqa: E501

        Indicates whether the sales price already includes tax  # noqa: E501

        :return: The price_includes_tax of this SalesPrice.  # noqa: E501
        :rtype: bool
        """
        return self._price_includes_tax

    @price_includes_tax.setter
    def price_includes_tax(self, price_includes_tax):
        """Sets the price_includes_tax of this SalesPrice.

        Indicates whether the sales price already includes tax  # noqa: E501

        :param price_includes_tax: The price_includes_tax of this SalesPrice.  # noqa: E501
        :type: bool
        """

        self._price_includes_tax = price_includes_tax

    @property
    def product_sales_price_type(self):
        """Gets the product_sales_price_type of this SalesPrice.  # noqa: E501


        :return: The product_sales_price_type of this SalesPrice.  # noqa: E501
        :rtype: Base
        """
        return self._product_sales_price_type

    @product_sales_price_type.setter
    def product_sales_price_type(self, product_sales_price_type):
        """Sets the product_sales_price_type of this SalesPrice.


        :param product_sales_price_type: The product_sales_price_type of this SalesPrice.  # noqa: E501
        :type: Base
        """

        self._product_sales_price_type = product_sales_price_type

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
        if not isinstance(other, SalesPrice):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SalesPrice):
            return True

        return self.to_dict() != other.to_dict()