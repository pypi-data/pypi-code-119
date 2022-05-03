#

#

"""
    Python Insight API

    This is an internal REST API between Python and Mosel  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech

    This material is the confidential, proprietary, unpublished property
    of Fair Isaac Corporation.  Receipt or possession of this material
    does not convey rights to divulge, reproduce, use, or allow others
    to use it without the specific written authorization of Fair Isaac
    Corporation and use must conform strictly to the license agreement.

    Copyright (c) 2020-2022 Fair Isaac Corporation. All rights reserved.
"""


from __future__ import absolute_import

__version__ = "1.0.0"

#
from xpressinsight.rest.api.default_api import DefaultApi

#
from xpressinsight.rest.api_client import ApiClient
from xpressinsight.rest.configuration import Configuration
from xpressinsight.rest.exceptions import OpenApiException
from xpressinsight.rest.exceptions import ApiTypeError
from xpressinsight.rest.exceptions import ApiValueError
from xpressinsight.rest.exceptions import ApiKeyError
from xpressinsight.rest.exceptions import ApiException
#
from xpressinsight.rest.models.attach_status import AttachStatus
from xpressinsight.rest.models.attachment import Attachment
from xpressinsight.rest.models.attachment_rules import AttachmentRules
from xpressinsight.rest.models.attachment_tag import AttachmentTag
from xpressinsight.rest.models.item_info import ItemInfo
from xpressinsight.rest.models.status import Status

