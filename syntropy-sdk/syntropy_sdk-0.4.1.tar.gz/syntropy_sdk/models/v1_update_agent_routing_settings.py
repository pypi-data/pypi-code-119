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


class V1UpdateAgentRoutingSettings(object):
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
        "rerouting_threshold": "V1UpdateAgentRoutingSettingsReroutingThreshold"
    }

    attribute_map = {"rerouting_threshold": "rerouting_threshold"}

    def __init__(self, rerouting_threshold=None):  # noqa: E501
        """V1UpdateAgentRoutingSettings - a model defined in Swagger"""  # noqa: E501
        self._rerouting_threshold = None
        self.discriminator = None
        self.rerouting_threshold = rerouting_threshold

    @property
    def rerouting_threshold(self):
        """Gets the rerouting_threshold of this V1UpdateAgentRoutingSettings.  # noqa: E501


        :return: The rerouting_threshold of this V1UpdateAgentRoutingSettings.  # noqa: E501
        :rtype: V1UpdateAgentRoutingSettingsReroutingThreshold
        """
        return self._rerouting_threshold

    @rerouting_threshold.setter
    def rerouting_threshold(self, rerouting_threshold):
        """Sets the rerouting_threshold of this V1UpdateAgentRoutingSettings.


        :param rerouting_threshold: The rerouting_threshold of this V1UpdateAgentRoutingSettings.  # noqa: E501
        :type: V1UpdateAgentRoutingSettingsReroutingThreshold
        """
        if rerouting_threshold is None:
            raise ValueError(
                "Invalid value for `rerouting_threshold`, must not be `None`"
            )  # noqa: E501

        self._rerouting_threshold = rerouting_threshold

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
        if issubclass(V1UpdateAgentRoutingSettings, dict):
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
        if not isinstance(other, V1UpdateAgentRoutingSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
