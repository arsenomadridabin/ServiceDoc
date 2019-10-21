# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body52(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, session_id: str=None):  # noqa: E501
        """Body52 - a model defined in Swagger

        :param token: The token of this Body52.  # noqa: E501
        :type token: str
        :param session_id: The session_id of this Body52.  # noqa: E501
        :type session_id: str
        """
        self.swagger_types = {
            'token': str,
            'session_id': str
        }

        self.attribute_map = {
            'token': 'token',
            'session_id': 'session_id'
        }
        self._token = token
        self._session_id = session_id

    @classmethod
    def from_dict(cls, dikt) -> 'Body52':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_52 of this Body52.  # noqa: E501
        :rtype: Body52
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body52.


        :return: The token of this Body52.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body52.


        :param token: The token of this Body52.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def session_id(self) -> str:
        """Gets the session_id of this Body52.


        :return: The session_id of this Body52.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id: str):
        """Sets the session_id of this Body52.


        :param session_id: The session_id of this Body52.
        :type session_id: str
        """

        self._session_id = session_id