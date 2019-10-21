# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body35(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, debit_note_no: str=None, reference: str=None):  # noqa: E501
        """Body35 - a model defined in Swagger

        :param token: The token of this Body35.  # noqa: E501
        :type token: str
        :param debit_note_no: The debit_note_no of this Body35.  # noqa: E501
        :type debit_note_no: str
        :param reference: The reference of this Body35.  # noqa: E501
        :type reference: str
        """
        self.swagger_types = {
            'token': str,
            'debit_note_no': str,
            'reference': str
        }

        self.attribute_map = {
            'token': 'token',
            'debit_note_no': 'debit_note_no',
            'reference': 'reference'
        }
        self._token = token
        self._debit_note_no = debit_note_no
        self._reference = reference

    @classmethod
    def from_dict(cls, dikt) -> 'Body35':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_35 of this Body35.  # noqa: E501
        :rtype: Body35
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body35.


        :return: The token of this Body35.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body35.


        :param token: The token of this Body35.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def debit_note_no(self) -> str:
        """Gets the debit_note_no of this Body35.


        :return: The debit_note_no of this Body35.
        :rtype: str
        """
        return self._debit_note_no

    @debit_note_no.setter
    def debit_note_no(self, debit_note_no: str):
        """Sets the debit_note_no of this Body35.


        :param debit_note_no: The debit_note_no of this Body35.
        :type debit_note_no: str
        """

        self._debit_note_no = debit_note_no

    @property
    def reference(self) -> str:
        """Gets the reference of this Body35.


        :return: The reference of this Body35.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Body35.


        :param reference: The reference of this Body35.
        :type reference: str
        """

        self._reference = reference