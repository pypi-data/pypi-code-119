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


class V1NetworkAStatusesSearchRequestFilter(object):
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
    swagger_types = {"agent_pairs": "list[V1AAgentPair]"}

    attribute_map = {"agent_pairs": "agent_pairs"}

    def __init__(self, agent_pairs=None):  # noqa: E501
        """V1NetworkAStatusesSearchRequestFilter - a model defined in Swagger"""  # noqa: E501
        self._agent_pairs = None
        self.discriminator = None
        self.agent_pairs = agent_pairs

    @property
    def agent_pairs(self):
        """Gets the agent_pairs of this V1NetworkAStatusesSearchRequestFilter.  # noqa: E501


        :return: The agent_pairs of this V1NetworkAStatusesSearchRequestFilter.  # noqa: E501
        :rtype: list[V1AAgentPair]
        """
        return self._agent_pairs

    @agent_pairs.setter
    def agent_pairs(self, agent_pairs):
        """Sets the agent_pairs of this V1NetworkAStatusesSearchRequestFilter.


        :param agent_pairs: The agent_pairs of this V1NetworkAStatusesSearchRequestFilter.  # noqa: E501
        :type: list[V1AAgentPair]
        """
        if agent_pairs is None:
            raise ValueError(
                "Invalid value for `agent_pairs`, must not be `None`"
            )  # noqa: E501

        self._agent_pairs = agent_pairs

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
        if issubclass(V1NetworkAStatusesSearchRequestFilter, dict):
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
        if not isinstance(other, V1NetworkAStatusesSearchRequestFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
