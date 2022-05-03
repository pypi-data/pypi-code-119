"""
    BIMData API

    BIMData API is a tool to interact with your models stored on BIMData’s servers.     Through the API, you can manage your projects, the clouds, upload your IFC files and manage them through endpoints.  # noqa: E501

    The version of the OpenAPI document: v1 (v1)
    Contact: support@bimdata.io
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from bimdata_api_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from bimdata_api_client.exceptions import ApiAttributeError


def lazy_import():
    from bimdata_api_client.model.clipping_plane import ClippingPlane
    from bimdata_api_client.model.components_parent import ComponentsParent
    from bimdata_api_client.model.line import Line
    from bimdata_api_client.model.orthogonal_camera import OrthogonalCamera
    from bimdata_api_client.model.perspective_camera import PerspectiveCamera
    from bimdata_api_client.model.snapshot import Snapshot
    globals()['ClippingPlane'] = ClippingPlane
    globals()['ComponentsParent'] = ComponentsParent
    globals()['Line'] = Line
    globals()['OrthogonalCamera'] = OrthogonalCamera
    globals()['PerspectiveCamera'] = PerspectiveCamera
    globals()['Snapshot'] = Snapshot


class Viewpoint(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('index',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': 0,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'index': (int, none_type,),  # noqa: E501
            'guid': (str,),  # noqa: E501
            'orthogonal_camera': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'perspective_camera': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'lines': ([Line], none_type,),  # noqa: E501
            'clipping_planes': ([ClippingPlane], none_type,),  # noqa: E501
            'snapshot': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'components': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'pins': ([[float]], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'index': 'index',  # noqa: E501
        'guid': 'guid',  # noqa: E501
        'orthogonal_camera': 'orthogonal_camera',  # noqa: E501
        'perspective_camera': 'perspective_camera',  # noqa: E501
        'lines': 'lines',  # noqa: E501
        'clipping_planes': 'clipping_planes',  # noqa: E501
        'snapshot': 'snapshot',  # noqa: E501
        'components': 'components',  # noqa: E501
        'pins': 'pins',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Viewpoint - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            index (int, none_type): [optional]  # noqa: E501
            guid (str): [optional]  # noqa: E501
            orthogonal_camera (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            perspective_camera (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            lines ([Line], none_type): [optional]  # noqa: E501
            clipping_planes ([ClippingPlane], none_type): [optional]  # noqa: E501
            snapshot (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            components (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            pins ([[float]], none_type): Non standard field. Pins is a list of points representing annotation positions. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Viewpoint - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            index (int, none_type): [optional]  # noqa: E501
            guid (str): [optional]  # noqa: E501
            orthogonal_camera (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            perspective_camera (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            lines ([Line], none_type): [optional]  # noqa: E501
            clipping_planes ([ClippingPlane], none_type): [optional]  # noqa: E501
            snapshot (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            components (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            pins ([[float]], none_type): Non standard field. Pins is a list of points representing annotation positions. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
