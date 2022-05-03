# coding: utf-8

"""
    Deci Platform API

    Train, deploy, optimize and serve your models using Deci's platform, In your cloud or on premise.  # noqa: E501

    The version of the OpenAPI document: 1.19.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from deci_lab_client.configuration import Configuration


class APIResponseListInfraDataTypesEnumModelsEnumsMetric(object):
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
        'success': 'bool',
        'message': 'str',
        'data': 'list[Metric]'
    }

    attribute_map = {
        'success': 'success',
        'message': 'message',
        'data': 'data'
    }

    def __init__(self, success=None, message=None, data=None, local_vars_configuration=None):  # noqa: E501
        """APIResponseListInfraDataTypesEnumModelsEnumsMetric - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._message = None
        self._data = None
        self.discriminator = None

        self.success = success
        self.message = message
        if data is not None:
            self.data = data

    @property
    def success(self):
        """Gets the success of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501


        :return: The success of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.


        :param success: The success of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def message(self):
        """Gets the message of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501


        :return: The message of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.


        :param message: The message of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def data(self):
        """Gets the data of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501


        :return: The data of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501
        :rtype: list[Metric]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.


        :param data: The data of this APIResponseListInfraDataTypesEnumModelsEnumsMetric.  # noqa: E501
        :type: list[Metric]
        """

        self._data = data

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
        if not isinstance(other, APIResponseListInfraDataTypesEnumModelsEnumsMetric):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, APIResponseListInfraDataTypesEnumModelsEnumsMetric):
            return True

        return self.to_dict() != other.to_dict()
