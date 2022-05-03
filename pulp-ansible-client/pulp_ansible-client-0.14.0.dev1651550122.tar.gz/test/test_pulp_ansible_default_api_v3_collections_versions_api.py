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

import pulpcore.client.pulp_ansible
from pulpcore.client.pulp_ansible.api.pulp_ansible_default_api_v3_collections_versions_api import PulpAnsibleDefaultApiV3CollectionsVersionsApi  # noqa: E501
from pulpcore.client.pulp_ansible.rest import ApiException


class TestPulpAnsibleDefaultApiV3CollectionsVersionsApi(unittest.TestCase):
    """PulpAnsibleDefaultApiV3CollectionsVersionsApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_ansible.api.pulp_ansible_default_api_v3_collections_versions_api.PulpAnsibleDefaultApiV3CollectionsVersionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete(self):
        """Test case for delete

        """
        pass

    def test_list(self):
        """Test case for list

        """
        pass

    def test_read(self):
        """Test case for read

        """
        pass


if __name__ == '__main__':
    unittest.main()
