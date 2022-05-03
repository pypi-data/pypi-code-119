# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.models.collection_version_response import CollectionVersionResponse  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException

class TestCollectionVersionResponse(unittest.TestCase):
    """CollectionVersionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CollectionVersionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_ansible.models.collection_version_response.CollectionVersionResponse()  # noqa: E501
        if include_optional :
            return CollectionVersionResponse(
                version = '0', 
                href = '0', 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                requires_ansible = '0', 
                artifact = null, 
                collection = null, 
                download_url = '0', 
                name = '0', 
                namespace = null, 
                signatures = '0', 
                metadata = null, 
                git_url = '0', 
                git_commit_sha = '0', 
                manifest = None, 
                files = None
            )
        else :
            return CollectionVersionResponse(
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )

    def testCollectionVersionResponse(self):
        """Test CollectionVersionResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
