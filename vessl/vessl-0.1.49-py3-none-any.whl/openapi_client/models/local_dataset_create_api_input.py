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


class LocalDatasetCreateAPIInput(object):
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
        'cluster_id': 'int',
        'description': 'str',
        'local_volume': 'OrmLocalVolumeConfig',
        'minio_endpoint': 'str',
        'name': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'description': 'description',
        'local_volume': 'local_volume',
        'minio_endpoint': 'minio_endpoint',
        'name': 'name'
    }

    def __init__(self, cluster_id=None, description=None, local_volume=None, minio_endpoint=None, name=None, local_vars_configuration=None):  # noqa: E501
        """LocalDatasetCreateAPIInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._description = None
        self._local_volume = None
        self._minio_endpoint = None
        self._name = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.description = description
        self.local_volume = local_volume
        self.minio_endpoint = minio_endpoint
        self.name = name

    @property
    def cluster_id(self):
        """Gets the cluster_id of this LocalDatasetCreateAPIInput.  # noqa: E501


        :return: The cluster_id of this LocalDatasetCreateAPIInput.  # noqa: E501
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this LocalDatasetCreateAPIInput.


        :param cluster_id: The cluster_id of this LocalDatasetCreateAPIInput.  # noqa: E501
        :type cluster_id: int
        """
        if self.local_vars_configuration.client_side_validation and cluster_id is None:  # noqa: E501
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def description(self):
        """Gets the description of this LocalDatasetCreateAPIInput.  # noqa: E501


        :return: The description of this LocalDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LocalDatasetCreateAPIInput.


        :param description: The description of this LocalDatasetCreateAPIInput.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501

        self._description = description

    @property
    def local_volume(self):
        """Gets the local_volume of this LocalDatasetCreateAPIInput.  # noqa: E501


        :return: The local_volume of this LocalDatasetCreateAPIInput.  # noqa: E501
        :rtype: OrmLocalVolumeConfig
        """
        return self._local_volume

    @local_volume.setter
    def local_volume(self, local_volume):
        """Sets the local_volume of this LocalDatasetCreateAPIInput.


        :param local_volume: The local_volume of this LocalDatasetCreateAPIInput.  # noqa: E501
        :type local_volume: OrmLocalVolumeConfig
        """
        if self.local_vars_configuration.client_side_validation and local_volume is None:  # noqa: E501
            raise ValueError("Invalid value for `local_volume`, must not be `None`")  # noqa: E501

        self._local_volume = local_volume

    @property
    def minio_endpoint(self):
        """Gets the minio_endpoint of this LocalDatasetCreateAPIInput.  # noqa: E501


        :return: The minio_endpoint of this LocalDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._minio_endpoint

    @minio_endpoint.setter
    def minio_endpoint(self, minio_endpoint):
        """Sets the minio_endpoint of this LocalDatasetCreateAPIInput.


        :param minio_endpoint: The minio_endpoint of this LocalDatasetCreateAPIInput.  # noqa: E501
        :type minio_endpoint: str
        """

        self._minio_endpoint = minio_endpoint

    @property
    def name(self):
        """Gets the name of this LocalDatasetCreateAPIInput.  # noqa: E501


        :return: The name of this LocalDatasetCreateAPIInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LocalDatasetCreateAPIInput.


        :param name: The name of this LocalDatasetCreateAPIInput.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 255):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, LocalDatasetCreateAPIInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LocalDatasetCreateAPIInput):
            return True

        return self.to_dict() != other.to_dict()
