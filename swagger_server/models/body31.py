# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body31(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, session_id: str=None, package_code: str=None):  # noqa: E501
        """Body31 - a model defined in Swagger

        :param token: The token of this Body31.  # noqa: E501
        :type token: str
        :param session_id: The session_id of this Body31.  # noqa: E501
        :type session_id: str
        :param package_code: The package_code of this Body31.  # noqa: E501
        :type package_code: str
        """
        self.swagger_types = {
            'token': str,
            'session_id': str,
            'package_code': str
        }

        self.attribute_map = {
            'token': 'token',
            'session_id': 'session_id',
            'package_code': 'package_code'
        }
        self._token = token
        self._session_id = session_id
        self._package_code = package_code

    @classmethod
    def from_dict(cls, dikt) -> 'Body31':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_31 of this Body31.  # noqa: E501
        :rtype: Body31
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body31.


        :return: The token of this Body31.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body31.


        :param token: The token of this Body31.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def session_id(self) -> str:
        """Gets the session_id of this Body31.


        :return: The session_id of this Body31.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str):
        """Sets the session_id of this Body31.


        :param session_id: The session_id of this Body31.
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def package_code(self) -> str:
        """Gets the package_code of this Body31.


        :return: The package_code of this Body31.
        :rtype: str
        """
        return self._package_code

    @package_code.setter
    def package_code(self, package_code: str):
        """Sets the package_code of this Body31.


        :param package_code: The package_code of this Body31.
        :type package_code: str
        """

        self._package_code = package_code
