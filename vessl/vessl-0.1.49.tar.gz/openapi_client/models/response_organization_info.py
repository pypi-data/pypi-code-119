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


class ResponseOrganizationInfo(object):
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
        'aws_external_id': 'str',
        'created_dt': 'datetime',
        'credit_balance': 'float',
        'default_region': 'str',
        'description': 'str',
        'display_name': 'str',
        'id': 'int',
        'is_public': 'bool',
        'name': 'str',
        'pricing_plan': 'ResponsePricingPlan',
        'primary_owner_id': 'int',
        'stripe_customer_id': 'str',
        'stripe_subscription_id': 'str',
        'updated_dt': 'datetime'
    }

    attribute_map = {
        'aws_external_id': 'aws_external_id',
        'created_dt': 'created_dt',
        'credit_balance': 'credit_balance',
        'default_region': 'default_region',
        'description': 'description',
        'display_name': 'display_name',
        'id': 'id',
        'is_public': 'is_public',
        'name': 'name',
        'pricing_plan': 'pricing_plan',
        'primary_owner_id': 'primary_owner_id',
        'stripe_customer_id': 'stripe_customer_id',
        'stripe_subscription_id': 'stripe_subscription_id',
        'updated_dt': 'updated_dt'
    }

    def __init__(self, aws_external_id=None, created_dt=None, credit_balance=None, default_region=None, description=None, display_name=None, id=None, is_public=None, name=None, pricing_plan=None, primary_owner_id=None, stripe_customer_id=None, stripe_subscription_id=None, updated_dt=None, local_vars_configuration=None):  # noqa: E501
        """ResponseOrganizationInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aws_external_id = None
        self._created_dt = None
        self._credit_balance = None
        self._default_region = None
        self._description = None
        self._display_name = None
        self._id = None
        self._is_public = None
        self._name = None
        self._pricing_plan = None
        self._primary_owner_id = None
        self._stripe_customer_id = None
        self._stripe_subscription_id = None
        self._updated_dt = None
        self.discriminator = None

        self.aws_external_id = aws_external_id
        self.created_dt = created_dt
        self.credit_balance = credit_balance
        self.default_region = default_region
        self.description = description
        self.display_name = display_name
        self.id = id
        self.is_public = is_public
        self.name = name
        self.pricing_plan = pricing_plan
        self.primary_owner_id = primary_owner_id
        self.stripe_customer_id = stripe_customer_id
        self.stripe_subscription_id = stripe_subscription_id
        self.updated_dt = updated_dt

    @property
    def aws_external_id(self):
        """Gets the aws_external_id of this ResponseOrganizationInfo.  # noqa: E501


        :return: The aws_external_id of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._aws_external_id

    @aws_external_id.setter
    def aws_external_id(self, aws_external_id):
        """Sets the aws_external_id of this ResponseOrganizationInfo.


        :param aws_external_id: The aws_external_id of this ResponseOrganizationInfo.  # noqa: E501
        :type aws_external_id: str
        """
        if self.local_vars_configuration.client_side_validation and aws_external_id is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_external_id`, must not be `None`")  # noqa: E501

        self._aws_external_id = aws_external_id

    @property
    def created_dt(self):
        """Gets the created_dt of this ResponseOrganizationInfo.  # noqa: E501


        :return: The created_dt of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._created_dt

    @created_dt.setter
    def created_dt(self, created_dt):
        """Sets the created_dt of this ResponseOrganizationInfo.


        :param created_dt: The created_dt of this ResponseOrganizationInfo.  # noqa: E501
        :type created_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `created_dt`, must not be `None`")  # noqa: E501

        self._created_dt = created_dt

    @property
    def credit_balance(self):
        """Gets the credit_balance of this ResponseOrganizationInfo.  # noqa: E501


        :return: The credit_balance of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: float
        """
        return self._credit_balance

    @credit_balance.setter
    def credit_balance(self, credit_balance):
        """Sets the credit_balance of this ResponseOrganizationInfo.


        :param credit_balance: The credit_balance of this ResponseOrganizationInfo.  # noqa: E501
        :type credit_balance: float
        """
        if self.local_vars_configuration.client_side_validation and credit_balance is None:  # noqa: E501
            raise ValueError("Invalid value for `credit_balance`, must not be `None`")  # noqa: E501

        self._credit_balance = credit_balance

    @property
    def default_region(self):
        """Gets the default_region of this ResponseOrganizationInfo.  # noqa: E501


        :return: The default_region of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._default_region

    @default_region.setter
    def default_region(self, default_region):
        """Sets the default_region of this ResponseOrganizationInfo.


        :param default_region: The default_region of this ResponseOrganizationInfo.  # noqa: E501
        :type default_region: str
        """
        if self.local_vars_configuration.client_side_validation and default_region is None:  # noqa: E501
            raise ValueError("Invalid value for `default_region`, must not be `None`")  # noqa: E501

        self._default_region = default_region

    @property
    def description(self):
        """Gets the description of this ResponseOrganizationInfo.  # noqa: E501


        :return: The description of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ResponseOrganizationInfo.


        :param description: The description of this ResponseOrganizationInfo.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this ResponseOrganizationInfo.  # noqa: E501


        :return: The display_name of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResponseOrganizationInfo.


        :param display_name: The display_name of this ResponseOrganizationInfo.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this ResponseOrganizationInfo.  # noqa: E501


        :return: The id of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResponseOrganizationInfo.


        :param id: The id of this ResponseOrganizationInfo.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def is_public(self):
        """Gets the is_public of this ResponseOrganizationInfo.  # noqa: E501


        :return: The is_public of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ResponseOrganizationInfo.


        :param is_public: The is_public of this ResponseOrganizationInfo.  # noqa: E501
        :type is_public: bool
        """
        if self.local_vars_configuration.client_side_validation and is_public is None:  # noqa: E501
            raise ValueError("Invalid value for `is_public`, must not be `None`")  # noqa: E501

        self._is_public = is_public

    @property
    def name(self):
        """Gets the name of this ResponseOrganizationInfo.  # noqa: E501


        :return: The name of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseOrganizationInfo.


        :param name: The name of this ResponseOrganizationInfo.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def pricing_plan(self):
        """Gets the pricing_plan of this ResponseOrganizationInfo.  # noqa: E501


        :return: The pricing_plan of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: ResponsePricingPlan
        """
        return self._pricing_plan

    @pricing_plan.setter
    def pricing_plan(self, pricing_plan):
        """Sets the pricing_plan of this ResponseOrganizationInfo.


        :param pricing_plan: The pricing_plan of this ResponseOrganizationInfo.  # noqa: E501
        :type pricing_plan: ResponsePricingPlan
        """
        if self.local_vars_configuration.client_side_validation and pricing_plan is None:  # noqa: E501
            raise ValueError("Invalid value for `pricing_plan`, must not be `None`")  # noqa: E501

        self._pricing_plan = pricing_plan

    @property
    def primary_owner_id(self):
        """Gets the primary_owner_id of this ResponseOrganizationInfo.  # noqa: E501


        :return: The primary_owner_id of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: int
        """
        return self._primary_owner_id

    @primary_owner_id.setter
    def primary_owner_id(self, primary_owner_id):
        """Sets the primary_owner_id of this ResponseOrganizationInfo.


        :param primary_owner_id: The primary_owner_id of this ResponseOrganizationInfo.  # noqa: E501
        :type primary_owner_id: int
        """
        if self.local_vars_configuration.client_side_validation and primary_owner_id is None:  # noqa: E501
            raise ValueError("Invalid value for `primary_owner_id`, must not be `None`")  # noqa: E501

        self._primary_owner_id = primary_owner_id

    @property
    def stripe_customer_id(self):
        """Gets the stripe_customer_id of this ResponseOrganizationInfo.  # noqa: E501


        :return: The stripe_customer_id of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._stripe_customer_id

    @stripe_customer_id.setter
    def stripe_customer_id(self, stripe_customer_id):
        """Sets the stripe_customer_id of this ResponseOrganizationInfo.


        :param stripe_customer_id: The stripe_customer_id of this ResponseOrganizationInfo.  # noqa: E501
        :type stripe_customer_id: str
        """

        self._stripe_customer_id = stripe_customer_id

    @property
    def stripe_subscription_id(self):
        """Gets the stripe_subscription_id of this ResponseOrganizationInfo.  # noqa: E501


        :return: The stripe_subscription_id of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: str
        """
        return self._stripe_subscription_id

    @stripe_subscription_id.setter
    def stripe_subscription_id(self, stripe_subscription_id):
        """Sets the stripe_subscription_id of this ResponseOrganizationInfo.


        :param stripe_subscription_id: The stripe_subscription_id of this ResponseOrganizationInfo.  # noqa: E501
        :type stripe_subscription_id: str
        """

        self._stripe_subscription_id = stripe_subscription_id

    @property
    def updated_dt(self):
        """Gets the updated_dt of this ResponseOrganizationInfo.  # noqa: E501


        :return: The updated_dt of this ResponseOrganizationInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_dt

    @updated_dt.setter
    def updated_dt(self, updated_dt):
        """Sets the updated_dt of this ResponseOrganizationInfo.


        :param updated_dt: The updated_dt of this ResponseOrganizationInfo.  # noqa: E501
        :type updated_dt: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_dt is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_dt`, must not be `None`")  # noqa: E501

        self._updated_dt = updated_dt

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
        if not isinstance(other, ResponseOrganizationInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseOrganizationInfo):
            return True

        return self.to_dict() != other.to_dict()
