"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import bimdata_api_client
from bimdata_api_client.model.raw_material import RawMaterial
from bimdata_api_client.model.raw_material_list_components import RawMaterialListComponents
from bimdata_api_client.model.raw_material_options import RawMaterialOptions
globals()['RawMaterial'] = RawMaterial
globals()['RawMaterialListComponents'] = RawMaterialListComponents
globals()['RawMaterialOptions'] = RawMaterialOptions
from bimdata_api_client.model.raw_material_list import RawMaterialList


class TestRawMaterialList(unittest.TestCase):
    """RawMaterialList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRawMaterialList(self):
        """Test RawMaterialList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RawMaterialList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
