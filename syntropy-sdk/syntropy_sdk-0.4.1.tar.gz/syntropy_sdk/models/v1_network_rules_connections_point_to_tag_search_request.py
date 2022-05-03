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


class V1NetworkRulesConnectionsPointToTagSearchRequest(object):
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
    swagger_types = {"filter": "V1RulesPointToTagFilter"}

    attribute_map = {"filter": "filter"}

    def __init__(self, filter=None):  # noqa: E501
        """V1NetworkRulesConnectionsPointToTagSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._filter = None
        self.discriminator = None
        if filter is not None:
            self.filter = filter

    @property
    def filter(self):
        """Gets the filter of this V1NetworkRulesConnectionsPointToTagSearchRequest.  # noqa: E501


        :return: The filter of this V1NetworkRulesConnectionsPointToTagSearchRequest.  # noqa: E501
        :rtype: V1RulesPointToTagFilter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this V1NetworkRulesConnectionsPointToTagSearchRequest.


        :param filter: The filter of this V1NetworkRulesConnectionsPointToTagSearchRequest.  # noqa: E501
        :type: V1RulesPointToTagFilter
        """

        self._filter = filter

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
        if issubclass(V1NetworkRulesConnectionsPointToTagSearchRequest, dict):
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
        if not isinstance(other, V1NetworkRulesConnectionsPointToTagSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
