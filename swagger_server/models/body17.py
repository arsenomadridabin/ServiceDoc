# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body17(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, username: str=None, reference: str=None):  # noqa: E501
        """Body17 - a model defined in Swagger

        :param token: The token of this Body17.  # noqa: E501
        :type token: str
        :param username: The username of this Body17.  # noqa: E501
        :type username: str
        :param reference: The reference of this Body17.  # noqa: E501
        :type reference: str
        """
        self.swagger_types = {
            'token': str,
            'username': str,
            'reference': str
        }

        self.attribute_map = {
            'token': 'token',
            'username': 'username',
            'reference': 'reference'
        }
        self._token = token
        self._username = username
        self._reference = reference

    @classmethod
    def from_dict(cls, dikt) -> 'Body17':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_17 of this Body17.  # noqa: E501
        :rtype: Body17
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body17.


        :return: The token of this Body17.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body17.


        :param token: The token of this Body17.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def username(self) -> str:
        """Gets the username of this Body17.


        :return: The username of this Body17.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username: str):
        """Sets the username of this Body17.


        :param username: The username of this Body17.
        :type username: str
        """

        self._username = username

    @property
    def reference(self) -> str:
        """Gets the reference of this Body17.


        :return: The reference of this Body17.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Body17.


        :param reference: The reference of this Body17.
        :type reference: str
        """

        self._reference = reference