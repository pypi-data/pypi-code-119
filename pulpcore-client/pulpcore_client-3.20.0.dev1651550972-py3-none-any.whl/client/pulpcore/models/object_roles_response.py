# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulpcore.configuration import Configuration


class ObjectRolesResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'roles': 'list[NestedRoleResponse]'
    }

    attribute_map = {
        'roles': 'roles'
    }

    def __init__(self, roles=None, local_vars_configuration=None):  # noqa: E501
        """ObjectRolesResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._roles = None
        self.discriminator = None

        self.roles = roles

    @property
    def roles(self):
        """Gets the roles of this ObjectRolesResponse.  # noqa: E501


        :return: The roles of this ObjectRolesResponse.  # noqa: E501
        :rtype: list[NestedRoleResponse]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this ObjectRolesResponse.


        :param roles: The roles of this ObjectRolesResponse.  # noqa: E501
        :type: list[NestedRoleResponse]
        """
        if self.local_vars_configuration.client_side_validation and roles is None:  # noqa: E501
            raise ValueError("Invalid value for `roles`, must not be `None`")  # noqa: E501

        self._roles = roles

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObjectRolesResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectRolesResponse):
            return True

        return self.to_dict() != other.to_dict()
