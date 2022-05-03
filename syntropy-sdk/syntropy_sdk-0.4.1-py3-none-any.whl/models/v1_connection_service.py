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


class V1ConnectionService(object):
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
    swagger_types = {
        "agent_connection_group_id": "int",
        "agent_connection_subnets": "list[V1ConnectionServiceSubnet]",
        "agent_2": "V1ConnectionServiceAgent",
        "agent_1": "V1ConnectionServiceAgent",
    }

    attribute_map = {
        "agent_connection_group_id": "agent_connection_group_id",
        "agent_connection_subnets": "agent_connection_subnets",
        "agent_2": "agent_2",
        "agent_1": "agent_1",
    }

    def __init__(
        self,
        agent_connection_group_id=None,
        agent_connection_subnets=None,
        agent_2=None,
        agent_1=None,
    ):  # noqa: E501
        """V1ConnectionService - a model defined in Swagger"""  # noqa: E501
        self._agent_connection_group_id = None
        self._agent_connection_subnets = None
        self._agent_2 = None
        self._agent_1 = None
        self.discriminator = None
        self.agent_connection_group_id = agent_connection_group_id
        self.agent_connection_subnets = agent_connection_subnets
        self.agent_2 = agent_2
        self.agent_1 = agent_1

    @property
    def agent_connection_group_id(self):
        """Gets the agent_connection_group_id of this V1ConnectionService.  # noqa: E501


        :return: The agent_connection_group_id of this V1ConnectionService.  # noqa: E501
        :rtype: int
        """
        return self._agent_connection_group_id

    @agent_connection_group_id.setter
    def agent_connection_group_id(self, agent_connection_group_id):
        """Sets the agent_connection_group_id of this V1ConnectionService.


        :param agent_connection_group_id: The agent_connection_group_id of this V1ConnectionService.  # noqa: E501
        :type: int
        """
        if agent_connection_group_id is None:
            raise ValueError(
                "Invalid value for `agent_connection_group_id`, must not be `None`"
            )  # noqa: E501

        self._agent_connection_group_id = agent_connection_group_id

    @property
    def agent_connection_subnets(self):
        """Gets the agent_connection_subnets of this V1ConnectionService.  # noqa: E501


        :return: The agent_connection_subnets of this V1ConnectionService.  # noqa: E501
        :rtype: list[V1ConnectionServiceSubnet]
        """
        return self._agent_connection_subnets

    @agent_connection_subnets.setter
    def agent_connection_subnets(self, agent_connection_subnets):
        """Sets the agent_connection_subnets of this V1ConnectionService.


        :param agent_connection_subnets: The agent_connection_subnets of this V1ConnectionService.  # noqa: E501
        :type: list[V1ConnectionServiceSubnet]
        """
        if agent_connection_subnets is None:
            raise ValueError(
                "Invalid value for `agent_connection_subnets`, must not be `None`"
            )  # noqa: E501

        self._agent_connection_subnets = agent_connection_subnets

    @property
    def agent_2(self):
        """Gets the agent_2 of this V1ConnectionService.  # noqa: E501


        :return: The agent_2 of this V1ConnectionService.  # noqa: E501
        :rtype: V1ConnectionServiceAgent
        """
        return self._agent_2

    @agent_2.setter
    def agent_2(self, agent_2):
        """Sets the agent_2 of this V1ConnectionService.


        :param agent_2: The agent_2 of this V1ConnectionService.  # noqa: E501
        :type: V1ConnectionServiceAgent
        """
        if agent_2 is None:
            raise ValueError(
                "Invalid value for `agent_2`, must not be `None`"
            )  # noqa: E501

        self._agent_2 = agent_2

    @property
    def agent_1(self):
        """Gets the agent_1 of this V1ConnectionService.  # noqa: E501


        :return: The agent_1 of this V1ConnectionService.  # noqa: E501
        :rtype: V1ConnectionServiceAgent
        """
        return self._agent_1

    @agent_1.setter
    def agent_1(self, agent_1):
        """Sets the agent_1 of this V1ConnectionService.


        :param agent_1: The agent_1 of this V1ConnectionService.  # noqa: E501
        :type: V1ConnectionServiceAgent
        """
        if agent_1 is None:
            raise ValueError(
                "Invalid value for `agent_1`, must not be `None`"
            )  # noqa: E501

        self._agent_1 = agent_1

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
        if issubclass(V1ConnectionService, dict):
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
        if not isinstance(other, V1ConnectionService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
