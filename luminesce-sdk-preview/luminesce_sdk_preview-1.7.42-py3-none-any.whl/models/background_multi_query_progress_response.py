# coding: utf-8

"""
    FINBOURNE Honeycomb Web API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.7.42
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from luminesce.configuration import Configuration


class BackgroundMultiQueryProgressResponse(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'progress': 'str',
        'feedback': 'list[FeedbackEventArgs]',
        'status': 'TaskStatus',
        'queries': 'list[BackgroundQueryProgressResponse]'
    }

    attribute_map = {
        'progress': 'progress',
        'feedback': 'feedback',
        'status': 'status',
        'queries': 'queries'
    }

    required_map = {
        'progress': 'optional',
        'feedback': 'optional',
        'status': 'optional',
        'queries': 'optional'
    }

    def __init__(self, progress=None, feedback=None, status=None, queries=None, local_vars_configuration=None):  # noqa: E501
        """BackgroundMultiQueryProgressResponse - a model defined in OpenAPI"
        
        :param progress:  The full progress log (up to this point at least)
        :type progress: str
        :param feedback:  Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call.
        :type feedback: list[luminesce.FeedbackEventArgs]
        :param status: 
        :type status: luminesce.TaskStatus
        :param queries: 
        :type queries: list[luminesce.BackgroundQueryProgressResponse]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._progress = None
        self._feedback = None
        self._status = None
        self._queries = None
        self.discriminator = None

        self.progress = progress
        self.feedback = feedback
        if status is not None:
            self.status = status
        self.queries = queries

    @property
    def progress(self):
        """Gets the progress of this BackgroundMultiQueryProgressResponse.  # noqa: E501

        The full progress log (up to this point at least)  # noqa: E501

        :return: The progress of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :rtype: str
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this BackgroundMultiQueryProgressResponse.

        The full progress log (up to this point at least)  # noqa: E501

        :param progress: The progress of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :type progress: str
        """

        self._progress = progress

    @property
    def feedback(self):
        """Gets the feedback of this BackgroundMultiQueryProgressResponse.  # noqa: E501

        Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call.  # noqa: E501

        :return: The feedback of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :rtype: list[luminesce.FeedbackEventArgs]
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this BackgroundMultiQueryProgressResponse.

        Individual Feedback Messages (to replace Progress).  A given message will be returned from only one call.  # noqa: E501

        :param feedback: The feedback of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :type feedback: list[luminesce.FeedbackEventArgs]
        """

        self._feedback = feedback

    @property
    def status(self):
        """Gets the status of this BackgroundMultiQueryProgressResponse.  # noqa: E501


        :return: The status of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :rtype: luminesce.TaskStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BackgroundMultiQueryProgressResponse.


        :param status: The status of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :type status: luminesce.TaskStatus
        """

        self._status = status

    @property
    def queries(self):
        """Gets the queries of this BackgroundMultiQueryProgressResponse.  # noqa: E501


        :return: The queries of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :rtype: list[luminesce.BackgroundQueryProgressResponse]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        """Sets the queries of this BackgroundMultiQueryProgressResponse.


        :param queries: The queries of this BackgroundMultiQueryProgressResponse.  # noqa: E501
        :type queries: list[luminesce.BackgroundQueryProgressResponse]
        """

        self._queries = queries

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
        if not isinstance(other, BackgroundMultiQueryProgressResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BackgroundMultiQueryProgressResponse):
            return True

        return self.to_dict() != other.to_dict()
