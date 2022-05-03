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


class V1NetworkConnectionsCreateMeshRequest(object):
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
        "agent_ids": "list[V1NetworkConnectionsCreateMeshRequestAgentIds]",
        "sdn_enabled": "bool",
        "sdn_paths": "V1SdnPaths",
    }

    attribute_map = {
        "agent_ids": "agent_ids",
        "sdn_enabled": "sdn_enabled",
        "sdn_paths": "sdn_paths",
    }

    def __init__(self, agent_ids=None, sdn_enabled=None, sdn_paths=None):  # noqa: E501
        """V1NetworkConnectionsCreateMeshRequest - a model defined in Swagger"""  # noqa: E501
        self._agent_ids = None
        self._sdn_enabled = None
        self._sdn_paths = None
        self.discriminator = None
        self.agent_ids = agent_ids
        if sdn_enabled is not None:
            self.sdn_enabled = sdn_enabled
        if sdn_paths is not None:
            self.sdn_paths = sdn_paths

    @property
    def agent_ids(self):
        """Gets the agent_ids of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501


        :return: The agent_ids of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501
        :rtype: list[V1NetworkConnectionsCreateMeshRequestAgentIds]
        """
        return self._agent_ids

    @agent_ids.setter
    def agent_ids(self, agent_ids):
        """Sets the agent_ids of this V1NetworkConnectionsCreateMeshRequest.


        :param agent_ids: The agent_ids of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501
        :type: list[V1NetworkConnectionsCreateMeshRequestAgentIds]
        """
        if agent_ids is None:
            raise ValueError(
                "Invalid value for `agent_ids`, must not be `None`"
            )  # noqa: E501

        self._agent_ids = agent_ids

    @property
    def sdn_enabled(self):
        """Gets the sdn_enabled of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501


        :return: The sdn_enabled of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501
        :rtype: bool
        """
        return self._sdn_enabled

    @sdn_enabled.setter
    def sdn_enabled(self, sdn_enabled):
        """Sets the sdn_enabled of this V1NetworkConnectionsCreateMeshRequest.


        :param sdn_enabled: The sdn_enabled of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501
        :type: bool
        """

        self._sdn_enabled = sdn_enabled

    @property
    def sdn_paths(self):
        """Gets the sdn_paths of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501


        :return: The sdn_paths of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501
        :rtype: V1SdnPaths
        """
        return self._sdn_paths

    @sdn_paths.setter
    def sdn_paths(self, sdn_paths):
        """Sets the sdn_paths of this V1NetworkConnectionsCreateMeshRequest.


        :param sdn_paths: The sdn_paths of this V1NetworkConnectionsCreateMeshRequest.  # noqa: E501
        :type: V1SdnPaths
        """

        self._sdn_paths = sdn_paths

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
        if issubclass(V1NetworkConnectionsCreateMeshRequest, dict):
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
        if not isinstance(other, V1NetworkConnectionsCreateMeshRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
