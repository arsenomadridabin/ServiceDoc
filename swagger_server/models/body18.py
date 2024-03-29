# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body18(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, username: str=None, reference: str=None, amount: int=None, payment_type: str=None, option_id: str=None, plan_category_id: str=None):  # noqa: E501
        """Body18 - a model defined in Swagger

        :param token: The token of this Body18.  # noqa: E501
        :type token: str
        :param username: The username of this Body18.  # noqa: E501
        :type username: str
        :param reference: The reference of this Body18.  # noqa: E501
        :type reference: str
        :param amount: The amount of this Body18.  # noqa: E501
        :type amount: int
        :param payment_type: The payment_type of this Body18.  # noqa: E501
        :type payment_type: str
        :param option_id: The option_id of this Body18.  # noqa: E501
        :type option_id: str
        :param plan_category_id: The plan_category_id of this Body18.  # noqa: E501
        :type plan_category_id: str
        """
        self.swagger_types = {
            'token': str,
            'username': str,
            'reference': str,
            'amount': int,
            'payment_type': str,
            'option_id': str,
            'plan_category_id': str
        }

        self.attribute_map = {
            'token': 'token',
            'username': 'username',
            'reference': 'reference',
            'amount': 'amount',
            'payment_type': 'payment_type',
            'option_id': 'option_id',
            'plan_category_id': 'plan_category_id'
        }
        self._token = token
        self._username = username
        self._reference = reference
        self._amount = amount
        self._payment_type = payment_type
        self._option_id = option_id
        self._plan_category_id = plan_category_id

    @classmethod
    def from_dict(cls, dikt) -> 'Body18':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_18 of this Body18.  # noqa: E501
        :rtype: Body18
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body18.


        :return: The token of this Body18.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body18.


        :param token: The token of this Body18.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def username(self) -> str:
        """Gets the username of this Body18.


        :return: The username of this Body18.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Body18.


        :param username: The username of this Body18.
        :type username: str
        """

        self._username = username

    @property
    def reference(self) -> str:
        """Gets the reference of this Body18.


        :return: The reference of this Body18.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Body18.


        :param reference: The reference of this Body18.
        :type reference: str
        """

        self._reference = reference

    @property
    def amount(self) -> int:
        """Gets the amount of this Body18.


        :return: The amount of this Body18.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Body18.


        :param amount: The amount of this Body18.
        :type amount: int
        """

        self._amount = amount

    @property
    def payment_type(self) -> str:
        """Gets the payment_type of this Body18.


        :return: The payment_type of this Body18.
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type: str):
        """Sets the payment_type of this Body18.


        :param payment_type: The payment_type of this Body18.
        :type payment_type: str
        """

        self._payment_type = payment_type

    @property
    def option_id(self) -> str:
        """Gets the option_id of this Body18.


        :return: The option_id of this Body18.
        :rtype: str
        """
        return self._option_id

    @option_id.setter
    def option_id(self, option_id: str):
        """Sets the option_id of this Body18.


        :param option_id: The option_id of this Body18.
        :type option_id: str
        """

        self._option_id = option_id

    @property
    def plan_category_id(self) -> str:
        """Gets the plan_category_id of this Body18.


        :return: The plan_category_id of this Body18.
        :rtype: str
        """
        return self._plan_category_id

    @plan_category_id.setter
    def plan_category_id(self, plan_category_id: str):
        """Sets the plan_category_id of this Body18.


        :param plan_category_id: The plan_category_id of this Body18.
        :type plan_category_id: str
        """

        self._plan_category_id = plan_category_id
