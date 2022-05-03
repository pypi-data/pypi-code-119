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


class OrmPageInfoWithCount(object):
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
        'end_cursor_id': 'int',
        'end_cursor_value': 'str',
        'has_next_page': 'bool',
        'has_previous_page': 'bool',
        'start_cursor_id': 'int',
        'start_cursor_value': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'end_cursor_id': 'endCursorID',
        'end_cursor_value': 'endCursorValue',
        'has_next_page': 'hasNextPage',
        'has_previous_page': 'hasPreviousPage',
        'start_cursor_id': 'startCursorID',
        'start_cursor_value': 'startCursorValue',
        'total_count': 'total_count'
    }

    def __init__(self, end_cursor_id=None, end_cursor_value=None, has_next_page=None, has_previous_page=None, start_cursor_id=None, start_cursor_value=None, total_count=None, local_vars_configuration=None):  # noqa: E501
        """OrmPageInfoWithCount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._end_cursor_id = None
        self._end_cursor_value = None
        self._has_next_page = None
        self._has_previous_page = None
        self._start_cursor_id = None
        self._start_cursor_value = None
        self._total_count = None
        self.discriminator = None

        if end_cursor_id is not None:
            self.end_cursor_id = end_cursor_id
        self.end_cursor_value = end_cursor_value
        if has_next_page is not None:
            self.has_next_page = has_next_page
        if has_previous_page is not None:
            self.has_previous_page = has_previous_page
        if start_cursor_id is not None:
            self.start_cursor_id = start_cursor_id
        self.start_cursor_value = start_cursor_value
        self.total_count = total_count

    @property
    def end_cursor_id(self):
        """Gets the end_cursor_id of this OrmPageInfoWithCount.  # noqa: E501


        :return: The end_cursor_id of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: int
        """
        return self._end_cursor_id

    @end_cursor_id.setter
    def end_cursor_id(self, end_cursor_id):
        """Sets the end_cursor_id of this OrmPageInfoWithCount.


        :param end_cursor_id: The end_cursor_id of this OrmPageInfoWithCount.  # noqa: E501
        :type end_cursor_id: int
        """

        self._end_cursor_id = end_cursor_id

    @property
    def end_cursor_value(self):
        """Gets the end_cursor_value of this OrmPageInfoWithCount.  # noqa: E501


        :return: The end_cursor_value of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: str
        """
        return self._end_cursor_value

    @end_cursor_value.setter
    def end_cursor_value(self, end_cursor_value):
        """Sets the end_cursor_value of this OrmPageInfoWithCount.


        :param end_cursor_value: The end_cursor_value of this OrmPageInfoWithCount.  # noqa: E501
        :type end_cursor_value: str
        """

        self._end_cursor_value = end_cursor_value

    @property
    def has_next_page(self):
        """Gets the has_next_page of this OrmPageInfoWithCount.  # noqa: E501


        :return: The has_next_page of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: bool
        """
        return self._has_next_page

    @has_next_page.setter
    def has_next_page(self, has_next_page):
        """Sets the has_next_page of this OrmPageInfoWithCount.


        :param has_next_page: The has_next_page of this OrmPageInfoWithCount.  # noqa: E501
        :type has_next_page: bool
        """

        self._has_next_page = has_next_page

    @property
    def has_previous_page(self):
        """Gets the has_previous_page of this OrmPageInfoWithCount.  # noqa: E501


        :return: The has_previous_page of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: bool
        """
        return self._has_previous_page

    @has_previous_page.setter
    def has_previous_page(self, has_previous_page):
        """Sets the has_previous_page of this OrmPageInfoWithCount.


        :param has_previous_page: The has_previous_page of this OrmPageInfoWithCount.  # noqa: E501
        :type has_previous_page: bool
        """

        self._has_previous_page = has_previous_page

    @property
    def start_cursor_id(self):
        """Gets the start_cursor_id of this OrmPageInfoWithCount.  # noqa: E501


        :return: The start_cursor_id of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: int
        """
        return self._start_cursor_id

    @start_cursor_id.setter
    def start_cursor_id(self, start_cursor_id):
        """Sets the start_cursor_id of this OrmPageInfoWithCount.


        :param start_cursor_id: The start_cursor_id of this OrmPageInfoWithCount.  # noqa: E501
        :type start_cursor_id: int
        """

        self._start_cursor_id = start_cursor_id

    @property
    def start_cursor_value(self):
        """Gets the start_cursor_value of this OrmPageInfoWithCount.  # noqa: E501


        :return: The start_cursor_value of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: str
        """
        return self._start_cursor_value

    @start_cursor_value.setter
    def start_cursor_value(self, start_cursor_value):
        """Sets the start_cursor_value of this OrmPageInfoWithCount.


        :param start_cursor_value: The start_cursor_value of this OrmPageInfoWithCount.  # noqa: E501
        :type start_cursor_value: str
        """

        self._start_cursor_value = start_cursor_value

    @property
    def total_count(self):
        """Gets the total_count of this OrmPageInfoWithCount.  # noqa: E501


        :return: The total_count of this OrmPageInfoWithCount.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this OrmPageInfoWithCount.


        :param total_count: The total_count of this OrmPageInfoWithCount.  # noqa: E501
        :type total_count: int
        """
        if self.local_vars_configuration.client_side_validation and total_count is None:  # noqa: E501
            raise ValueError("Invalid value for `total_count`, must not be `None`")  # noqa: E501

        self._total_count = total_count

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
        if not isinstance(other, OrmPageInfoWithCount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmPageInfoWithCount):
            return True

        return self.to_dict() != other.to_dict()
