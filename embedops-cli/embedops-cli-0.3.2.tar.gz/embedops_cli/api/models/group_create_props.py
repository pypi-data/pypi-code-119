# coding: utf-8

"""
    EmbedOps API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@embedops.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class GroupCreateProps(object):
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
    swagger_types = {"name": "str", "org_perm": "str"}

    attribute_map = {"name": "name", "org_perm": "orgPerm"}

    def __init__(self, name=None, org_perm=None):  # noqa: E501
        """GroupCreateProps - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._org_perm = None
        self.discriminator = None
        self.name = name
        self.org_perm = org_perm

    @property
    def name(self):
        """Gets the name of this GroupCreateProps.  # noqa: E501


        :return: The name of this GroupCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GroupCreateProps.


        :param name: The name of this GroupCreateProps.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError(
                "Invalid value for `name`, must not be `None`"
            )  # noqa: E501

        self._name = name

    @property
    def org_perm(self):
        """Gets the org_perm of this GroupCreateProps.  # noqa: E501


        :return: The org_perm of this GroupCreateProps.  # noqa: E501
        :rtype: str
        """
        return self._org_perm

    @org_perm.setter
    def org_perm(self, org_perm):
        """Sets the org_perm of this GroupCreateProps.


        :param org_perm: The org_perm of this GroupCreateProps.  # noqa: E501
        :type: str
        """
        if org_perm is None:
            raise ValueError(
                "Invalid value for `org_perm`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["admin", "read", "update"]  # noqa: E501
        if org_perm not in allowed_values:
            raise ValueError(
                "Invalid value for `org_perm` ({0}), must be one of {1}".format(  # noqa: E501
                    org_perm, allowed_values
                )
            )

        self._org_perm = org_perm

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
        if issubclass(GroupCreateProps, dict):
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
        if not isinstance(other, GroupCreateProps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
