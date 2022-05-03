# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.317
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

from lusid_notifications.configuration import Configuration


class Delivery(object):
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
        'id': 'str',
        'event_id': 'str',
        'subscription_id': 'ResourceId',
        'notification_id': 'str',
        'delivery_channel': 'str',
        'message_details': 'str',
        'attempts': 'list[Attempt]'
    }

    attribute_map = {
        'id': 'id',
        'event_id': 'eventId',
        'subscription_id': 'subscriptionId',
        'notification_id': 'notificationId',
        'delivery_channel': 'deliveryChannel',
        'message_details': 'messageDetails',
        'attempts': 'attempts'
    }

    required_map = {
        'id': 'required',
        'event_id': 'required',
        'subscription_id': 'required',
        'notification_id': 'required',
        'delivery_channel': 'required',
        'message_details': 'required',
        'attempts': 'required'
    }

    def __init__(self, id=None, event_id=None, subscription_id=None, notification_id=None, delivery_channel=None, message_details=None, attempts=None, local_vars_configuration=None):  # noqa: E501
        """Delivery - a model defined in OpenAPI"
        
        :param id:  The identifier of the delivery. (required)
        :type id: str
        :param event_id:  The identifier of the associated event. (required)
        :type event_id: str
        :param subscription_id:  (required)
        :type subscription_id: lusid_notifications.ResourceId
        :param notification_id:  The identifier of the associated notification. (required)
        :type notification_id: str
        :param delivery_channel:  The delivery channel of the message. (required)
        :type delivery_channel: str
        :param message_details:  The Details of the delivery message as JSON string. (required)
        :type message_details: str
        :param attempts:  A list of all the delivery attempts made for this message. (required)
        :type attempts: list[lusid_notifications.Attempt]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._event_id = None
        self._subscription_id = None
        self._notification_id = None
        self._delivery_channel = None
        self._message_details = None
        self._attempts = None
        self.discriminator = None

        self.id = id
        self.event_id = event_id
        self.subscription_id = subscription_id
        self.notification_id = notification_id
        self.delivery_channel = delivery_channel
        self.message_details = message_details
        self.attempts = attempts

    @property
    def id(self):
        """Gets the id of this Delivery.  # noqa: E501

        The identifier of the delivery.  # noqa: E501

        :return: The id of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Delivery.

        The identifier of the delivery.  # noqa: E501

        :param id: The id of this Delivery.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def event_id(self):
        """Gets the event_id of this Delivery.  # noqa: E501

        The identifier of the associated event.  # noqa: E501

        :return: The event_id of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this Delivery.

        The identifier of the associated event.  # noqa: E501

        :param event_id: The event_id of this Delivery.  # noqa: E501
        :type event_id: str
        """
        if self.local_vars_configuration.client_side_validation and event_id is None:  # noqa: E501
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def subscription_id(self):
        """Gets the subscription_id of this Delivery.  # noqa: E501


        :return: The subscription_id of this Delivery.  # noqa: E501
        :rtype: lusid_notifications.ResourceId
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        """Sets the subscription_id of this Delivery.


        :param subscription_id: The subscription_id of this Delivery.  # noqa: E501
        :type subscription_id: lusid_notifications.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and subscription_id is None:  # noqa: E501
            raise ValueError("Invalid value for `subscription_id`, must not be `None`")  # noqa: E501

        self._subscription_id = subscription_id

    @property
    def notification_id(self):
        """Gets the notification_id of this Delivery.  # noqa: E501

        The identifier of the associated notification.  # noqa: E501

        :return: The notification_id of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this Delivery.

        The identifier of the associated notification.  # noqa: E501

        :param notification_id: The notification_id of this Delivery.  # noqa: E501
        :type notification_id: str
        """
        if self.local_vars_configuration.client_side_validation and notification_id is None:  # noqa: E501
            raise ValueError("Invalid value for `notification_id`, must not be `None`")  # noqa: E501

        self._notification_id = notification_id

    @property
    def delivery_channel(self):
        """Gets the delivery_channel of this Delivery.  # noqa: E501

        The delivery channel of the message.  # noqa: E501

        :return: The delivery_channel of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._delivery_channel

    @delivery_channel.setter
    def delivery_channel(self, delivery_channel):
        """Sets the delivery_channel of this Delivery.

        The delivery channel of the message.  # noqa: E501

        :param delivery_channel: The delivery_channel of this Delivery.  # noqa: E501
        :type delivery_channel: str
        """
        if self.local_vars_configuration.client_side_validation and delivery_channel is None:  # noqa: E501
            raise ValueError("Invalid value for `delivery_channel`, must not be `None`")  # noqa: E501

        self._delivery_channel = delivery_channel

    @property
    def message_details(self):
        """Gets the message_details of this Delivery.  # noqa: E501

        The Details of the delivery message as JSON string.  # noqa: E501

        :return: The message_details of this Delivery.  # noqa: E501
        :rtype: str
        """
        return self._message_details

    @message_details.setter
    def message_details(self, message_details):
        """Sets the message_details of this Delivery.

        The Details of the delivery message as JSON string.  # noqa: E501

        :param message_details: The message_details of this Delivery.  # noqa: E501
        :type message_details: str
        """
        if self.local_vars_configuration.client_side_validation and message_details is None:  # noqa: E501
            raise ValueError("Invalid value for `message_details`, must not be `None`")  # noqa: E501

        self._message_details = message_details

    @property
    def attempts(self):
        """Gets the attempts of this Delivery.  # noqa: E501

        A list of all the delivery attempts made for this message.  # noqa: E501

        :return: The attempts of this Delivery.  # noqa: E501
        :rtype: list[lusid_notifications.Attempt]
        """
        return self._attempts

    @attempts.setter
    def attempts(self, attempts):
        """Sets the attempts of this Delivery.

        A list of all the delivery attempts made for this message.  # noqa: E501

        :param attempts: The attempts of this Delivery.  # noqa: E501
        :type attempts: list[lusid_notifications.Attempt]
        """
        if self.local_vars_configuration.client_side_validation and attempts is None:  # noqa: E501
            raise ValueError("Invalid value for `attempts`, must not be `None`")  # noqa: E501

        self._attempts = attempts

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
        if not isinstance(other, Delivery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Delivery):
            return True

        return self.to_dict() != other.to_dict()
