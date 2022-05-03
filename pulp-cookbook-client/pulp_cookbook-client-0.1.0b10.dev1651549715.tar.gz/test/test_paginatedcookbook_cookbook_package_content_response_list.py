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

import pulpcore.client.pulp_cookbook
from pulpcore.client.pulp_cookbook.models.paginatedcookbook_cookbook_package_content_response_list import PaginatedcookbookCookbookPackageContentResponseList  # noqa: E501
from pulpcore.client.pulp_cookbook.rest import ApiException

class TestPaginatedcookbookCookbookPackageContentResponseList(unittest.TestCase):
    """PaginatedcookbookCookbookPackageContentResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedcookbookCookbookPackageContentResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_cookbook.models.paginatedcookbook_cookbook_package_content_response_list.PaginatedcookbookCookbookPackageContentResponseList()  # noqa: E501
        if include_optional :
            return PaginatedcookbookCookbookPackageContentResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_cookbook.models.cookbook/cookbook_package_content_response.cookbook.CookbookPackageContentResponse(
                        pulp_href = '0', 
                        artifact = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '0', 
                        version = '0', 
                        dependencies = pulpcore.client.pulp_cookbook.models.dependencies.dependencies(), 
                        content_id = '0', )
                    ]
            )
        else :
            return PaginatedcookbookCookbookPackageContentResponseList(
        )

    def testPaginatedcookbookCookbookPackageContentResponseList(self):
        """Test PaginatedcookbookCookbookPackageContentResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
