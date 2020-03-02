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


class PostContactPersonsContactPerson(object):
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
        'address_id': 'str',
        'name': 'str',
        'contact_person_type_ids': 'list[str]',
        'job_title': 'str',
        'telephone': 'str',
        'mobile': 'str',
        'email': 'str',
        'fax': 'str',
        'is_main_contact': 'bool',
        'is_preferred_contact': 'bool'
    }

    attribute_map = {
        'address_id': 'address_id',
        'name': 'name',
        'contact_person_type_ids': 'contact_person_type_ids',
        'job_title': 'job_title',
        'telephone': 'telephone',
        'mobile': 'mobile',
        'email': 'email',
        'fax': 'fax',
        'is_main_contact': 'is_main_contact',
        'is_preferred_contact': 'is_preferred_contact'
    }

    def __init__(self, address_id=None, name=None, contact_person_type_ids=None, job_title=None, telephone=None, mobile=None, email=None, fax=None, is_main_contact=None, is_preferred_contact=None, local_vars_configuration=None):  # noqa: E501
        """PostContactPersonsContactPerson - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_id = None
        self._name = None
        self._contact_person_type_ids = None
        self._job_title = None
        self._telephone = None
        self._mobile = None
        self._email = None
        self._fax = None
        self._is_main_contact = None
        self._is_preferred_contact = None
        self.discriminator = None

        self.address_id = address_id
        self.name = name
        self.contact_person_type_ids = contact_person_type_ids
        if job_title is not None:
            self.job_title = job_title
        if telephone is not None:
            self.telephone = telephone
        if mobile is not None:
            self.mobile = mobile
        if email is not None:
            self.email = email
        if fax is not None:
            self.fax = fax
        if is_main_contact is not None:
            self.is_main_contact = is_main_contact
        if is_preferred_contact is not None:
            self.is_preferred_contact = is_preferred_contact

    @property
    def address_id(self):
        """Gets the address_id of this PostContactPersonsContactPerson.  # noqa: E501

        The address of the contact person  # noqa: E501

        :return: The address_id of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._address_id

    @address_id.setter
    def address_id(self, address_id):
        """Sets the address_id of this PostContactPersonsContactPerson.

        The address of the contact person  # noqa: E501

        :param address_id: The address_id of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and address_id is None:  # noqa: E501
            raise ValueError("Invalid value for `address_id`, must not be `None`")  # noqa: E501

        self._address_id = address_id

    @property
    def name(self):
        """Gets the name of this PostContactPersonsContactPerson.  # noqa: E501

        The name of the contact person  # noqa: E501

        :return: The name of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostContactPersonsContactPerson.

        The name of the contact person  # noqa: E501

        :param name: The name of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def contact_person_type_ids(self):
        """Gets the contact_person_type_ids of this PostContactPersonsContactPerson.  # noqa: E501

        The IDs of the Contact Person Types.  # noqa: E501

        :return: The contact_person_type_ids of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: list[str]
        """
        return self._contact_person_type_ids

    @contact_person_type_ids.setter
    def contact_person_type_ids(self, contact_person_type_ids):
        """Sets the contact_person_type_ids of this PostContactPersonsContactPerson.

        The IDs of the Contact Person Types.  # noqa: E501

        :param contact_person_type_ids: The contact_person_type_ids of this PostContactPersonsContactPerson.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and contact_person_type_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `contact_person_type_ids`, must not be `None`")  # noqa: E501

        self._contact_person_type_ids = contact_person_type_ids

    @property
    def job_title(self):
        """Gets the job_title of this PostContactPersonsContactPerson.  # noqa: E501

        The job title of the contact person  # noqa: E501

        :return: The job_title of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """Sets the job_title of this PostContactPersonsContactPerson.

        The job title of the contact person  # noqa: E501

        :param job_title: The job_title of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """

        self._job_title = job_title

    @property
    def telephone(self):
        """Gets the telephone of this PostContactPersonsContactPerson.  # noqa: E501

        The telephone number of the contact person  # noqa: E501

        :return: The telephone of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PostContactPersonsContactPerson.

        The telephone number of the contact person  # noqa: E501

        :param telephone: The telephone of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def mobile(self):
        """Gets the mobile of this PostContactPersonsContactPerson.  # noqa: E501

        The mobile number of the contact person  # noqa: E501

        :return: The mobile of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """Sets the mobile of this PostContactPersonsContactPerson.

        The mobile number of the contact person  # noqa: E501

        :param mobile: The mobile of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """

        self._mobile = mobile

    @property
    def email(self):
        """Gets the email of this PostContactPersonsContactPerson.  # noqa: E501

        The email address of the contact person  # noqa: E501

        :return: The email of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PostContactPersonsContactPerson.

        The email address of the contact person  # noqa: E501

        :param email: The email of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def fax(self):
        """Gets the fax of this PostContactPersonsContactPerson.  # noqa: E501

        The fax number of the contact person  # noqa: E501

        :return: The fax of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """Sets the fax of this PostContactPersonsContactPerson.

        The fax number of the contact person  # noqa: E501

        :param fax: The fax of this PostContactPersonsContactPerson.  # noqa: E501
        :type: str
        """

        self._fax = fax

    @property
    def is_main_contact(self):
        """Gets the is_main_contact of this PostContactPersonsContactPerson.  # noqa: E501

        Indicates whether this is the main contact person  # noqa: E501

        :return: The is_main_contact of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: bool
        """
        return self._is_main_contact

    @is_main_contact.setter
    def is_main_contact(self, is_main_contact):
        """Sets the is_main_contact of this PostContactPersonsContactPerson.

        Indicates whether this is the main contact person  # noqa: E501

        :param is_main_contact: The is_main_contact of this PostContactPersonsContactPerson.  # noqa: E501
        :type: bool
        """

        self._is_main_contact = is_main_contact

    @property
    def is_preferred_contact(self):
        """Gets the is_preferred_contact of this PostContactPersonsContactPerson.  # noqa: E501

        Indicates that this contact person is a preferred contact  # noqa: E501

        :return: The is_preferred_contact of this PostContactPersonsContactPerson.  # noqa: E501
        :rtype: bool
        """
        return self._is_preferred_contact

    @is_preferred_contact.setter
    def is_preferred_contact(self, is_preferred_contact):
        """Sets the is_preferred_contact of this PostContactPersonsContactPerson.

        Indicates that this contact person is a preferred contact  # noqa: E501

        :param is_preferred_contact: The is_preferred_contact of this PostContactPersonsContactPerson.  # noqa: E501
        :type: bool
        """

        self._is_preferred_contact = is_preferred_contact

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
        if not isinstance(other, PostContactPersonsContactPerson):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PostContactPersonsContactPerson):
            return True

        return self.to_dict() != other.to_dict()
