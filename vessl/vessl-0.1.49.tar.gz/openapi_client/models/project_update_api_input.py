# coding: utf-8

"""
    Aron API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from openapi_client.configuration import Configuration


class ProjectUpdateAPIInput(object):
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
        'description': 'str',
        'key_metrics': 'OrmKeyMetrics',
        'note': 'str'
    }

    attribute_map = {
        'description': 'description',
        'key_metrics': 'key_metrics',
        'note': 'note'
    }

    def __init__(self, description=None, key_metrics=None, note=None, local_vars_configuration=None):  # noqa: E501
        """ProjectUpdateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._key_metrics = None
        self._note = None
        self.discriminator = None

        self.description = description
        if key_metrics is not None:
            self.key_metrics = key_metrics
        self.note = note

    @property
    def description(self):
        """Gets the description of this ProjectUpdateAPIInput.  # noqa: E501


        :return: The description of this ProjectUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectUpdateAPIInput.


        :param description: The description of this ProjectUpdateAPIInput.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def key_metrics(self):
        """Gets the key_metrics of this ProjectUpdateAPIInput.  # noqa: E501


        :return: The key_metrics of this ProjectUpdateAPIInput.  # noqa: E501
        :rtype: OrmKeyMetrics
        """
        return self._key_metrics

    @key_metrics.setter
    def key_metrics(self, key_metrics):
        """Sets the key_metrics of this ProjectUpdateAPIInput.


        :param key_metrics: The key_metrics of this ProjectUpdateAPIInput.  # noqa: E501
        :type key_metrics: OrmKeyMetrics
        """

        self._key_metrics = key_metrics

    @property
    def note(self):
        """Gets the note of this ProjectUpdateAPIInput.  # noqa: E501


        :return: The note of this ProjectUpdateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this ProjectUpdateAPIInput.


        :param note: The note of this ProjectUpdateAPIInput.  # noqa: E501
        :type note: str
        """

        self._note = note

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ProjectUpdateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectUpdateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
