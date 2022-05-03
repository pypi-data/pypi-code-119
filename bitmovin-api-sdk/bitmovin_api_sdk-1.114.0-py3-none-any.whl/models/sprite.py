# coding: utf-8

from enum import Enum
from six import string_types, iteritems
from bitmovin_api_sdk.common.poscheck import poscheck_model
from bitmovin_api_sdk.models.bitmovin_resource import BitmovinResource
from bitmovin_api_sdk.models.sprite_creation_mode import SpriteCreationMode
from bitmovin_api_sdk.models.sprite_jpeg_config import SpriteJpegConfig
from bitmovin_api_sdk.models.sprite_unit import SpriteUnit
from bitmovin_api_sdk.models.thumbnail_aspect_mode import ThumbnailAspectMode
import pprint
import six


class Sprite(BitmovinResource):
    @poscheck_model
    def __init__(self,
                 id_=None,
                 name=None,
                 description=None,
                 created_at=None,
                 modified_at=None,
                 custom_data=None,
                 height=None,
                 width=None,
                 unit=None,
                 distance=None,
                 sprite_name=None,
                 filename=None,
                 vtt_name=None,
                 outputs=None,
                 images_per_file=None,
                 h_tiles=None,
                 v_tiles=None,
                 jpeg_config=None,
                 creation_mode=None,
                 aspect_mode=None):
        # type: (string_types, string_types, string_types, datetime, datetime, dict, int, int, SpriteUnit, float, string_types, string_types, string_types, list[EncodingOutput], int, int, int, SpriteJpegConfig, SpriteCreationMode, ThumbnailAspectMode) -> None
        super(Sprite, self).__init__(id_=id_, name=name, description=description, created_at=created_at, modified_at=modified_at, custom_data=custom_data)

        self._height = None
        self._width = None
        self._unit = None
        self._distance = None
        self._sprite_name = None
        self._filename = None
        self._vtt_name = None
        self._outputs = list()
        self._images_per_file = None
        self._h_tiles = None
        self._v_tiles = None
        self._jpeg_config = None
        self._creation_mode = None
        self._aspect_mode = None
        self.discriminator = None

        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if unit is not None:
            self.unit = unit
        if distance is not None:
            self.distance = distance
        if sprite_name is not None:
            self.sprite_name = sprite_name
        if filename is not None:
            self.filename = filename
        if vtt_name is not None:
            self.vtt_name = vtt_name
        if outputs is not None:
            self.outputs = outputs
        if images_per_file is not None:
            self.images_per_file = images_per_file
        if h_tiles is not None:
            self.h_tiles = h_tiles
        if v_tiles is not None:
            self.v_tiles = v_tiles
        if jpeg_config is not None:
            self.jpeg_config = jpeg_config
        if creation_mode is not None:
            self.creation_mode = creation_mode
        if aspect_mode is not None:
            self.aspect_mode = aspect_mode

    @property
    def openapi_types(self):
        types = {}

        if hasattr(super(Sprite, self), 'openapi_types'):
            types = getattr(super(Sprite, self), 'openapi_types')

        types.update({
            'height': 'int',
            'width': 'int',
            'unit': 'SpriteUnit',
            'distance': 'float',
            'sprite_name': 'string_types',
            'filename': 'string_types',
            'vtt_name': 'string_types',
            'outputs': 'list[EncodingOutput]',
            'images_per_file': 'int',
            'h_tiles': 'int',
            'v_tiles': 'int',
            'jpeg_config': 'SpriteJpegConfig',
            'creation_mode': 'SpriteCreationMode',
            'aspect_mode': 'ThumbnailAspectMode'
        })

        return types

    @property
    def attribute_map(self):
        attributes = {}

        if hasattr(super(Sprite, self), 'attribute_map'):
            attributes = getattr(super(Sprite, self), 'attribute_map')

        attributes.update({
            'height': 'height',
            'width': 'width',
            'unit': 'unit',
            'distance': 'distance',
            'sprite_name': 'spriteName',
            'filename': 'filename',
            'vtt_name': 'vttName',
            'outputs': 'outputs',
            'images_per_file': 'imagesPerFile',
            'h_tiles': 'hTiles',
            'v_tiles': 'vTiles',
            'jpeg_config': 'jpegConfig',
            'creation_mode': 'creationMode',
            'aspect_mode': 'aspectMode'
        })
        return attributes

    @property
    def height(self):
        # type: () -> int
        """Gets the height of this Sprite.

        Height of one thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 both are required 

        :return: The height of this Sprite.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        # type: (int) -> None
        """Sets the height of this Sprite.

        Height of one thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 both are required 

        :param height: The height of this Sprite.
        :type: int
        """

        if height is not None:
            if not isinstance(height, int):
                raise TypeError("Invalid type for `height`, type has to be `int`")

        self._height = height

    @property
    def width(self):
        # type: () -> int
        """Gets the width of this Sprite.

        Width of one thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 both are required 

        :return: The width of this Sprite.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        # type: (int) -> None
        """Sets the width of this Sprite.

        Width of one thumbnail, either height or width are required fields. If only one is given the encoder will calculate the other way value based on the aspect ratio of the video file. If the encoder version is below 2.83.0 both are required 

        :param width: The width of this Sprite.
        :type: int
        """

        if width is not None:
            if not isinstance(width, int):
                raise TypeError("Invalid type for `width`, type has to be `int`")

        self._width = width

    @property
    def unit(self):
        # type: () -> SpriteUnit
        """Gets the unit of this Sprite.


        :return: The unit of this Sprite.
        :rtype: SpriteUnit
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        # type: (SpriteUnit) -> None
        """Sets the unit of this Sprite.


        :param unit: The unit of this Sprite.
        :type: SpriteUnit
        """

        if unit is not None:
            if not isinstance(unit, SpriteUnit):
                raise TypeError("Invalid type for `unit`, type has to be `SpriteUnit`")

        self._unit = unit

    @property
    def distance(self):
        # type: () -> float
        """Gets the distance of this Sprite.

        Distance in the given unit between a screenshot

        :return: The distance of this Sprite.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        # type: (float) -> None
        """Sets the distance of this Sprite.

        Distance in the given unit between a screenshot

        :param distance: The distance of this Sprite.
        :type: float
        """

        if distance is not None:
            if not isinstance(distance, (float, int)):
                raise TypeError("Invalid type for `distance`, type has to be `float`")

        self._distance = distance

    @property
    def sprite_name(self):
        # type: () -> string_types
        """Gets the sprite_name of this Sprite.

        Name of the sprite image. File extension \".jpg\"/\".jpeg\" or \".png\" is required. (required)

        :return: The sprite_name of this Sprite.
        :rtype: string_types
        """
        return self._sprite_name

    @sprite_name.setter
    def sprite_name(self, sprite_name):
        # type: (string_types) -> None
        """Sets the sprite_name of this Sprite.

        Name of the sprite image. File extension \".jpg\"/\".jpeg\" or \".png\" is required. (required)

        :param sprite_name: The sprite_name of this Sprite.
        :type: string_types
        """

        if sprite_name is not None:
            if not isinstance(sprite_name, string_types):
                raise TypeError("Invalid type for `sprite_name`, type has to be `string_types`")

        self._sprite_name = sprite_name

    @property
    def filename(self):
        # type: () -> string_types
        """Gets the filename of this Sprite.

        Filename of the sprite image. If not set, spriteName will be used, but without an extension.

        :return: The filename of this Sprite.
        :rtype: string_types
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        # type: (string_types) -> None
        """Sets the filename of this Sprite.

        Filename of the sprite image. If not set, spriteName will be used, but without an extension.

        :param filename: The filename of this Sprite.
        :type: string_types
        """

        if filename is not None:
            if not isinstance(filename, string_types):
                raise TypeError("Invalid type for `filename`, type has to be `string_types`")

        self._filename = filename

    @property
    def vtt_name(self):
        # type: () -> string_types
        """Gets the vtt_name of this Sprite.

        Filename of the vtt-file. The file-extension \".vtt\" is required.

        :return: The vtt_name of this Sprite.
        :rtype: string_types
        """
        return self._vtt_name

    @vtt_name.setter
    def vtt_name(self, vtt_name):
        # type: (string_types) -> None
        """Sets the vtt_name of this Sprite.

        Filename of the vtt-file. The file-extension \".vtt\" is required.

        :param vtt_name: The vtt_name of this Sprite.
        :type: string_types
        """

        if vtt_name is not None:
            if not isinstance(vtt_name, string_types):
                raise TypeError("Invalid type for `vtt_name`, type has to be `string_types`")

        self._vtt_name = vtt_name

    @property
    def outputs(self):
        # type: () -> list[EncodingOutput]
        """Gets the outputs of this Sprite.


        :return: The outputs of this Sprite.
        :rtype: list[EncodingOutput]
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        # type: (list) -> None
        """Sets the outputs of this Sprite.


        :param outputs: The outputs of this Sprite.
        :type: list[EncodingOutput]
        """

        if outputs is not None:
            if not isinstance(outputs, list):
                raise TypeError("Invalid type for `outputs`, type has to be `list[EncodingOutput]`")

        self._outputs = outputs

    @property
    def images_per_file(self):
        # type: () -> int
        """Gets the images_per_file of this Sprite.

        Number of images per file. If more images are generated than specified in this value, multiple sprites will be created. You can use the placeholder '%number%' in the spriteName to specify the naming policy. Either this property must be set or hTiles and vTiles. 

        :return: The images_per_file of this Sprite.
        :rtype: int
        """
        return self._images_per_file

    @images_per_file.setter
    def images_per_file(self, images_per_file):
        # type: (int) -> None
        """Sets the images_per_file of this Sprite.

        Number of images per file. If more images are generated than specified in this value, multiple sprites will be created. You can use the placeholder '%number%' in the spriteName to specify the naming policy. Either this property must be set or hTiles and vTiles. 

        :param images_per_file: The images_per_file of this Sprite.
        :type: int
        """

        if images_per_file is not None:
            if not isinstance(images_per_file, int):
                raise TypeError("Invalid type for `images_per_file`, type has to be `int`")

        self._images_per_file = images_per_file

    @property
    def h_tiles(self):
        # type: () -> int
        """Gets the h_tiles of this Sprite.

        Number of rows of images per file.  Has to be set together with vTiles. If this property and vTiles are set, the imagesPerFile property must not be set.  It is recommended to use the placeholder '%number%' in the spriteName to allow the generation of multiple sprites.  Only supported starting with encoder version `2.76.0`. 

        :return: The h_tiles of this Sprite.
        :rtype: int
        """
        return self._h_tiles

    @h_tiles.setter
    def h_tiles(self, h_tiles):
        # type: (int) -> None
        """Sets the h_tiles of this Sprite.

        Number of rows of images per file.  Has to be set together with vTiles. If this property and vTiles are set, the imagesPerFile property must not be set.  It is recommended to use the placeholder '%number%' in the spriteName to allow the generation of multiple sprites.  Only supported starting with encoder version `2.76.0`. 

        :param h_tiles: The h_tiles of this Sprite.
        :type: int
        """

        if h_tiles is not None:
            if h_tiles is not None and h_tiles < 1:
                raise ValueError("Invalid value for `h_tiles`, must be a value greater than or equal to `1`")
            if not isinstance(h_tiles, int):
                raise TypeError("Invalid type for `h_tiles`, type has to be `int`")

        self._h_tiles = h_tiles

    @property
    def v_tiles(self):
        # type: () -> int
        """Gets the v_tiles of this Sprite.

        Number of columns of images per file.  Has to be set together with hTiles. If this property and hTiles are set, the imagesPerFile property must not be set.  It is recommended to use the placeholder '%number%' in the spriteName to allow the generation of multiple sprites.  Only supported starting with encoder version `2.76.0`. 

        :return: The v_tiles of this Sprite.
        :rtype: int
        """
        return self._v_tiles

    @v_tiles.setter
    def v_tiles(self, v_tiles):
        # type: (int) -> None
        """Sets the v_tiles of this Sprite.

        Number of columns of images per file.  Has to be set together with hTiles. If this property and hTiles are set, the imagesPerFile property must not be set.  It is recommended to use the placeholder '%number%' in the spriteName to allow the generation of multiple sprites.  Only supported starting with encoder version `2.76.0`. 

        :param v_tiles: The v_tiles of this Sprite.
        :type: int
        """

        if v_tiles is not None:
            if v_tiles is not None and v_tiles < 1:
                raise ValueError("Invalid value for `v_tiles`, must be a value greater than or equal to `1`")
            if not isinstance(v_tiles, int):
                raise TypeError("Invalid type for `v_tiles`, type has to be `int`")

        self._v_tiles = v_tiles

    @property
    def jpeg_config(self):
        # type: () -> SpriteJpegConfig
        """Gets the jpeg_config of this Sprite.

        Additional configuration for JPEG sprite generation.  If this property is set the extension of the file must be '.jpg.' or '.jpeg'  Only supported starting with encoder version `2.76.0` 

        :return: The jpeg_config of this Sprite.
        :rtype: SpriteJpegConfig
        """
        return self._jpeg_config

    @jpeg_config.setter
    def jpeg_config(self, jpeg_config):
        # type: (SpriteJpegConfig) -> None
        """Sets the jpeg_config of this Sprite.

        Additional configuration for JPEG sprite generation.  If this property is set the extension of the file must be '.jpg.' or '.jpeg'  Only supported starting with encoder version `2.76.0` 

        :param jpeg_config: The jpeg_config of this Sprite.
        :type: SpriteJpegConfig
        """

        if jpeg_config is not None:
            if not isinstance(jpeg_config, SpriteJpegConfig):
                raise TypeError("Invalid type for `jpeg_config`, type has to be `SpriteJpegConfig`")

        self._jpeg_config = jpeg_config

    @property
    def creation_mode(self):
        # type: () -> SpriteCreationMode
        """Gets the creation_mode of this Sprite.

        The creation mode for the thumbnails in the Sprite.  Two possible creation modes exist: generate thumbnails starting with the beginning of the video or after the first configured period.  When using distance=10 and unit=SECONDS and INTERVAL_END, the first image of the sprite is from the second 10 of the video. When using distance=10 and unit=SECONDS and INTERVAL_START, the first image of the sprite is from the very start of the video, while the second image is from second 10 of the video.  It is recommended to use 'INTERVAL_START' when using the sprites for trick play so that there is an additional thumbnail from the beginning of the video.  Only supported starting with encoder version `2.76.0`. 

        :return: The creation_mode of this Sprite.
        :rtype: SpriteCreationMode
        """
        return self._creation_mode

    @creation_mode.setter
    def creation_mode(self, creation_mode):
        # type: (SpriteCreationMode) -> None
        """Sets the creation_mode of this Sprite.

        The creation mode for the thumbnails in the Sprite.  Two possible creation modes exist: generate thumbnails starting with the beginning of the video or after the first configured period.  When using distance=10 and unit=SECONDS and INTERVAL_END, the first image of the sprite is from the second 10 of the video. When using distance=10 and unit=SECONDS and INTERVAL_START, the first image of the sprite is from the very start of the video, while the second image is from second 10 of the video.  It is recommended to use 'INTERVAL_START' when using the sprites for trick play so that there is an additional thumbnail from the beginning of the video.  Only supported starting with encoder version `2.76.0`. 

        :param creation_mode: The creation_mode of this Sprite.
        :type: SpriteCreationMode
        """

        if creation_mode is not None:
            if not isinstance(creation_mode, SpriteCreationMode):
                raise TypeError("Invalid type for `creation_mode`, type has to be `SpriteCreationMode`")

        self._creation_mode = creation_mode

    @property
    def aspect_mode(self):
        # type: () -> ThumbnailAspectMode
        """Gets the aspect_mode of this Sprite.

        Specifies the aspect mode that is used when both height and width are specified Only supported starting with encoder version `2.85.0`. 

        :return: The aspect_mode of this Sprite.
        :rtype: ThumbnailAspectMode
        """
        return self._aspect_mode

    @aspect_mode.setter
    def aspect_mode(self, aspect_mode):
        # type: (ThumbnailAspectMode) -> None
        """Sets the aspect_mode of this Sprite.

        Specifies the aspect mode that is used when both height and width are specified Only supported starting with encoder version `2.85.0`. 

        :param aspect_mode: The aspect_mode of this Sprite.
        :type: ThumbnailAspectMode
        """

        if aspect_mode is not None:
            if not isinstance(aspect_mode, ThumbnailAspectMode):
                raise TypeError("Invalid type for `aspect_mode`, type has to be `ThumbnailAspectMode`")

        self._aspect_mode = aspect_mode

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        if hasattr(super(Sprite, self), "to_dict"):
            result = super(Sprite, self).to_dict()
        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if value is None:
                continue
            if isinstance(value, list):
                if len(value) == 0:
                    continue
                result[self.attribute_map.get(attr)] = [y.value if isinstance(y, Enum) else y for y in [x.to_dict() if hasattr(x, "to_dict") else x for x in value]]
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = {k: (v.to_dict() if hasattr(v, "to_dict") else v) for (k, v) in value.items()}
            else:
                result[self.attribute_map.get(attr)] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Sprite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
