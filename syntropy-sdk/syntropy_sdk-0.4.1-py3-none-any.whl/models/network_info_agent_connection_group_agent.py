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


class NetworkInfoAgentConnectionGroupAgent(object):
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
    swagger_types = {"agent_id": "int", "agent_is_virtual": "bool"}

    attribute_map = {"agent_id": "agent_id", "agent_is_virtual": "agent_is_virtual"}

    def __init__(self, agent_id=None, agent_is_virtual=None):  # noqa: E501
        """NetworkInfoAgentConnectionGroupAgent - a model defined in Swagger"""  # noqa: E501
        self._agent_id = None
        self._agent_is_virtual = None
        self.discriminator = None
        self.agent_id = agent_id
        self.agent_is_virtual = agent_is_virtual

    @property
    def agent_id(self):
        """Gets the agent_id of this NetworkInfoAgentConnectionGroupAgent.  # noqa: E501


        :return: The agent_id of this NetworkInfoAgentConnectionGroupAgent.  # noqa: E501
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """Sets the agent_id of this NetworkInfoAgentConnectionGroupAgent.


        :param agent_id: The agent_id of this NetworkInfoAgentConnectionGroupAgent.  # noqa: E501
        :type: int
        """
        if agent_id is None:
            raise ValueError(
                "Invalid value for `agent_id`, must not be `None`"
            )  # noqa: E501

        self._agent_id = agent_id

    @property
    def agent_is_virtual(self):
        """Gets the agent_is_virtual of this NetworkInfoAgentConnectionGroupAgent.  # noqa: E501


        :return: The agent_is_virtual of this NetworkInfoAgentConnectionGroupAgent.  # noqa: E501
        :rtype: bool
        """
        return self._agent_is_virtual

    @agent_is_virtual.setter
    def agent_is_virtual(self, agent_is_virtual):
        """Sets the agent_is_virtual of this NetworkInfoAgentConnectionGroupAgent.


        :param agent_is_virtual: The agent_is_virtual of this NetworkInfoAgentConnectionGroupAgent.  # noqa: E501
        :type: bool
        """
        if agent_is_virtual is None:
            raise ValueError(
                "Invalid value for `agent_is_virtual`, must not be `None`"
            )  # noqa: E501

        self._agent_is_virtual = agent_is_virtual

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
        if issubclass(NetworkInfoAgentConnectionGroupAgent, dict):
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
        if not isinstance(other, NetworkInfoAgentConnectionGroupAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
