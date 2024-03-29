# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body13(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, token: str=None, month_id: str=None, customer_code: str=None, counter: str=None, reference: str=None):  # noqa: E501
        """Body13 - a model defined in Swagger

        :param token: The token of this Body13.  # noqa: E501
        :type token: str
        :param month_id: The month_id of this Body13.  # noqa: E501
        :type month_id: str
        :param customer_code: The customer_code of this Body13.  # noqa: E501
        :type customer_code: str
        :param counter: The counter of this Body13.  # noqa: E501
        :type counter: str
        :param reference: The reference of this Body13.  # noqa: E501
        :type reference: str
        """
        self.swagger_types = {
            'token': str,
            'month_id': str,
            'customer_code': str,
            'counter': str,
            'reference': str
        }

        self.attribute_map = {
            'token': 'token',
            'month_id': 'month_id',
            'customer_code': 'customer_code',
            'counter': 'counter',
            'reference': 'reference'
        }
        self._token = token
        self._month_id = month_id
        self._customer_code = customer_code
        self._counter = counter
        self._reference = reference

    @classmethod
    def from_dict(cls, dikt) -> 'Body13':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_13 of this Body13.  # noqa: E501
        :rtype: Body13
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this Body13.


        :return: The token of this Body13.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this Body13.


        :param token: The token of this Body13.
        :type token: str
        """
        if token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def month_id(self) -> str:
        """Gets the month_id of this Body13.


        :return: The month_id of this Body13.
        :rtype: str
        """
        return self._month_id

    @month_id.setter
    def month_id(self, month_id: str):
        """Sets the month_id of this Body13.


        :param month_id: The month_id of this Body13.
        :type month_id: str
        """

        self._month_id = month_id

    @property
    def customer_code(self) -> str:
        """Gets the customer_code of this Body13.


        :return: The customer_code of this Body13.
        :rtype: str
        """
        return self._customer_code

    @customer_code.setter
    def customer_code(self, customer_code: str):
        """Sets the customer_code of this Body13.


        :param customer_code: The customer_code of this Body13.
        :type customer_code: str
        """

        self._customer_code = customer_code

    @property
    def counter(self) -> str:
        """Gets the counter of this Body13.


        :return: The counter of this Body13.
        :rtype: str
        """
        return self._counter

    @counter.setter
    def counter(self, counter: str):
        """Sets the counter of this Body13.


        :param counter: The counter of this Body13.
        :type counter: str
        """

        self._counter = counter

    @property
    def reference(self) -> str:
        """Gets the reference of this Body13.


        :return: The reference of this Body13.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference: str):
        """Sets the reference of this Body13.


        :param reference: The reference of this Body13.
        :type reference: str
        """

        self._reference = reference
