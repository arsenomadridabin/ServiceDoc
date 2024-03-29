# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse4001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sc_no: str=None, consumer_id: str=None, office_code: str=None):  # noqa: E501
        """InlineResponse4001 - a model defined in Swagger

        :param sc_no: The sc_no of this InlineResponse4001.  # noqa: E501
        :type sc_no: str
        :param consumer_id: The consumer_id of this InlineResponse4001.  # noqa: E501
        :type consumer_id: str
        :param office_code: The office_code of this InlineResponse4001.  # noqa: E501
        :type office_code: str
        """
        self.swagger_types = {
            'sc_no': str,
            'consumer_id': str,
            'office_code': str
        }

        self.attribute_map = {
            'sc_no': 'sc_no',
            'consumer_id': 'consumer_id',
            'office_code': 'office_code'
        }
        self._sc_no = sc_no
        self._consumer_id = consumer_id
        self._office_code = office_code

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse4001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_400_1 of this InlineResponse4001.  # noqa: E501
        :rtype: InlineResponse4001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sc_no(self) -> str:
        """Gets the sc_no of this InlineResponse4001.


        :return: The sc_no of this InlineResponse4001.
        :rtype: str
        """
        return self._sc_no

    @sc_no.setter
    def sc_no(self, sc_no: str):
        """Sets the sc_no of this InlineResponse4001.


        :param sc_no: The sc_no of this InlineResponse4001.
        :type sc_no: str
        """

        self._sc_no = sc_no

    @property
    def consumer_id(self) -> str:
        """Gets the consumer_id of this InlineResponse4001.


        :return: The consumer_id of this InlineResponse4001.
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id: str):
        """Sets the consumer_id of this InlineResponse4001.


        :param consumer_id: The consumer_id of this InlineResponse4001.
        :type consumer_id: str
        """

        self._consumer_id = consumer_id

    @property
    def office_code(self) -> str:
        """Gets the office_code of this InlineResponse4001.


        :return: The office_code of this InlineResponse4001.
        :rtype: str
        """
        return self._office_code

    @office_code.setter
    def office_code(self, office_code: str):
        """Sets the office_code of this InlineResponse4001.


        :param office_code: The office_code of this InlineResponse4001.
        :type office_code: str
        """

        self._office_code = office_code
