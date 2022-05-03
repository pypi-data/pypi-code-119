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


class V1AuthApiKey(object):
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
        "api_key_name": "str",
        "api_key_description": "str",
        "api_key_valid_until": "datetime",
        "api_key_status": "bool",
        "api_key_id": "int",
        "api_key_created_at": "datetime",
        "api_key_updated_at": "datetime",
    }

    attribute_map = {
        "api_key_name": "api_key_name",
        "api_key_description": "api_key_description",
        "api_key_valid_until": "api_key_valid_until",
        "api_key_status": "api_key_status",
        "api_key_id": "api_key_id",
        "api_key_created_at": "api_key_created_at",
        "api_key_updated_at": "api_key_updated_at",
    }

    def __init__(
        self,
        api_key_name=None,
        api_key_description=None,
        api_key_valid_until=None,
        api_key_status=None,
        api_key_id=None,
        api_key_created_at=None,
        api_key_updated_at=None,
    ):  # noqa: E501
        """V1AuthApiKey - a model defined in Swagger"""  # noqa: E501
        self._api_key_name = None
        self._api_key_description = None
        self._api_key_valid_until = None
        self._api_key_status = None
        self._api_key_id = None
        self._api_key_created_at = None
        self._api_key_updated_at = None
        self.discriminator = None
        self.api_key_name = api_key_name
        self.api_key_description = api_key_description
        self.api_key_valid_until = api_key_valid_until
        self.api_key_status = api_key_status
        self.api_key_id = api_key_id
        self.api_key_created_at = api_key_created_at
        self.api_key_updated_at = api_key_updated_at

    @property
    def api_key_name(self):
        """Gets the api_key_name of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_name of this V1AuthApiKey.  # noqa: E501
        :rtype: str
        """
        return self._api_key_name

    @api_key_name.setter
    def api_key_name(self, api_key_name):
        """Sets the api_key_name of this V1AuthApiKey.


        :param api_key_name: The api_key_name of this V1AuthApiKey.  # noqa: E501
        :type: str
        """
        if api_key_name is None:
            raise ValueError(
                "Invalid value for `api_key_name`, must not be `None`"
            )  # noqa: E501

        self._api_key_name = api_key_name

    @property
    def api_key_description(self):
        """Gets the api_key_description of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_description of this V1AuthApiKey.  # noqa: E501
        :rtype: str
        """
        return self._api_key_description

    @api_key_description.setter
    def api_key_description(self, api_key_description):
        """Sets the api_key_description of this V1AuthApiKey.


        :param api_key_description: The api_key_description of this V1AuthApiKey.  # noqa: E501
        :type: str
        """
        if api_key_description is None:
            raise ValueError(
                "Invalid value for `api_key_description`, must not be `None`"
            )  # noqa: E501

        self._api_key_description = api_key_description

    @property
    def api_key_valid_until(self):
        """Gets the api_key_valid_until of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_valid_until of this V1AuthApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._api_key_valid_until

    @api_key_valid_until.setter
    def api_key_valid_until(self, api_key_valid_until):
        """Sets the api_key_valid_until of this V1AuthApiKey.


        :param api_key_valid_until: The api_key_valid_until of this V1AuthApiKey.  # noqa: E501
        :type: datetime
        """
        if api_key_valid_until is None:
            raise ValueError(
                "Invalid value for `api_key_valid_until`, must not be `None`"
            )  # noqa: E501

        self._api_key_valid_until = api_key_valid_until

    @property
    def api_key_status(self):
        """Gets the api_key_status of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_status of this V1AuthApiKey.  # noqa: E501
        :rtype: bool
        """
        return self._api_key_status

    @api_key_status.setter
    def api_key_status(self, api_key_status):
        """Sets the api_key_status of this V1AuthApiKey.


        :param api_key_status: The api_key_status of this V1AuthApiKey.  # noqa: E501
        :type: bool
        """
        if api_key_status is None:
            raise ValueError(
                "Invalid value for `api_key_status`, must not be `None`"
            )  # noqa: E501

        self._api_key_status = api_key_status

    @property
    def api_key_id(self):
        """Gets the api_key_id of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_id of this V1AuthApiKey.  # noqa: E501
        :rtype: int
        """
        return self._api_key_id

    @api_key_id.setter
    def api_key_id(self, api_key_id):
        """Sets the api_key_id of this V1AuthApiKey.


        :param api_key_id: The api_key_id of this V1AuthApiKey.  # noqa: E501
        :type: int
        """
        if api_key_id is None:
            raise ValueError(
                "Invalid value for `api_key_id`, must not be `None`"
            )  # noqa: E501

        self._api_key_id = api_key_id

    @property
    def api_key_created_at(self):
        """Gets the api_key_created_at of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_created_at of this V1AuthApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._api_key_created_at

    @api_key_created_at.setter
    def api_key_created_at(self, api_key_created_at):
        """Sets the api_key_created_at of this V1AuthApiKey.


        :param api_key_created_at: The api_key_created_at of this V1AuthApiKey.  # noqa: E501
        :type: datetime
        """
        if api_key_created_at is None:
            raise ValueError(
                "Invalid value for `api_key_created_at`, must not be `None`"
            )  # noqa: E501

        self._api_key_created_at = api_key_created_at

    @property
    def api_key_updated_at(self):
        """Gets the api_key_updated_at of this V1AuthApiKey.  # noqa: E501


        :return: The api_key_updated_at of this V1AuthApiKey.  # noqa: E501
        :rtype: datetime
        """
        return self._api_key_updated_at

    @api_key_updated_at.setter
    def api_key_updated_at(self, api_key_updated_at):
        """Sets the api_key_updated_at of this V1AuthApiKey.


        :param api_key_updated_at: The api_key_updated_at of this V1AuthApiKey.  # noqa: E501
        :type: datetime
        """
        if api_key_updated_at is None:
            raise ValueError(
                "Invalid value for `api_key_updated_at`, must not be `None`"
            )  # noqa: E501

        self._api_key_updated_at = api_key_updated_at

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
        if issubclass(V1AuthApiKey, dict):
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
        if not isinstance(other, V1AuthApiKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
