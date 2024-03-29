# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body2(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, number: str=None, customer_id: str=None, amount: int=None, reference: str=None):  # noqa: E501
        """Body2 - a model defined in Swagger

        :param token: The token of this Body2.  # noqa: E501
        :type token: str
        :param number: The number of this Body2.  # noqa: E501
        :type number: str
        :param customer_id: The customer_id of this Body2.  # noqa: E501
        :type customer_id: str
        :param amount: The amount of this Body2.  # noqa: E501
        :type amount: int
        :param reference: The reference of this Body2.  # noqa: E501
        :type reference: str
        """
        self.swagger_types = {
            'token': str,
            'number': str,
            'customer_id': str,
            'amount': int,
            'reference': str
        }

        self.attribute_map = {
            'token': 'token',
            'number': 'number',
            'customer_id': 'customer_id',
            'amount': 'amount',
            'reference': 'reference'
        }
        self._token = token
        self._number = number
        self._customer_id = customer_id
        self._amount = amount
        self._reference = reference

    @classmethod
    def from_dict(cls, dikt) -> 'Body2':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_2 of this Body2.  # noqa: E501
        :rtype: Body2
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body2.


        :return: The token of this Body2.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body2.


        :param token: The token of this Body2.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def number(self) -> str:
        """Gets the number of this Body2.


        :return: The number of this Body2.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number: str):
        """Sets the number of this Body2.


        :param number: The number of this Body2.
        :type number: str
        """

        self._number = number

    @property
    def customer_id(self) -> str:
        """Gets the customer_id of this Body2.


        :return: The customer_id of this Body2.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id: str):
        """Sets the customer_id of this Body2.


        :param customer_id: The customer_id of this Body2.
        :type customer_id: str
        """

        self._customer_id = customer_id

    @property
    def amount(self) -> int:
        """Gets the amount of this Body2.


        :return: The amount of this Body2.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Body2.


        :param amount: The amount of this Body2.
        :type amount: int
        """

        self._amount = amount

    @property
    def reference(self) -> str:
        """Gets the reference of this Body2.


        :return: The reference of this Body2.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Body2.


        :param reference: The reference of this Body2.
        :type reference: str
        """

        self._reference = reference
