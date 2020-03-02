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


class PostMigrationTaxReturnsMigrationTaxReturnIe(object):
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
        'box_t1': 'float',
        'box_t2': 'float',
        'box_t3': 'float',
        'box_t4': 'float',
        'box_e1': 'float',
        'box_e2': 'float',
        'box_es1': 'float',
        'box_es2': 'float'
    }

    attribute_map = {
        'box_t1': 'box_T1',
        'box_t2': 'box_T2',
        'box_t3': 'box_T3',
        'box_t4': 'box_T4',
        'box_e1': 'box_E1',
        'box_e2': 'box_E2',
        'box_es1': 'box_ES1',
        'box_es2': 'box_ES2'
    }

    def __init__(self, box_t1=None, box_t2=None, box_t3=None, box_t4=None, box_e1=None, box_e2=None, box_es1=None, box_es2=None, local_vars_configuration=None):  # noqa: E501
        """PostMigrationTaxReturnsMigrationTaxReturnIe - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._box_t1 = None
        self._box_t2 = None
        self._box_t3 = None
        self._box_t4 = None
        self._box_e1 = None
        self._box_e2 = None
        self._box_es1 = None
        self._box_es2 = None
        self.discriminator = None

        if box_t1 is not None:
            self.box_t1 = box_t1
        if box_t2 is not None:
            self.box_t2 = box_t2
        if box_t3 is not None:
            self.box_t3 = box_t3
        if box_t4 is not None:
            self.box_t4 = box_t4
        if box_e1 is not None:
            self.box_e1 = box_e1
        if box_e2 is not None:
            self.box_e2 = box_e2
        if box_es1 is not None:
            self.box_es1 = box_es1
        if box_es2 is not None:
            self.box_es2 = box_es2

    @property
    def box_t1(self):
        """Gets the box_t1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box T1  # noqa: E501

        :return: The box_t1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_t1

    @box_t1.setter
    def box_t1(self, box_t1):
        """Sets the box_t1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box T1  # noqa: E501

        :param box_t1: The box_t1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_t1 = box_t1

    @property
    def box_t2(self):
        """Gets the box_t2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box T2  # noqa: E501

        :return: The box_t2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_t2

    @box_t2.setter
    def box_t2(self, box_t2):
        """Sets the box_t2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box T2  # noqa: E501

        :param box_t2: The box_t2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_t2 = box_t2

    @property
    def box_t3(self):
        """Gets the box_t3 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box T3  # noqa: E501

        :return: The box_t3 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_t3

    @box_t3.setter
    def box_t3(self, box_t3):
        """Sets the box_t3 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box T3  # noqa: E501

        :param box_t3: The box_t3 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_t3 = box_t3

    @property
    def box_t4(self):
        """Gets the box_t4 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box T4  # noqa: E501

        :return: The box_t4 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_t4

    @box_t4.setter
    def box_t4(self, box_t4):
        """Sets the box_t4 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box T4  # noqa: E501

        :param box_t4: The box_t4 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_t4 = box_t4

    @property
    def box_e1(self):
        """Gets the box_e1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box E1  # noqa: E501

        :return: The box_e1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_e1

    @box_e1.setter
    def box_e1(self, box_e1):
        """Sets the box_e1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box E1  # noqa: E501

        :param box_e1: The box_e1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_e1 = box_e1

    @property
    def box_e2(self):
        """Gets the box_e2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box E2  # noqa: E501

        :return: The box_e2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_e2

    @box_e2.setter
    def box_e2(self, box_e2):
        """Sets the box_e2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box E2  # noqa: E501

        :param box_e2: The box_e2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_e2 = box_e2

    @property
    def box_es1(self):
        """Gets the box_es1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box ES1  # noqa: E501

        :return: The box_es1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_es1

    @box_es1.setter
    def box_es1(self, box_es1):
        """Sets the box_es1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box ES1  # noqa: E501

        :param box_es1: The box_es1 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_es1 = box_es1

    @property
    def box_es2(self):
        """Gets the box_es2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501

        The value of box ES2  # noqa: E501

        :return: The box_es2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :rtype: float
        """
        return self._box_es2

    @box_es2.setter
    def box_es2(self, box_es2):
        """Sets the box_es2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.

        The value of box ES2  # noqa: E501

        :param box_es2: The box_es2 of this PostMigrationTaxReturnsMigrationTaxReturnIe.  # noqa: E501
        :type: float
        """

        self._box_es2 = box_es2

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
        if not isinstance(other, PostMigrationTaxReturnsMigrationTaxReturnIe):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostMigrationTaxReturnsMigrationTaxReturnIe):
            return True

        return self.to_dict() != other.to_dict()
