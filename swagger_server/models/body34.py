# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body34(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, insurance_slug: str=None, policy_type: str=None, customer_name: str=None, policy_category: str=None, amount: int=None, reference_identifier: str=None, policy_number: str=None, mobile_number: str=None, service_name: str=None):  # noqa: E501
        """Body34 - a model defined in Swagger

        :param token: The token of this Body34.  # noqa: E501
        :type token: str
        :param insurance_slug: The insurance_slug of this Body34.  # noqa: E501
        :type insurance_slug: str
        :param policy_type: The policy_type of this Body34.  # noqa: E501
        :type policy_type: str
        :param customer_name: The customer_name of this Body34.  # noqa: E501
        :type customer_name: str
        :param policy_category: The policy_category of this Body34.  # noqa: E501
        :type policy_category: str
        :param amount: The amount of this Body34.  # noqa: E501
        :type amount: int
        :param reference_identifier: The reference_identifier of this Body34.  # noqa: E501
        :type reference_identifier: str
        :param policy_number: The policy_number of this Body34.  # noqa: E501
        :type policy_number: str
        :param mobile_number: The mobile_number of this Body34.  # noqa: E501
        :type mobile_number: str
        :param service_name: The service_name of this Body34.  # noqa: E501
        :type service_name: str
        """
        self.swagger_types = {
            'token': str,
            'insurance_slug': str,
            'policy_type': str,
            'customer_name': str,
            'policy_category': str,
            'amount': int,
            'reference_identifier': str,
            'policy_number': str,
            'mobile_number': str,
            'service_name': str
        }

        self.attribute_map = {
            'token': 'token',
            'insurance_slug': 'insurance_slug',
            'policy_type': 'policy_type',
            'customer_name': 'customer_name',
            'policy_category': 'policy_category',
            'amount': 'amount',
            'reference_identifier': 'reference_identifier',
            'policy_number': 'policy_number',
            'mobile_number': 'mobile_number',
            'service_name': 'service_name'
        }
        self._token = token
        self._insurance_slug = insurance_slug
        self._policy_type = policy_type
        self._customer_name = customer_name
        self._policy_category = policy_category
        self._amount = amount
        self._reference_identifier = reference_identifier
        self._policy_number = policy_number
        self._mobile_number = mobile_number
        self._service_name = service_name

    @classmethod
    def from_dict(cls, dikt) -> 'Body34':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_34 of this Body34.  # noqa: E501
        :rtype: Body34
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body34.


        :return: The token of this Body34.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body34.


        :param token: The token of this Body34.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def insurance_slug(self) -> str:
        """Gets the insurance_slug of this Body34.


        :return: The insurance_slug of this Body34.
        :rtype: str
        """
        return self._insurance_slug

    @insurance_slug.setter
    def insurance_slug(self, insurance_slug: str):
        """Sets the insurance_slug of this Body34.


        :param insurance_slug: The insurance_slug of this Body34.
        :type insurance_slug: str
        """

        self._insurance_slug = insurance_slug

    @property
    def policy_type(self) -> str:
        """Gets the policy_type of this Body34.


        :return: The policy_type of this Body34.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type: str):
        """Sets the policy_type of this Body34.


        :param policy_type: The policy_type of this Body34.
        :type policy_type: str
        """

        self._policy_type = policy_type

    @property
    def customer_name(self) -> str:
        """Gets the customer_name of this Body34.


        :return: The customer_name of this Body34.
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name: str):
        """Sets the customer_name of this Body34.


        :param customer_name: The customer_name of this Body34.
        :type customer_name: str
        """

        self._customer_name = customer_name

    @property
    def policy_category(self) -> str:
        """Gets the policy_category of this Body34.


        :return: The policy_category of this Body34.
        :rtype: str
        """
        return self._policy_category

    @policy_category.setter
    def policy_category(self, policy_category: str):
        """Sets the policy_category of this Body34.


        :param policy_category: The policy_category of this Body34.
        :type policy_category: str
        """

        self._policy_category = policy_category

    @property
    def amount(self) -> int:
        """Gets the amount of this Body34.


        :return: The amount of this Body34.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Body34.


        :param amount: The amount of this Body34.
        :type amount: int
        """

        self._amount = amount

    @property
    def reference_identifier(self) -> str:
        """Gets the reference_identifier of this Body34.


        :return: The reference_identifier of this Body34.
        :rtype: str
        """
        return self._reference_identifier

    @reference_identifier.setter
    def reference_identifier(self, reference_identifier: str):
        """Sets the reference_identifier of this Body34.


        :param reference_identifier: The reference_identifier of this Body34.
        :type reference_identifier: str
        """

        self._reference_identifier = reference_identifier

    @property
    def policy_number(self) -> str:
        """Gets the policy_number of this Body34.


        :return: The policy_number of this Body34.
        :rtype: str
        """
        return self._policy_number

    @policy_number.setter
    def policy_number(self, policy_number: str):
        """Sets the policy_number of this Body34.


        :param policy_number: The policy_number of this Body34.
        :type policy_number: str
        """

        self._policy_number = policy_number

    @property
    def mobile_number(self) -> str:
        """Gets the mobile_number of this Body34.


        :return: The mobile_number of this Body34.
        :rtype: str
        """
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number: str):
        """Sets the mobile_number of this Body34.


        :param mobile_number: The mobile_number of this Body34.
        :type mobile_number: str
        """

        self._mobile_number = mobile_number

    @property
    def service_name(self) -> str:
        """Gets the service_name of this Body34.


        :return: The service_name of this Body34.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name: str):
        """Sets the service_name of this Body34.


        :param service_name: The service_name of this Body34.
        :type service_name: str
        """

        self._service_name = service_name
