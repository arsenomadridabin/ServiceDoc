# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, reference: str=None, amount: int=None):  # noqa: E501
        """Body - a model defined in Swagger

        :param token: The token of this Body.  # noqa: E501
        :type token: str
        :param reference: The reference of this Body.  # noqa: E501
        :type reference: str
        :param amount: The amount of this Body.  # noqa: E501
        :type amount: int
        """
        self.swagger_types = {
            'token': str,
            'reference': str,
            'amount': int
        }

        self.attribute_map = {
            'token': 'token',
            'reference': 'reference',
            'amount': 'amount'
        }
        self._token = token
        self._reference = reference
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'Body':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body of this Body.  # noqa: E501
        :rtype: Body
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body.


        :return: The token of this Body.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body.


        :param token: The token of this Body.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def reference(self) -> str:
        """Gets the reference of this Body.


        :return: The reference of this Body.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Body.


        :param reference: The reference of this Body.
        :type reference: str
        """

        self._reference = reference

    @property
    def amount(self) -> int:
        """Gets the amount of this Body.


        :return: The amount of this Body.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Body.


        :param amount: The amount of this Body.
        :type amount: int
        """

        self._amount = amount
