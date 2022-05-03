# coding: utf-8

"""
    Syntropy network API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@syntropynet.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class V1NetworkAgentsLogsErrorsSearchRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"_from": "datetime", "agent_ids": "list[IdNumber]", "size": "int"}

    attribute_map = {"_from": "from", "agent_ids": "agent_ids", "size": "size"}

    def __init__(self, _from=None, agent_ids=None, size=None):  # noqa: E501
        """V1NetworkAgentsLogsErrorsSearchRequest - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._agent_ids = None
        self._size = None
        self.discriminator = None
        self._from = _from
        if agent_ids is not None:
            self.agent_ids = agent_ids
        if size is not None:
            self.size = size

    @property
    def _from(self):
        """Gets the _from of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501


        :return: The _from of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this V1NetworkAgentsLogsErrorsSearchRequest.


        :param _from: The _from of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501
        :type: datetime
        """
        if _from is None:
            raise ValueError(
                "Invalid value for `_from`, must not be `None`"
            )  # noqa: E501

        self.__from = _from

    @property
    def agent_ids(self):
        """Gets the agent_ids of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501


        :return: The agent_ids of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501
        :rtype: list[IdNumber]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """Sets the agent_ids of this V1NetworkAgentsLogsErrorsSearchRequest.


        :param agent_ids: The agent_ids of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501
        :type: list[IdNumber]
        """

        self._agent_ids = agent_ids

    @property
    def size(self):
        """Gets the size of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501


        :return: The size of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this V1NetworkAgentsLogsErrorsSearchRequest.


        :param size: The size of this V1NetworkAgentsLogsErrorsSearchRequest.  # noqa: E501
        :type: int
        """

        self._size = size

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(V1NetworkAgentsLogsErrorsSearchRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1NetworkAgentsLogsErrorsSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
