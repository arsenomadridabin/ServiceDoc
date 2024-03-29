# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body22(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, session_id: str=None, amount: int=None, month: str=None, package: str=None):  # noqa: E501
        """Body22 - a model defined in Swagger

        :param token: The token of this Body22.  # noqa: E501
        :type token: str
        :param session_id: The session_id of this Body22.  # noqa: E501
        :type session_id: str
        :param amount: The amount of this Body22.  # noqa: E501
        :type amount: int
        :param month: The month of this Body22.  # noqa: E501
        :type month: str
        :param package: The package of this Body22.  # noqa: E501
        :type package: str
        """
        self.swagger_types = {
            'token': str,
            'session_id': str,
            'amount': int,
            'month': str,
            'package': str
        }

        self.attribute_map = {
            'token': 'token',
            'session_id': 'session_id',
            'amount': 'amount',
            'month': 'month',
            'package': 'package'
        }
        self._token = token
        self._session_id = session_id
        self._amount = amount
        self._month = month
        self._package = package

    @classmethod
    def from_dict(cls, dikt) -> 'Body22':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_22 of this Body22.  # noqa: E501
        :rtype: Body22
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body22.


        :return: The token of this Body22.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body22.


        :param token: The token of this Body22.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def session_id(self) -> str:
        """Gets the session_id of this Body22.


        :return: The session_id of this Body22.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str):
        """Sets the session_id of this Body22.


        :param session_id: The session_id of this Body22.
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def amount(self) -> int:
        """Gets the amount of this Body22.


        :return: The amount of this Body22.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Body22.


        :param amount: The amount of this Body22.
        :type amount: int
        """

        self._amount = amount

    @property
    def month(self) -> str:
        """Gets the month of this Body22.


        :return: The month of this Body22.
        :rtype: str
        """
        return self._month

    @month.setter
    def month(self, month: str):
        """Sets the month of this Body22.


        :param month: The month of this Body22.
        :type month: str
        """

        self._month = month

    @property
    def package(self) -> str:
        """Gets the package of this Body22.


        :return: The package of this Body22.
        :rtype: str
        """
        return self._package

    @package.setter
    def package(self, package: str):
        """Sets the package of this Body22.


        :param package: The package of this Body22.
        :type package: str
        """

        self._package = package
