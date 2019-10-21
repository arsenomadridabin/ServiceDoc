# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body16(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, package_id: str=None, session_id: str=None, amount: int=None):  # noqa: E501
        """Body16 - a model defined in Swagger

        :param token: The token of this Body16.  # noqa: E501
        :type token: str
        :param package_id: The package_id of this Body16.  # noqa: E501
        :type package_id: str
        :param session_id: The session_id of this Body16.  # noqa: E501
        :type session_id: str
        :param amount: The amount of this Body16.  # noqa: E501
        :type amount: int
        """
        self.swagger_types = {
            'token': str,
            'package_id': str,
            'session_id': str,
            'amount': int
        }

        self.attribute_map = {
            'token': 'token',
            'package_id': 'package_id',
            'session_id': 'session_id',
            'amount': 'amount'
        }
        self._token = token
        self._package_id = package_id
        self._session_id = session_id
        self._amount = amount

    @classmethod
    def from_dict(cls, dikt) -> 'Body16':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_16 of this Body16.  # noqa: E501
        :rtype: Body16
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body16.


        :return: The token of this Body16.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body16.


        :param token: The token of this Body16.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def package_id(self) -> str:
        """Gets the package_id of this Body16.


        :return: The package_id of this Body16.
        :rtype: str
        """
        return self._package_id

    @package_id.setter
    def package_id(self, package_id: str):
        """Sets the package_id of this Body16.


        :param package_id: The package_id of this Body16.
        :type package_id: str
        """

        self._package_id = package_id

    @property
    def session_id(self) -> str:
        """Gets the session_id of this Body16.


        :return: The session_id of this Body16.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str):
        """Sets the session_id of this Body16.


        :param session_id: The session_id of this Body16.
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def amount(self) -> int:
        """Gets the amount of this Body16.


        :return: The amount of this Body16.
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount: int):
        """Sets the amount of this Body16.


        :param amount: The amount of this Body16.
        :type amount: int
        """

        self._amount = amount