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


class ResponseBillingHistoryInfo(object):
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
        'amount': 'float',
        'created_by': 'ResponseSimpleUser',
        'created_dt': 'datetime',
        'duration': 'float',
        'experiment': 'ResponseSimpleExperiment',
        'project': 'ResponseSimpleProject',
        'status': 'str',
        'total': 'float',
        'type': 'str',
        'workspace': 'ResponseSimpleWorkspace'
    }

    attribute_map = {
        'amount': 'amount',
        'created_by': 'created_by',
        'created_dt': 'created_dt',
        'duration': 'duration',
        'experiment': 'experiment',
        'project': 'project',
        'status': 'status',
        'total': 'total',
        'type': 'type',
        'workspace': 'workspace'
    }

    def __init__(self, amount=None, created_by=None, created_dt=None, duration=None, experiment=None, project=None, status=None, total=None, type=None, workspace=None, local_vars_configuration=None):  # noqa: E501
        """ResponseBillingHistoryInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._created_by = None
        self._created_dt = None
        self._duration = None
        self._experiment = None
        self._project = None
        self._status = None
        self._total = None
        self._type = None
        self._workspace = None
        self.discriminator = None

        self.amount = amount
        self.created_by = created_by
        self.created_dt = created_dt
        self.duration = duration
        if experiment is not None:
            self.experiment = experiment
        self.project = project
        self.status = status
        self.total = total
        self.type = type
        if workspace is not None:
            self.workspace = workspace

    @property
    def amount(self):
        """Gets the amount of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The amount of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ResponseBillingHistoryInfo.


        :param amount: The amount of this ResponseBillingHistoryInfo.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def created_by(self):
        """Gets the created_by of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The created_by of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: ResponseSimpleUser
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ResponseBillingHistoryInfo.


        :param created_by: The created_by of this ResponseBillingHistoryInfo.  # noqa: E501
        :type created_by: ResponseSimpleUser
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The created_dt of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseBillingHistoryInfo.


        :param created_dt: The created_dt of this ResponseBillingHistoryInfo.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def duration(self):
        """Gets the duration of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The duration of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ResponseBillingHistoryInfo.


        :param duration: The duration of this ResponseBillingHistoryInfo.  # noqa: E501
        :type duration: float
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def experiment(self):
        """Gets the experiment of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The experiment of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: ResponseSimpleExperiment
        """
        return self._experiment

    @experiment.setter
    def experiment(self, experiment):
        """Sets the experiment of this ResponseBillingHistoryInfo.


        :param experiment: The experiment of this ResponseBillingHistoryInfo.  # noqa: E501
        :type experiment: ResponseSimpleExperiment
        """

        self._experiment = experiment

    @property
    def project(self):
        """Gets the project of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The project of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: ResponseSimpleProject
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ResponseBillingHistoryInfo.


        :param project: The project of this ResponseBillingHistoryInfo.  # noqa: E501
        :type project: ResponseSimpleProject
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def status(self):
        """Gets the status of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The status of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseBillingHistoryInfo.


        :param status: The status of this ResponseBillingHistoryInfo.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def total(self):
        """Gets the total of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The total of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ResponseBillingHistoryInfo.


        :param total: The total of this ResponseBillingHistoryInfo.  # noqa: E501
        :type total: float
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def type(self):
        """Gets the type of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The type of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResponseBillingHistoryInfo.


        :param type: The type of this ResponseBillingHistoryInfo.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def workspace(self):
        """Gets the workspace of this ResponseBillingHistoryInfo.  # noqa: E501


        :return: The workspace of this ResponseBillingHistoryInfo.  # noqa: E501
        :rtype: ResponseSimpleWorkspace
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ResponseBillingHistoryInfo.


        :param workspace: The workspace of this ResponseBillingHistoryInfo.  # noqa: E501
        :type workspace: ResponseSimpleWorkspace
        """

        self._workspace = workspace

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
        if not isinstance(other, ResponseBillingHistoryInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseBillingHistoryInfo):
            return True

        return self.to_dict() != other.to_dict()
