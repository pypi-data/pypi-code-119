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


class OrmOrganizationEdges(object):
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
        'billing_histories': 'list[OrmBillingHistory]',
        'default_storage': 'OrmStorage',
        'default_volume': 'OrmVolume',
        'notification_configs': 'list[OrmNotificationConfig]',
        'organization_credentials': 'list[OrmOrganizationCredentials]',
        'organization_kernel_clusters': 'list[OrmOrganizationKernelCluster]',
        'pricing_plan': 'OrmPricingPlan',
        'primary_owner': 'OrmUser',
        'quotas': 'list[OrmQuota]',
        'stripe_billing_history': 'list[OrmStripeBillingHistory]',
        'user_organization': 'list[OrmUserOrganization]',
        'workspaces': 'list[OrmWorkspace]'
    }

    attribute_map = {
        'billing_histories': 'billing_histories',
        'default_storage': 'default_storage',
        'default_volume': 'default_volume',
        'notification_configs': 'notification_configs',
        'organization_credentials': 'organization_credentials',
        'organization_kernel_clusters': 'organization_kernel_clusters',
        'pricing_plan': 'pricing_plan',
        'primary_owner': 'primary_owner',
        'quotas': 'quotas',
        'stripe_billing_history': 'stripe_billing_history',
        'user_organization': 'user_organization',
        'workspaces': 'workspaces'
    }

    def __init__(self, billing_histories=None, default_storage=None, default_volume=None, notification_configs=None, organization_credentials=None, organization_kernel_clusters=None, pricing_plan=None, primary_owner=None, quotas=None, stripe_billing_history=None, user_organization=None, workspaces=None, local_vars_configuration=None):  # noqa: E501
        """OrmOrganizationEdges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._billing_histories = None
        self._default_storage = None
        self._default_volume = None
        self._notification_configs = None
        self._organization_credentials = None
        self._organization_kernel_clusters = None
        self._pricing_plan = None
        self._primary_owner = None
        self._quotas = None
        self._stripe_billing_history = None
        self._user_organization = None
        self._workspaces = None
        self.discriminator = None

        if billing_histories is not None:
            self.billing_histories = billing_histories
        if default_storage is not None:
            self.default_storage = default_storage
        if default_volume is not None:
            self.default_volume = default_volume
        if notification_configs is not None:
            self.notification_configs = notification_configs
        if organization_credentials is not None:
            self.organization_credentials = organization_credentials
        if organization_kernel_clusters is not None:
            self.organization_kernel_clusters = organization_kernel_clusters
        if pricing_plan is not None:
            self.pricing_plan = pricing_plan
        if primary_owner is not None:
            self.primary_owner = primary_owner
        if quotas is not None:
            self.quotas = quotas
        if stripe_billing_history is not None:
            self.stripe_billing_history = stripe_billing_history
        if user_organization is not None:
            self.user_organization = user_organization
        if workspaces is not None:
            self.workspaces = workspaces

    @property
    def billing_histories(self):
        """Gets the billing_histories of this OrmOrganizationEdges.  # noqa: E501


        :return: The billing_histories of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmBillingHistory]
        """
        return self._billing_histories

    @billing_histories.setter
    def billing_histories(self, billing_histories):
        """Sets the billing_histories of this OrmOrganizationEdges.


        :param billing_histories: The billing_histories of this OrmOrganizationEdges.  # noqa: E501
        :type billing_histories: list[OrmBillingHistory]
        """

        self._billing_histories = billing_histories

    @property
    def default_storage(self):
        """Gets the default_storage of this OrmOrganizationEdges.  # noqa: E501


        :return: The default_storage of this OrmOrganizationEdges.  # noqa: E501
        :rtype: OrmStorage
        """
        return self._default_storage

    @default_storage.setter
    def default_storage(self, default_storage):
        """Sets the default_storage of this OrmOrganizationEdges.


        :param default_storage: The default_storage of this OrmOrganizationEdges.  # noqa: E501
        :type default_storage: OrmStorage
        """

        self._default_storage = default_storage

    @property
    def default_volume(self):
        """Gets the default_volume of this OrmOrganizationEdges.  # noqa: E501


        :return: The default_volume of this OrmOrganizationEdges.  # noqa: E501
        :rtype: OrmVolume
        """
        return self._default_volume

    @default_volume.setter
    def default_volume(self, default_volume):
        """Sets the default_volume of this OrmOrganizationEdges.


        :param default_volume: The default_volume of this OrmOrganizationEdges.  # noqa: E501
        :type default_volume: OrmVolume
        """

        self._default_volume = default_volume

    @property
    def notification_configs(self):
        """Gets the notification_configs of this OrmOrganizationEdges.  # noqa: E501


        :return: The notification_configs of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmNotificationConfig]
        """
        return self._notification_configs

    @notification_configs.setter
    def notification_configs(self, notification_configs):
        """Sets the notification_configs of this OrmOrganizationEdges.


        :param notification_configs: The notification_configs of this OrmOrganizationEdges.  # noqa: E501
        :type notification_configs: list[OrmNotificationConfig]
        """

        self._notification_configs = notification_configs

    @property
    def organization_credentials(self):
        """Gets the organization_credentials of this OrmOrganizationEdges.  # noqa: E501


        :return: The organization_credentials of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmOrganizationCredentials]
        """
        return self._organization_credentials

    @organization_credentials.setter
    def organization_credentials(self, organization_credentials):
        """Sets the organization_credentials of this OrmOrganizationEdges.


        :param organization_credentials: The organization_credentials of this OrmOrganizationEdges.  # noqa: E501
        :type organization_credentials: list[OrmOrganizationCredentials]
        """

        self._organization_credentials = organization_credentials

    @property
    def organization_kernel_clusters(self):
        """Gets the organization_kernel_clusters of this OrmOrganizationEdges.  # noqa: E501


        :return: The organization_kernel_clusters of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmOrganizationKernelCluster]
        """
        return self._organization_kernel_clusters

    @organization_kernel_clusters.setter
    def organization_kernel_clusters(self, organization_kernel_clusters):
        """Sets the organization_kernel_clusters of this OrmOrganizationEdges.


        :param organization_kernel_clusters: The organization_kernel_clusters of this OrmOrganizationEdges.  # noqa: E501
        :type organization_kernel_clusters: list[OrmOrganizationKernelCluster]
        """

        self._organization_kernel_clusters = organization_kernel_clusters

    @property
    def pricing_plan(self):
        """Gets the pricing_plan of this OrmOrganizationEdges.  # noqa: E501


        :return: The pricing_plan of this OrmOrganizationEdges.  # noqa: E501
        :rtype: OrmPricingPlan
        """
        return self._pricing_plan

    @pricing_plan.setter
    def pricing_plan(self, pricing_plan):
        """Sets the pricing_plan of this OrmOrganizationEdges.


        :param pricing_plan: The pricing_plan of this OrmOrganizationEdges.  # noqa: E501
        :type pricing_plan: OrmPricingPlan
        """

        self._pricing_plan = pricing_plan

    @property
    def primary_owner(self):
        """Gets the primary_owner of this OrmOrganizationEdges.  # noqa: E501


        :return: The primary_owner of this OrmOrganizationEdges.  # noqa: E501
        :rtype: OrmUser
        """
        return self._primary_owner

    @primary_owner.setter
    def primary_owner(self, primary_owner):
        """Sets the primary_owner of this OrmOrganizationEdges.


        :param primary_owner: The primary_owner of this OrmOrganizationEdges.  # noqa: E501
        :type primary_owner: OrmUser
        """

        self._primary_owner = primary_owner

    @property
    def quotas(self):
        """Gets the quotas of this OrmOrganizationEdges.  # noqa: E501


        :return: The quotas of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmQuota]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this OrmOrganizationEdges.


        :param quotas: The quotas of this OrmOrganizationEdges.  # noqa: E501
        :type quotas: list[OrmQuota]
        """

        self._quotas = quotas

    @property
    def stripe_billing_history(self):
        """Gets the stripe_billing_history of this OrmOrganizationEdges.  # noqa: E501


        :return: The stripe_billing_history of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmStripeBillingHistory]
        """
        return self._stripe_billing_history

    @stripe_billing_history.setter
    def stripe_billing_history(self, stripe_billing_history):
        """Sets the stripe_billing_history of this OrmOrganizationEdges.


        :param stripe_billing_history: The stripe_billing_history of this OrmOrganizationEdges.  # noqa: E501
        :type stripe_billing_history: list[OrmStripeBillingHistory]
        """

        self._stripe_billing_history = stripe_billing_history

    @property
    def user_organization(self):
        """Gets the user_organization of this OrmOrganizationEdges.  # noqa: E501


        :return: The user_organization of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmUserOrganization]
        """
        return self._user_organization

    @user_organization.setter
    def user_organization(self, user_organization):
        """Sets the user_organization of this OrmOrganizationEdges.


        :param user_organization: The user_organization of this OrmOrganizationEdges.  # noqa: E501
        :type user_organization: list[OrmUserOrganization]
        """

        self._user_organization = user_organization

    @property
    def workspaces(self):
        """Gets the workspaces of this OrmOrganizationEdges.  # noqa: E501


        :return: The workspaces of this OrmOrganizationEdges.  # noqa: E501
        :rtype: list[OrmWorkspace]
        """
        return self._workspaces

    @workspaces.setter
    def workspaces(self, workspaces):
        """Sets the workspaces of this OrmOrganizationEdges.


        :param workspaces: The workspaces of this OrmOrganizationEdges.  # noqa: E501
        :type workspaces: list[OrmWorkspace]
        """

        self._workspaces = workspaces

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
        if not isinstance(other, OrmOrganizationEdges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrmOrganizationEdges):
            return True

        return self.to_dict() != other.to_dict()
