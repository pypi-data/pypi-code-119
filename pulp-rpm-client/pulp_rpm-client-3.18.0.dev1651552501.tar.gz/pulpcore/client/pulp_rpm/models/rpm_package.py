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

from pulpcore.client.pulp_rpm.configuration import Configuration


class RpmPackage(object):
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
        'artifact': 'str',
        'relative_path': 'str',
        'file': 'file',
        'repository': 'str'
    }

    attribute_map = {
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'file': 'file',
        'repository': 'repository'
    }

    def __init__(self, artifact=None, relative_path=None, file=None, repository=None, local_vars_configuration=None):  # noqa: E501
        """RpmPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._artifact = None
        self._relative_path = None
        self._file = None
        self._repository = None
        self.discriminator = None

        if artifact is not None:
            self.artifact = artifact
        self.relative_path = relative_path
        if file is not None:
            self.file = file
        if repository is not None:
            self.repository = repository

    @property
    def artifact(self):
        """Gets the artifact of this RpmPackage.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this RpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this RpmPackage.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this RpmPackage.  # noqa: E501
        :type: str
        """

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this RpmPackage.  # noqa: E501

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :return: The relative_path of this RpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this RpmPackage.

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :param relative_path: The relative_path of this RpmPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_path is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_path is not None and len(relative_path) < 1):
            raise ValueError("Invalid value for `relative_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def file(self):
        """Gets the file of this RpmPackage.  # noqa: E501

        An uploaded file that may be turned into the artifact of the content unit.  # noqa: E501

        :return: The file of this RpmPackage.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this RpmPackage.

        An uploaded file that may be turned into the artifact of the content unit.  # noqa: E501

        :param file: The file of this RpmPackage.  # noqa: E501
        :type: file
        """

        self._file = file

    @property
    def repository(self):
        """Gets the repository of this RpmPackage.  # noqa: E501

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :return: The repository of this RpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RpmPackage.

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :param repository: The repository of this RpmPackage.  # noqa: E501
        :type: str
        """

        self._repository = repository

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
        if not isinstance(other, RpmPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpmPackage):
            return True

        return self.to_dict() != other.to_dict()
