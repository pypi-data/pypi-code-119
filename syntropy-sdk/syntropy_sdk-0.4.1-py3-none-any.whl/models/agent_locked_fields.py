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


class AgentLockedFields(object):
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
        "agent_location_country": "bool",
        "agent_location_city": "bool",
        "agent_location_lat": "bool",
        "agent_location_lon": "bool",
        "agent_provider_name": "bool",
        "agent_tags": "list[str]",
        "agent_name": "bool",
    }

    attribute_map = {
        "agent_location_country": "agent_location_country",
        "agent_location_city": "agent_location_city",
        "agent_location_lat": "agent_location_lat",
        "agent_location_lon": "agent_location_lon",
        "agent_provider_name": "agent_provider_name",
        "agent_tags": "agent_tags",
        "agent_name": "agent_name",
    }

    def __init__(
        self,
        agent_location_country=None,
        agent_location_city=None,
        agent_location_lat=None,
        agent_location_lon=None,
        agent_provider_name=None,
        agent_tags=None,
        agent_name=None,
    ):  # noqa: E501
        """AgentLockedFields - a model defined in Swagger"""  # noqa: E501
        self._agent_location_country = None
        self._agent_location_city = None
        self._agent_location_lat = None
        self._agent_location_lon = None
        self._agent_provider_name = None
        self._agent_tags = None
        self._agent_name = None
        self.discriminator = None
        if agent_location_country is not None:
            self.agent_location_country = agent_location_country
        if agent_location_city is not None:
            self.agent_location_city = agent_location_city
        if agent_location_lat is not None:
            self.agent_location_lat = agent_location_lat
        if agent_location_lon is not None:
            self.agent_location_lon = agent_location_lon
        if agent_provider_name is not None:
            self.agent_provider_name = agent_provider_name
        if agent_tags is not None:
            self.agent_tags = agent_tags
        if agent_name is not None:
            self.agent_name = agent_name

    @property
    def agent_location_country(self):
        """Gets the agent_location_country of this AgentLockedFields.  # noqa: E501


        :return: The agent_location_country of this AgentLockedFields.  # noqa: E501
        :rtype: bool
        """
        return self._agent_location_country

    @agent_location_country.setter
    def agent_location_country(self, agent_location_country):
        """Sets the agent_location_country of this AgentLockedFields.


        :param agent_location_country: The agent_location_country of this AgentLockedFields.  # noqa: E501
        :type: bool
        """

        self._agent_location_country = agent_location_country

    @property
    def agent_location_city(self):
        """Gets the agent_location_city of this AgentLockedFields.  # noqa: E501


        :return: The agent_location_city of this AgentLockedFields.  # noqa: E501
        :rtype: bool
        """
        return self._agent_location_city

    @agent_location_city.setter
    def agent_location_city(self, agent_location_city):
        """Sets the agent_location_city of this AgentLockedFields.


        :param agent_location_city: The agent_location_city of this AgentLockedFields.  # noqa: E501
        :type: bool
        """

        self._agent_location_city = agent_location_city

    @property
    def agent_location_lat(self):
        """Gets the agent_location_lat of this AgentLockedFields.  # noqa: E501


        :return: The agent_location_lat of this AgentLockedFields.  # noqa: E501
        :rtype: bool
        """
        return self._agent_location_lat

    @agent_location_lat.setter
    def agent_location_lat(self, agent_location_lat):
        """Sets the agent_location_lat of this AgentLockedFields.


        :param agent_location_lat: The agent_location_lat of this AgentLockedFields.  # noqa: E501
        :type: bool
        """

        self._agent_location_lat = agent_location_lat

    @property
    def agent_location_lon(self):
        """Gets the agent_location_lon of this AgentLockedFields.  # noqa: E501


        :return: The agent_location_lon of this AgentLockedFields.  # noqa: E501
        :rtype: bool
        """
        return self._agent_location_lon

    @agent_location_lon.setter
    def agent_location_lon(self, agent_location_lon):
        """Sets the agent_location_lon of this AgentLockedFields.


        :param agent_location_lon: The agent_location_lon of this AgentLockedFields.  # noqa: E501
        :type: bool
        """

        self._agent_location_lon = agent_location_lon

    @property
    def agent_provider_name(self):
        """Gets the agent_provider_name of this AgentLockedFields.  # noqa: E501


        :return: The agent_provider_name of this AgentLockedFields.  # noqa: E501
        :rtype: bool
        """
        return self._agent_provider_name

    @agent_provider_name.setter
    def agent_provider_name(self, agent_provider_name):
        """Sets the agent_provider_name of this AgentLockedFields.


        :param agent_provider_name: The agent_provider_name of this AgentLockedFields.  # noqa: E501
        :type: bool
        """

        self._agent_provider_name = agent_provider_name

    @property
    def agent_tags(self):
        """Gets the agent_tags of this AgentLockedFields.  # noqa: E501


        :return: The agent_tags of this AgentLockedFields.  # noqa: E501
        :rtype: list[str]
        """
        return self._agent_tags

    @agent_tags.setter
    def agent_tags(self, agent_tags):
        """Sets the agent_tags of this AgentLockedFields.


        :param agent_tags: The agent_tags of this AgentLockedFields.  # noqa: E501
        :type: list[str]
        """

        self._agent_tags = agent_tags

    @property
    def agent_name(self):
        """Gets the agent_name of this AgentLockedFields.  # noqa: E501


        :return: The agent_name of this AgentLockedFields.  # noqa: E501
        :rtype: bool
        """
        return self._agent_name

    @agent_name.setter
    def agent_name(self, agent_name):
        """Sets the agent_name of this AgentLockedFields.


        :param agent_name: The agent_name of this AgentLockedFields.  # noqa: E501
        :type: bool
        """

        self._agent_name = agent_name

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
        if issubclass(AgentLockedFields, dict):
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
        if not isinstance(other, AgentLockedFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
