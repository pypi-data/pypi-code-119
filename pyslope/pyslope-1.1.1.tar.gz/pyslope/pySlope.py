# standard library imports
from math import radians, tan, sqrt, atan, cos, sin
import time
from dataclasses import dataclass

# third party imports
import plotly.graph_objects as go
from shapely.geometry import Point, LinearRing
from tqdm import tqdm

# have to do this to allow for relative imports
# have to allow for relative imports so also works with django

# if using this file or sphinx, cant be relative
if __name__ == "__main__" or __name__ == "pySlope":
    import data_validation
    import utilities
# if running from django need to use relative
else:
    from . import data_validation
    from . import utilities

COLOUR_FOS_DICT, MATERIAL_COLORS = utilities.COLOUR_FOS_DICT, utilities.MATERIAL_COLORS

@dataclass
class Material:
    """Class representing geological material unit.

        Parameters
        ----------
        unit_weight : float
            material unit weight in kN/m3, by default 20
        friction_angle: int
            material friction angle in degrees, by default 35
        cohesion : int
            material cohesion in kPa, by default 2
        depth_to_bottom : float
            depth to the bottom of the material strata from the top 
            of the slope, by default 5. Note, materials assigned to
            a slope must have a unique depth_to_bottom or an error
            will be raised.
        name : str (optional)
            name of the strata
        color : str (optional)
            color to be used to represent the strata when plotting. Color
            may be provided as a string, standard 3 hex digit or 6 hex digit
            web compatible representation. If not provided color automatically
            assigned.        
        
        """
    unit_weight: float = 20
    friction_angle: int = 35
    cohesion: int = 2
    depth_to_bottom: float = 5
    name : str = ''
    color: str = ''

    def __post_init__(self):
        data_validation.assert_range(self.unit_weight, 'unit weight', 1, 50)
        data_validation.assert_positive_number(self.friction_angle, 'friction_angle')
        data_validation.assert_positive_number(self.cohesion, 'cohesion')
        data_validation.assert_positive_number(self.depth_to_bottom, 'depth to bottom')

        if self.name is None:
            self.name = ''
        if self.color is None:
            self.color =''
        
        assert(isinstance(self.name, str))
        assert(isinstance(self.color, str))

        # need to define seperate to color since color property is changed
        # when user defined color doesnt exist. There was a define floor
        # previously since when removing materials the color for adjecent
        # materials could become the same.
        # Comment from Jesse B, 14.03.22
        self.user_defined_color = self.color


    def __repr__(self):
        return f"Material:{self.name}(uw={self.unit_weight},phi={self.friction_angle},c={self.cohesion},d_bot={self.depth_to_bottom})"

@dataclass
class Udl:
    """Class representing uniformly distributed surface pressure in kPa
    
        Parameters
        ----------
        magnitude : float
            magnitude of UDL force in kPa
        offset : float
            offset of load from slope in m
        length : float
            length of load in m, if 0 or None then assumed continuous.
            By default None.
        color : str (optional)
            color to be used to represent the strata when plotting. Color
            may be provided as a string, standard 3 hex digit or 6 hex digit
            web compatible representation. If not provided color automatically
            assigned.
        dynamic_offset : bool   
            If True then the load offset will be dynamically moved if a "dynamic
            analysis" is run. (For a standard analysis the offset value is still used).
            By default False.       
            
            
    """
    magnitude: float = 0
    offset: float = 0
    length: float = None
    color: str = 'red'
    dynamic_offset : bool = False

    def __post_init__(self):
        data_validation.assert_positive_number(self.magnitude, 'load magnitude')
        data_validation.assert_positive_number(self.offset, 'load offset')
        if self.length:
            data_validation.assert_positive_number(self.length, 'load length')
        else:
            # make none if length = 0?
            self.length = None

        self.precision = utilities.get_precision(self.magnitude)

        if not utilities.is_color(self.color):
            self.color ='red'

    def __repr__(self):
        return f"UDL: {self.magnitude} kPa, offset = {self.offset} m, load length = {self.length} m"

@dataclass
class LineLoad:
    """Class representing line load in kN/m
    
        Parameters
        ----------
        magnitude : float
            magnitude of UDL force in kPa
        offset : float
            offset of load from slope in m
        length : float
            length of load in m, if 0 or None then assumed continuous.
            By default None.
        color : str (optional)
            color to be used to represent the strata when plotting. Color
            may be provided as a string, standard 3 hex digit or 6 hex digit
            web compatible representation. If not provided color automatically
            assigned.
        dynamic_offset : bool   
            If True then the load offset will be dynamically moved if a "dynamic
            analysis" is run. (For a standard analysis the offset value is still used).
            By default False.    
    """
    magnitude: float = 0
    offset: float = 0
    color: str = 'blue'
    dynamic_offset : bool = False

    def __post_init__(self):
        data_validation.assert_positive_number(self.magnitude, 'load magnitude')
        data_validation.assert_positive_number(self.offset, 'load offset')

        self.precision = utilities.get_precision(self.magnitude)

        if not utilities.is_color(self.color):
            self.color ='blue'

    def __repr__(self):
        return f"Line: {self.magnitude} kN/m, offset = {self.offset} m"

class Slope:
    """Slope object.

        Parameters
        ----------
        height : float
            height of slope in metres, by default 2
        angle : int, optional
            angle of slope (only used if length None), by default 30
        length : float, optional
            length of slope in metres, by default None
    """

    def __repr__(self):
        return f"Slope: {round(self._height,3)}V : {round(self._length,3)}H"

    def __init__(self, height: float = 1, angle: int = 30, length: float = None):

        # initialise empty properties used in other components of class
        self._materials = []
        self._water_RL = None
        self._udls = []
        self._lls = []

        self._external_boundary = None

        # intialise options
        self.update_boundary_options(MIN_EXT_H=6, MIN_EXT_L=10)
        self.set_external_boundary(height=height, angle=angle, length=length)
        self.update_analysis_options(slices=50, iterations=2500, min_failure_dist = 0, gradient_tolerance=8)

        self.update_water_analysis_options(auto=True)

        # sets default analysis limits (ie no limit)
        self.remove_analysis_limits()

    @utilities.reset_results
    def set_external_boundary(
        self, height: float = 2, angle: int = 30, length: float = None
    ):
        """Set external boundary for model.

        Parameters
        ----------
        height : float, optional
            height of slope in metres, by default 2
        angle : int, optional
            angle of slope in degrees (may be left as none if slope
            is instead expressed by length of slope), by default 30
        length : float, optional
            length of slope in metres (may be left as none if slope
            is instead expressed by angle of slope), by default None

        Raises
        ------
        ValueError
            If input not in required range or of required type
        """

        # validate inputs
        data_validation.assert_strictly_positive_number(height, "height")
        if angle is not None:
            # is allowed to be 90 but not 0
            data_validation.assert_range(angle, "angle", 0, 90, not_low=True)
        if length is not None:
            data_validation.assert_positive_number(length, "length")

        # if angle assigned instead of length work out the model length
        if length is None:
            if not angle:
                raise ValueError(
                    "require angle of slope or length of slope to initialise"
                )
            length = height / tan(radians(angle))

        MIN_EXT_H = self._MIN_EXT_H
        MIN_EXT_L = self._MIN_EXT_L

        tot_h = max(3 * height, MIN_EXT_H, 5 * length / 2)
        tot_l = max(5 * length, MIN_EXT_L, 4 * height)

        # determine coordinates for edges of slope
        dx = (tot_l - length) / 2
        top = (dx, tot_h)
        bot = (dx + length, tot_h - height)

        # set up external boundary as a shapely LinearRing
        self._external_boundary = LinearRing(
            [(0, 0), (0, top[1]), top, bot, (tot_l, bot[1]), (tot_l, 0), (0, 0)]
        )

        # set relevant variables to self
        self._length = length
        self._height = height

        if angle == 90 or length == 0:
            self._gradient = 10000000
        else:
            self._gradient = height / length

        self._top_coord = top
        self._bot_coord = bot

        self._external_length = self._external_boundary.bounds[2]
        self._external_height = self._external_boundary.bounds[3]

        # udl coordinates can be effected by external boundary modification
        # need to update coordinates.
        self._update_udl_coordinates()
        self._update_pl_coordinates()

    @utilities.reset_results
    def set_water_table(self, depth: float):
        """set water table value.
        
        Parameters
        ----------
        depth : float
            depth of water from top of slope.
        """

        if depth is None:
            self.remove_water_table()
        else:
            data_validation.assert_positive_number(depth, "water depth")
            self._water_RL = max(0, self._top_coord[1] - depth)

    @utilities.reset_results
    def remove_water_table(self):
        """Remove water table from model"""
        self._water_RL = None

    @utilities.reset_results
    def set_udls(self, *udls):
        """set a surface surcharge on top of the slope.

        Parameters
        ----------
        *udls : Udl objects
            Udl object to be assigned to the slope object.
        """


        for udl in udls:
            if isinstance(udl, Udl):
                if udl.magnitude > 0:
                    self._udls.append(udl)

        self._update_udl_coordinates()
        
        if self._udls:
            self._udl_max = max(udl.magnitude for udl in self._udls)

    # dont need to reset results since this only should be called
    # as a part of resetting
    def _update_udl_coordinates(self):
        "Update coordinates for left and right of udl based on external boundary and Udl object"

        for udl in self._udls:
            
            right_x = self._top_coord[0] - udl.offset
            if udl.length:
                left_x = max(0, right_x - udl.length)
            else:
                left_x = 0
            
            udl.left = left_x
            udl.right = right_x

    @utilities.reset_results
    def remove_udls(self, *udls, remove_all = False):
        """Remove udl from model if associated with model.

        Parameters
        ----------
        *udls : Udl objects
            Udl object to be removed from the slope object.
        remove_all : bool, optional
            If true remove all udls, by default False
        """

        for udl in udls:
            for check_udl in self._udls:
                if (
                    check_udl.offset == udl.offset and
                    check_udl.magnitude == udl.magnitude and
                    check_udl.length == udl.length
                ):
                    self._udls.remove(check_udl)

        self._udl_max = max(self._udls, key= lambda x : x.magnitude)

        if remove_all:
            self._udls = []
            self._udl_max = 0
   
    @utilities.reset_results
    def set_lls(self, *lls):
        """set a surface surcharge on top of the slope
        
        *lls : LineLoad objects
            LineLoad object to be assigned to the slope object.
            
        """

        for pl in lls:
            if isinstance(pl, LineLoad):
                if pl.magnitude > 0:
                    self._lls.append(pl)

        self._update_pl_coordinates()

    # dont need to reset results since this only should be called
    # as a part of resetting
    def _update_pl_coordinates(self):
        "Update coordinates for point load based on external boundary and LineLoad object"

        for pl in self._lls:
            coord = max(0,self._top_coord[0]-pl.offset)

            pl.coord = coord

    @utilities.reset_results
    def remove_lls(self, *lls, remove_all = False):
        """Remove udl from model if associated with model.

        Parameters
        ----------
        *lls : LineLoad objects
            LineLoad object to be removed from the slope object.
        remove_all : bool, optional
            if true remove all lls, by default False
        """

        # can probably write this as O(n) rather than O(n^2)
        for pl in lls:
            for check_pl in self._lls:
                if (
                    check_pl.offset == pl.offset and
                    check_pl.magnitude == pl.magnitude
                ):
                    self._lls.remove(check_pl)

        if remove_all:
            self._lls = []

    @utilities.reset_results
    def set_materials(self, *materials):
        """Assign material instances to the slope instance.

        Parameters
        ----------
        *materials : Material (list), optional
            Material instances to be associated with slope.


        Raises
        ------
        ValueError
            If material not instance of Material class error is raised.
        ValueError
            If non-unique material depths then error is raised.
        """

        # check material object entered
        for material in materials:
            if not isinstance(material, Material):
                raise ValueError(
                    "The function add_materials only accepts instances of the Material Class"
                )

        # Need to validate material values also

        # sort materials to be in order, include existing materials
        materials = list(materials) + self._materials
        materials.sort(key=lambda x: x.depth_to_bottom)

        depths = [material.depth_to_bottom for material in materials]

        # if geological unit deeper than model than extend model to fit materials
        if depths[-1] > self._external_height:
            self.update_boundary_options(MIN_EXT_H=depths[-1])

        # check material depth unique
        if len(depths) > len(set(depths)):
            raise ValueError("The same material depth has been input twice")

        material_refined = []
        # define RL for each material and color for each material
        for i, material in enumerate(materials):
            material.RL = self._external_height - material.depth_to_bottom

            if utilities.is_color(material.user_defined_color) and material.user_defined_color!='':
                material.color = material.user_defined_color
            else:
                material.color = MATERIAL_COLORS[i%10]

            material_refined.append(material)

        self._materials = material_refined

    @utilities.reset_results
    def remove_material(self, material: Material = None, depth: float = None, remove_all=False):
        """Remove material from slope.

        Parameters
        ----------
        material : Material, optional
            material object. If specified and exists in materials
            associated with slope then will be removed, by default None
        depth : float, optional
            depth in metres of material object. If not None and material found
            at indicated depth then will remove the material, by default None
        remove_all : Boolean, optional
            if true all materials removed, default false

        """
        # general note: depth used to remove object rather than directly removing
        # even when material class provided because a user might reinitialise
        # an object with the same details but if the pointer is changed than
        # it might be confusing for the user as to why they cant remove.
        # Comment by Jesse B, 14.03.2022.

        # if material defined and material type is Material set depth to be depth of material
        if material and isinstance(material, Material):
            depth = material.depth_to_bottom

        # if depth specified adopt
        if depth:
            for m in self._materials:
                if m.depth_to_bottom == depth:
                    self._materials.remove(m)
                    break

        if remove_all:
            self._materials = []

    @utilities.reset_results
    def update_water_analysis_options(self,auto : bool = True,H : int = 1):
        """Update analysis options regarding how water is treated.

        Parameters
        ----------
        auto : bool, optional
            If true calculates pressure head automatically (factor is cos(a)**2 where a is
            the angle of slope). If False takes manual factor (H). by default True
        H : int, optional
            factor on water pressure. If 1 water head equals distance between water
            table and bottom of slice. If 0 no water pressure is considered. By default 1.
        """

        if auto:
            a = atan(self._gradient)
            H = cos(a)**2

        else:
            data_validation.assert_number(H, 'H')
            if H > 1:
                H = 1
            elif H < 0:
                H = 0

        self._water_analysis_H = H

    @utilities.reset_results
    def update_analysis_options(
        self,
        slices: int = None,
        iterations: int = None,
        min_failure_dist: int = None,
        gradient_tolerance : int = None,
    ):
        """Function to update analysis modelling options.

        Parameters
        ----------
        slices : int, optional
            Slices to take in calculation for each potential
            circular failureIf None doesnt update the parameter, by default None
        iterations : int, optional
            Approximate number of potential slopes to check.
            If None doesnt update the parameter, by default None
        min_failure_distance : int, optional
            If specified only failure slopes with a distance greater than the
            min failure distance will be assessed, by default None.
        gradient_tolerance : int, none
            The maximum value of gradient denominator allowed before failure is 
            no longer considered from the top of the slope, by default None.
        """
        if slices:
            data_validation.assert_range(slices, "slices", 10, 500)
            self._slices = slices
        if iterations:
            data_validation.assert_range(iterations, "iterations", 1000, 100000)
            self._iterations = iterations
        if min_failure_dist is not None:
            data_validation.assert_positive_number(min_failure_dist, 'min failure distance')
            if min_failure_dist > self._external_length:
                print('min failure distance should not be greater than the length of the model. Check Value.')
            self._min_failure_distance = min(min_failure_dist, self._external_length * 0.9)
        if gradient_tolerance and isinstance(gradient_tolerance, int):
            data_validation.assert_positive_number(gradient_tolerance, 'gradient tolerance')
            self._gradient_tolerance = gradient_tolerance


    @utilities.reset_results
    def update_boundary_options(
        self,
        MIN_EXT_L: float = None,
        MIN_EXT_H: float = None,
    ):
        """Function to update external boundary options.

        Parameters
        ----------
        MIN_EXT_L : float, optional
            Minimum external boundary length. If None doesnt update
            the parameter, by default None
        MIN_EXT_H : float, optional
            Minimum external boundary height. If None doesnt update
            the parameter, by default None.
        """

        if MIN_EXT_H:
            data_validation.assert_strictly_positive_number(
                MIN_EXT_H, "Minimum external model height (MIN_EXT_H)"
            )
            self._MIN_EXT_H = MIN_EXT_H
        if MIN_EXT_L:
            data_validation.assert_strictly_positive_number(
                MIN_EXT_L, "Minimum external model length (MIN_EXT_H)"
            )
            self._MIN_EXT_L = MIN_EXT_L

        # if the external boundary has been set this call is after init. Can update the boundary.
        # otherwise will get an error
        if self._external_boundary is not None:
            self.set_external_boundary(height=self._height, length=self._length)

    @utilities.reset_results
    def remove_analysis_limits(self):
        """Reset analysis limits to default (no limits). """
        self.set_analysis_limits(
            left_x = 0,
            right_x_left = 0,
            right_x = self._external_length,
            left_x_right = self._external_length,
        )

    @utilities.reset_results
    def set_analysis_limits(
        self,
        left_x: float = None,
        right_x: float = None,
        left_x_right: float = None,
        right_x_left: float = None,
    ):
        """set limits on slope analysis search.

        Parameters
        ----------
        left_x : float
            left x coordinate of search, defines outer edge
            of top of search
        right_x : float
            right x coordinate search, defines outer edge of
            bottom of search
        left_x_right : float, optional
            left x coordinate right hand limit of search, defines
            inner edge of top of search. If none ignored, by default None
        right_x_left : float, optional
            right x coordinate left hand limit of search, defines
            inner edge of bottom of search. If none ignored, by default None
        """
        # if only one of the double paremets is defined
        # the other should be set up to equal it
        # or the diagram is confusing
        if left_x_right is not None and right_x_left is None:
            right_x_left = max(self._limits[1][0], left_x_right)

        if right_x_left is not None and left_x_right is None:
            left_x_right = min(self._limits[0][1], right_x_left)

        # set to current model values if not set
        if left_x is None:
            left_x = self._limits[0][0]
        if left_x_right is None:
            left_x_right = self._limits[0][1]
        if right_x_left is None:
            right_x_left = self._limits[1][0]
        if right_x is None:
            right_x = self._limits[1][1]

        # check correct value entered
        data_validation.assert_positive_number(left_x, "left_x limit")
        data_validation.assert_strictly_positive_number(right_x, "right_x_limit")
        data_validation.assert_strictly_positive_number(right_x_left, "right_x left coordinate")
        data_validation.assert_strictly_positive_number(left_x_right, "left_x right coordinate")

        # check the numbers are in the correct ascending order.
        # note: it is okay for the inner limits to overlap. They look at seperate things.
        if left_x > right_x:
            raise ValueError(
                f"right_x ({right_x}) should be greater than left_x ({left_x}), i cant assign these limits"
            )

        if right_x_left > right_x:
            raise ValueError(
                f"right_x ({right_x}) should be greater than right_x left ({right_x_left}), i cant assign these limits"
            )

        if left_x_right < left_x:
            raise ValueError(
                f"left_x ({left_x}) should be less than left_x right ({left_x_right}), i cant assign these limits"
            )

        # check that the left x is on slope
        if left_x >= self._bot_coord[0]:
            raise ValueError(
                f"left_x ({left_x}) should be < bottom of slope coordinate ({self._bot_coord[0]}"
            )
        # check that righ x is on bottom slope or slope
        if right_x <= self._top_coord[0]:
            raise ValueError(
                f"right_x ({right_x}) should be > top slope coordinate ({self._top_coord[0]})"
            )

        self._limits = [(left_x, left_x_right), (right_x_left, right_x)]

        if right_x_left == 0 and left_x_right == self._external_length:
            self._number_limits = 2
        else:
            self._number_limits = 4


    def analyse_slope(self):
        """Analyse many possible failure planes for a slope.  """

        # Approximate number of runs and distribution of searches
        ITERATIONS = self._iterations

        # number of different radii to consider for the same end points
        NUMBER_CIRCLES = max(5, int(ITERATIONS / 1000))

        # number of different end points to consider
        NUMBER_POINTS_SLOPE = max(5, int(ITERATIONS / 800))

        # generate coordinates for left of slope
        point_combinations = ITERATIONS / NUMBER_CIRCLES

        NUMBER_POINTS = self._calculate_number_points_slope(point_combinations, NUMBER_POINTS_SLOPE)
        
        # get limits on bounds of slope
        # not some limits might still stretch off slope
        # but <= check later considers this.
        x1, x2, x3, x4 = (
            min(self._top_coord[0], self._limits[0][0]),
            min(self._top_coord[0], self._limits[0][1]),
            max(self._bot_coord[0], self._limits[1][0]),
            max(self._bot_coord[0], self._limits[1][1]),
        )

        y2, y3 = self._top_coord[1], self._bot_coord[1]

        # split top and bottom slope up into 10 coordinate points
        if x2 != x1:
            left_coords = [
                (x1 + (n / (NUMBER_POINTS-1)) * (x2 - x1), y2) for n in range(NUMBER_POINTS)
            ]
        else:
            left_coords =[]

        if x3 != x4:
            right_coords = [
                (x3 + (n / (NUMBER_POINTS-1)) * (x4 - x3), y3) for n in range(NUMBER_POINTS)
            ]
        else:
            right_coords =[]

        # ignore crest if too steep (gradient tolerance exceeded)
        if self._gradient > self._gradient_tolerance:
            left_coords = left_coords[:-1]


        # only want lines from mid to right for a not very steep gradient
        # if x2 ! > x1 then limit off of slope
        # NOTE: we dont want the end points since we already grabbed those in left and right coords.
        if self._gradient < self._gradient_tolerance and x2 >= x1:
            left_mid_coords = [x1 + (x2-x1)*(i/(NUMBER_POINTS_SLOPE+1)) for i in range(1,NUMBER_POINTS_SLOPE+1)]
            left_coords += [(x, self.get_external_y_intersection(x)) for x in left_mid_coords]

        # if x4 ! > x3 then limit off of slope
        if x4 >= x3:
            right_mid_coords = [x3 + (x4-x3)*(i/(NUMBER_POINTS_SLOPE+1)) for i in range(1,NUMBER_POINTS_SLOPE+1)]
            right_coords += [(x, self.get_external_y_intersection(x)) for x in right_mid_coords]

        search = []

        min_dist = self._min_failure_distance

        # loop through left and right coordinates and generate a circular slope
        # that passes through these points
        # Not sure if multiprocessing can help, always made it slightly slower for all my tests

        for l_c in tqdm(left_coords):
            for r_c in right_coords:
                if utilities.dist_points(l_c, r_c) > min_dist:
                    search += self.run_analysis_for_circles(l_c, r_c, NUMBER_CIRCLES)

        search.sort(key = lambda x : x['FOS'])
        self._search = search

        self._min_FOS_dict = search[0]

    def run_analysis_for_circles(
        self, l_c: tuple, r_c: tuple, NUMBER_CIRCLES: float = 5
    ) -> list:
        """Runs slope analyse for fixed left and right points for
        a number of possible circular failures.

        Parameters
        ----------
        l_c : tuple,
            left coordinate written in the form (x,y)
        r_c : tuple
            right coordinate written in the form (x,y)
        NUMBER_CIRCLES : int, optional
            Number of circular slopes to break the area into
            (although some potential slopes might not be generated),
            by default 5

        Returns
        -------
        list
            list of dictionaries of searched results
        """

        # data validation
        data_validation.assert_strictly_positive_number(NUMBER_CIRCLES, "NUMBER_CIRCLES")
        NUMBER_CIRCLES = int(NUMBER_CIRCLES)

        data_validation.assert_length(l_c, 2, "l_c")
        data_validation.assert_length(r_c, 2, "r_c")

        # assume a starting circle that has a straight vertical slope down at the top of the slope
        # this means the centre of the circle is in line with the top of the slope
        # since the tangent of the circle is perpendicular to the centre

        # angle of slope of choord (For circular slope)
        beta = atan((l_c[1] - r_c[1]) / (r_c[0] - l_c[0]))

        # half of the circle coord that passess from top of point to bottom of point
        half_coord_distance = sqrt((l_c[1] - r_c[1]) ** 2 + (r_c[0] - l_c[0]) ** 2) / 2

        # starting circle details
        start_radius = half_coord_distance / cos(beta)
        # start_centre = (l_c[0] + start_radius, l_c[1])
        start_chord_to_centre = sqrt(start_radius**2 - half_coord_distance**2)
        start_chord_to_edge = start_radius - start_chord_to_centre

        # two intersecting chords through circle have segments of chords related
        # as a * b = c * d , where a and b are the lengths of chord on each side of intersection
        # as such we have half_coord_distance ** 2 = chord_to_edge * (R + (R-chord_to_edge)) = C
        C = half_coord_distance**2

        # loop through circles
        search = []

        for i in range(0, NUMBER_CIRCLES):

            # doesnt include going all the way in which we dont want to do anyways
            chord_to_edge = start_chord_to_edge * (NUMBER_CIRCLES - i) / NUMBER_CIRCLES
            radius = utilities.circle_radius_from_abcd(chord_to_edge, C)
            centre = utilities.circle_centre(
                beta=beta,
                chord_intersection=utilities.mid_coord(l_c, r_c),
                chord_to_centre=radius - chord_to_edge,
            )
            c_x, c_y = centre

            result = self.analyse_circular_failure(c_x, c_y, radius, l_c, r_c)
            if result:
                FOS, i_l, i_r = result
                if ((self._limits[0][1] < i_l[0] < self._limits[1][0]) or 
                   (self._limits[0][1] < i_r[0] < self._limits[1][0])):
                    break
                search += [{
                    'FOS': FOS,
                    'l_c': i_l,
                    'r_c': i_r,
                    'c_x': c_x,
                    'c_y': c_y,
                    'radius': radius,
                    }]
            else:
                break

        return search

    def analyse_circular_failure(self, c_x: float, c_y: float, radius: float, l_c = None, r_c = None):
        """Calculate factor of safety for a circular failure plane through the slope.

        Parameters
        ----------
        c_x : float
            circle center x coordinate
        c_y : float
            circle center y coordinate
        radius : float
            circle radius
        l_c : tuple, optional
            coordinates of left intersection between boundary and
            failure plane if already known, by default None.
        r_c : tuple, optional
            coordinates of left intersection between boundary and
            failure plane if already known, by default None.


        Returns
        -------
        float
            factor of safety
        None
            if cant calculate returns None

        """
        # data validation
        data_validation.assert_strictly_positive_number(c_x, "c_x (circle x coordinate)")
        data_validation.assert_strictly_positive_number(c_y, "c_y (circle y coordinate)")
        data_validation.assert_strictly_positive_number(radius, "radius")

        i_list = self._get_circle_external_intersection(c_x, c_y, radius, l_c, r_c)
        if len(i_list) < 2:
            return None
        # total number of slices
        SLICES = self._slices

        # horizontal distance between left and right slice
        dist = i_list[1][0] - i_list[0][0]

        # width of a slice
        b = dist / SLICES

        if b <= 0.000001:
            return None

        # initialise centre point of first slice
        s_x = i_list[0][0] + b / 2

        # intialise the push and resistance components for FOS before looping
        pushing = 0.0
        resisting = 0.0

        # loop through slices
        for _ in range(0, SLICES):
            # define y coordinates for slice bottom
            s_yb = c_y - sqrt(radius**2 - (s_x - c_x) ** 2)

            # get y coordinate at slice top
            s_yt = self.get_external_y_intersection(s_x)
            
            # out of bounds
            if s_yt is None:
                return None

            # get alpha, dy always positive, dx negative to right (uphill), dx positive to left
            # note alpha in radians by default
            dy = c_y - s_yb
            dx = c_x - s_x
            alpha = atan(dx / dy)

            # get length
            l = b / cos(alpha)

            # calculate strip weight
            W = self._calculate_strip_weight(b, s_yt, s_yb)

            # get material properties at the bottom of the slice
            bottom_material = self._get_material_at_depth(s_yb)

            cohesion = bottom_material.cohesion
            friction_angle = bottom_material.friction_angle

            # if there is a udl load on the strip apply it.
            for udl in self._udls:
                W += self._calculate_strip_udl_force(b, s_x, udl)

            # if there is a point load on the strip apply it.
            for pl in self._lls:
                W += self._calculate_strip_pl(b, s_x, pl)

            # consideration for water
            if self._water_RL:
                # determine H factor based on setting
                # https://www.rocscience.com/help/slide2/documentation/slide-model/material-properties/define-material-properties/water-parameters

                # only use H factor if on the slope, otherwise use 1
                if self._top_coord[0] < s_x < self._bot_coord[0]:
                    U = max(min(self._water_RL, s_yt) - s_yb, 0) * 9.81 * l * self._water_analysis_H
                else:
                    U = max(min(self._water_RL, s_yt) - s_yb, 0) * 9.81 * l * 1
            else:
                U = 0

            # calculate resisting
            resisting += cohesion * l + max(0, (W * cos(alpha) - U)) * tan(
                radians(friction_angle)
            )

            # calculate pushing
            pushing += W * sin(alpha)

            # initialise slice x coordinate for next loop
            s_x = s_x + b

        if pushing <= 0:
            return None

        return (resisting / pushing, i_list[0], i_list[1])

    def analyse_dynamic(self, critical_fos=1.3):
        """Analyse slope and offset dynamic loads until critical FOS is achieved

        Parameters
        ----------
        critical_fos : float, optional
            minimum required factor of safety, by default 1.3
        """
        self._dynamic_results = {}

        # check case for load at right and load at left before
        # trying to converge on position
        right = 0
        left = self._length-0.01

        # check for extreme case with loads at crest (right)
        # if slope is safe (FOS high) then return
        self._set_dynamic_offset(right)
        self.analyse_slope()
        fos = self.get_min_FOS()
        self._dynamic_results[right] = fos
        if fos > critical_fos:
            return 0

        # check for extreme case with loads at end of slope as far away from crest (left)
        # If slope is unsafe (FOS still low) then return
        self._set_dynamic_offset(left)
        self.analyse_slope()
        fos = self.get_min_FOS()
        self._dynamic_results[left] = fos
        if fos < critical_fos:
            return 1

        # If neither of the previous results was true find the intermediate point
        # where the critical FOS is reached
        # offset for left shouldnt be more then the point that the slope started failing from
        # in the worse case
        #left = self.get_min_FOS_end_points()[0][0]

        previous_fos = 0

        # converge
        for _ in range(10):
            # # check midpoint for FOS
            # midpoint = (left + right) / 2

            # let midpoint be weighted value based on FOS
            left_fos = self._dynamic_results[left]
            right_fos = self._dynamic_results[right]

            m = (left_fos - right_fos)/(left-right)
            midpoint = right + (critical_fos-right_fos) / m

            self._set_dynamic_offset(midpoint)
            self.analyse_slope()
            fos = self.get_min_FOS()
            self._dynamic_results[midpoint] = fos

            # check if load is within the zone of influence, if last two FOS are identical
            # then probably not
            if previous_fos != fos:
                if abs(previous_fos - fos) <= 0.01 and round(fos,3) >= critical_fos and abs(fos-critical_fos)<=0.03:
                    return 2

            # If FOS high then move closer to cliff
            if fos < critical_fos:
                right = midpoint
            else:
                left = midpoint

            previous_fos = fos

    def _set_dynamic_offset(self, offset):
        # remember default values?
        udls = self._udls
        lls = self._lls

        # remove loads
        self.remove_udls(remove_all=True)
        self.remove_lls(remove_all=True)

        # update loads
        for udl in udls:
            if udl.dynamic_offset:
                udl.offset = offset
            self.set_udls(udl)

        for pl in lls:
            if pl.dynamic_offset:
                pl.offset = offset
            self.set_lls(pl)

    def _get_circle_external_intersection(self, c_x: float, c_y: float, radius: float, l_c = None, r_c = None):
        """Get intersection points of a circle with external boundary

        Parameters
        ----------
        c_x : float
            circle x coodinate
        c_y : float
            circle y coordinate
        radius : float
            circle radius
        l_c : tuple, optional
            coordinates of left intersection between boundary and
            failure plane if already known, by default None.
        r_c : tuple, optional
            coordinates of left intersection between boundary and
            failure plane if already known, by default None.

        Returns
        -------
        tuple
            tuple of two coordinates (left coordinate, right coordinate)
        """
        # if left and right intersection provided only need to check if cuts through middle of
        # the slope.
        if l_c and r_c:
            i_list = [l_c, r_c]
            mid_intersection = utilities.cirle_line_intersection(self._top_coord, self._bot_coord,c_x,c_y,radius)
            for a in mid_intersection:
                if a[0] >= self._top_coord[0] and a[0] <= self._bot_coord[0]:
                    if abs(a[0]-l_c[0]) > 0.1:
                        i_list.append(a)

            i_list.sort(key=lambda x : x[0])
            return i_list
        
        i_list = []
        
        top_intersection = utilities.cirle_line_intersection(
            (0,self._top_coord[1]), 
            self._top_coord,
            c_x, c_y, radius
            )

        # only care about left of circle for top intersection
        # since failure from left to right always
        if top_intersection:
            top_intersection.sort()
            top_intersection = top_intersection[0]
            if top_intersection[0] >= 0 and top_intersection[0] <= self._top_coord[0]:
                i_list.append(top_intersection)

        bot_intersection = utilities.cirle_line_intersection(
            self._bot_coord, 
            (self._external_length, self._bot_coord[1]),
            c_x, c_y, radius
            )

        # only care about right of circle for bottom intersection
        # since failure will always be to right of cirle on bottom
        # unless failure cuts through slope (in which case value of toe
        # will be picked up for mid intersection anyways)
        if bot_intersection:
            bot_intersection.sort()
            bot_intersection = bot_intersection[-1]       
            if bot_intersection[0] >= self._bot_coord[0] and bot_intersection[0] <= self._external_length:
                i_list.append(bot_intersection)

        mid_intersection = utilities.cirle_line_intersection(self._top_coord, self._bot_coord,c_x,c_y,radius)

        for a in mid_intersection:
            if a[0] >= self._top_coord[0] and a[0] <= self._bot_coord[0]:
                i_list.append(a)

        # remove any close points
        i_list.sort(key=lambda x : x[0])
        unique_list = []
        x = -1
        for i in i_list:
            if abs(i[0] - x) > 0.1:
                unique_list.append(i)
            x = i[0]

        return unique_list


    def _calculate_strip_weight(self, b : float, s_yt : float, s_yb : float):
        """calculates the weight of a strip.

        Parameters
        ----------
        b : float
            strip width in metres
        s_yt : float
            strip y coordinate at top of strip
        s_yb : float
            strip y coordinate at bottom of strip

        Returns
        -------
        float
            Weight of strip in kN.
        """

        # intialize properties
        W = 0.0  # kN
        top = s_yt

        # loop through materials noting that they are already sorted by depth
        for m in self._materials:
            # while layers are higher than the top of the slice ignore the material
            if m.RL > s_yt:
                continue
            # while the bottom of layer is in the slice consider, go from the
            # current top to the bottom of the layer
            # this captures the case of the top of the strip being partially in a layer
            elif m.RL < s_yt and m.RL > s_yb:
                W += b * m.unit_weight * (top - m.RL)
                top = m.RL
            # in the case that the bottom of the strip is now outside the range
            # we still have material between the current top and the bottom of the strip
            # we capture it in this edge case and then break since everything below can be ignored
            # we also grab the material properties at the base
            else:
                W += b * m.unit_weight * (top - s_yb)
                top = m.RL
                break

        # check case that ran out of layers (loop terminated earlier than expected)
        if top > s_yb:
            m = self._materials[-1]
            W += b * m.unit_weight * (top - s_yb)

        return W

    def _get_material_at_depth(self, s_yb):
        """Return the material class at a specified depth.

        Parameters
        ----------
        s_yb : float
            strip y coordinate at bottom of strip

        Returns
        -------
        Material
            material object at the specified depth.
        """

        # loop through all materials, if we have passed the bottom take the previous
        for m in self._materials:
            if m.RL < s_yb:
                return m

        return self._materials[-1]

    def _calculate_strip_udl_force(self, b, s_x, udl):
        """Calculates the udl force over strip.

        Parameters
        ----------
        b : float,
            strip width in m
        s_x : float,
            strip x coordinate (for center of strip)
        udl : Udl object,
            udl object

        Returns
        -------
        float
            udl force on strip in kN
        """
        W = 0

        load_xl, load_xr = udl.left, udl.right
        strip_xl = s_x - (b / 2)
        strip_xr = s_x + (b / 2)

        # case 1 clearly load is completely inside
        if load_xl <= strip_xl and load_xr >= strip_xr:
            W += b * udl.magnitude
        # case 2 on the left inside the load
        elif strip_xl <= load_xl and strip_xr >= load_xl:
            W += (strip_xr - load_xl) * udl.magnitude

        # case 3 on the right side of the load
        elif strip_xl <= load_xr and strip_xr >= load_xr:
            W += (load_xr - strip_xl) * udl.magnitude

        return W

    def _calculate_strip_pl(self, b, s_x, pl):
        """Calculates the pl force over strip.

        Parameters
        ----------
        b : float,
            strip width in m
        s_x : float,
            strip x coordinate (for center of strip)
        pl : LineLoad object,
            LineLoad object

        Returns
        -------
        float
            udl force on strip in kN
        """

        strip_xl = s_x - (b / 2)
        strip_xr = s_x + (b / 2)

        # Need just one comparison to be equal to or greater than so that
        # in the case the point load is excatly at the boundary
        # two adjcent strips wont double up or ignore completely.
        if strip_xl <= pl.coord < strip_xr:
            return pl.magnitude
        else:
            return 0

    def _calculate_number_points_slope(self, point_combinations, NUMBER_POINTS_SLOPE):
        """_summary_

        Parameters
        ----------
        point_combinations : int
            total number of slope coordinate groups to reach target number
            of iterations
        NUMBER_POINTS_SLOPE : int
            number of points to be added to slope

        Returns
        -------
        int
            number points for top and bottom of slope
        """
        # if deep seeded or limits exclude the slope
        if (
            self._limits[0][1] < self._top_coord[0] and
            self._limits[1][0] > self._bot_coord[0]
            ):
            NUMBER_POINTS = int(sqrt(point_combinations))

        # if limits exclude slope only in one direction
        elif (
            self._limits[0][1] < self._top_coord[0] or
            self._limits[1][0] > self._bot_coord[0]
            ):
            P = point_combinations
            N = NUMBER_POINTS_SLOPE

            NUMBER_POINTS = int((-N + sqrt( N**2 + 4 * P ))/2 )

        else:
            if self._gradient > self._gradient_tolerance:
                NUMBER_POINTS = (
                    int(
                        (
                            NUMBER_POINTS_SLOPE
                            + sqrt(NUMBER_POINTS_SLOPE**2 + 4 * point_combinations)
                        )
                        / 2
                    )
                    - NUMBER_POINTS_SLOPE
                )
            else:
                NUMBER_POINTS = int(sqrt(point_combinations)) - NUMBER_POINTS_SLOPE

        return NUMBER_POINTS

    def get_dynamic_results(self):
        return self._dynamic_results

    def print_dynamic_results(self):
        for k,v in self.get_dynamic_results().items():
            print('Offset:', round(k,3), ' m, FOS:', round(v,3))

    def get_min_FOS(self):
        """Get min factor of safety for slope model.

        Returns
        -------
        float
            critical factor of safety
        """
        return self._min_FOS_dict['FOS']

    def get_min_FOS_circle(self):
        """Get the properties of the circle that gave the critical factor of safety.

        Returns
        -------
        tuple
            tuple containing (circle x coordinate, circle y coordinate, circle radius)
        """
        c_x = self._min_FOS_dict['c_x']
        c_y = self._min_FOS_dict['c_y']
        radius = self._min_FOS_dict['radius']
        return (c_x, c_y, radius)

    def get_min_FOS_end_points(self):
        """Get the external boundary intersection for the slope that gave the critical factor of safety.

        Returns
        -------
        tuple
            tuple containing (left coordinate, right coordinate)
        """
        l_c = self._min_FOS_dict['l_c']
        r_c = self._min_FOS_dict['r_c']
        return (l_c, r_c)

    def get_external_y_intersection(self,x):
        """ return y coordinate of intersection with boundary for a given x """
        if x < 0 or x > self._external_length:
            return None
        # y is below the bottom of the slope
        elif x <= self._top_coord[0]:
            return self._top_coord[1]
        elif x >= self._bot_coord[0]:
            return self._bot_coord[1]
        # y is above the bottom of the slope
        else:
            return self._top_coord[1] - (x - self._top_coord[0]) * self._gradient

    def get_external_x_intersection(self,y):
        """ return x coordinate of intersection with boundary for a given y """
        # y is below the bottom of the slope
        if y < self._bot_coord[1]:
            return self._external_length

        # y is above the bottom of the slope
        elif y < self._external_height:
            return self._top_coord[0] + (self._top_coord[1] - y) / self._gradient

        elif y == self._bot_coord[1]:
            return self._bot_coord[0]
        
        elif y == self._top_coord[1]:
            return self._top_coord[0]

        else:
            return None

    def plot_boundary(self, material_table=True, legend=False):
        """Plot external boundary, materials, limits, loading and water for model.

        Returns
        -------
        plotly figure

        """
        # draw the external boundary
        x_, y_ = self._external_boundary.coords.xy
        fig = go.Figure(go.Scatter(x=list(x_), y=list(y_), mode="lines",name=''))

        fig.update_layout(width=2000, height=1200)

        # following makes sure x and y are scaled the same, so that
        # model can be interpretted properly
        fig.update_yaxes(
            scaleanchor="x",
            scaleratio=1,
        )

        # dont show legend
        fig.update_layout(
            showlegend=False,
        )

        # if there are no materials just return an empty shell
        if not self._materials:
            return fig

        # get the points representing the top line of the model
        # to help with drawing materials
        top = self._external_boundary.coords[1:3]

        # length of model (max x coordinate)
        tot_l = self._external_length
        num_materials = len(self._materials)

        # loop through materials
        for i, m in enumerate(self._materials):
            # get reference level (y coordinate) for material
            y = m.RL
            x = self.get_external_x_intersection(y)

            line = [(0, y), (x, y)]

            # if the bot slope coordinate is between the bounds of the material
            # OR LAST material and above need to draw a bit differently

            is_last = i == num_materials - 1

            if (top[1][1] >= self._bot_coord[1] and line[1][1] < self._bot_coord[1]) or (
                is_last and top[1][1] > self._bot_coord[1]
            ):
                top.append(self._bot_coord)
                top.append((tot_l, self._bot_coord[1]))

            # if we are at the last material make the bottom the bottom of the model
            if i == num_materials - 1:
                bot = self._external_boundary.coords[-2:]
            else:
                bot = line

            # change bottom coordinates to be right to left
            # so points are arranged clockwise in a circle
            bot = sorted(bot, reverse=True)

            # get coordinates
            coords = top + bot
            x_ = [a[0] for a in coords]
            y_ = [a[1] for a in coords]

            fig.add_trace(
                go.Scatter(
                    x=list(x_), y=list(y_),
                    mode="lines",
                    meta = [m.unit_weight, m.cohesion, m.friction_angle,m.name],
                    fill="toself",
                    name=f'{m.name}<br>γ: {m.unit_weight} kN/m3<br>c: {m.cohesion} kPa<br>ϕ: {m.friction_angle} degrees',
                    hovertemplate="",
                    fillcolor = m.color
                )
            )

            # set the new top as the bottom, sort to put it back
            # to left to right order
            bot.sort()
            top = bot

        if material_table:
            fig = self._plot_material_table(fig)
        
        if legend:
            fig = self._plot_FOS_legend(fig)

        for udl in self._udls:
            fig = self._plot_udl(fig, udl)

        for pl in self._lls:
            fig = self._plot_pl(fig, pl)

        if self._water_RL:
            fig = self._plot_water(fig)

        fig = self._plot_limits(fig)


        return fig

    def plot_critical(self, material_table=True, legend=False):
        """Plot critical slope (i.e. slope with lowest FOS)

        Returns
        -------
        Plotly figure
        """
        fig = self.plot_boundary(material_table=material_table,legend=legend)

        FOS = self._min_FOS_dict['FOS']
        c_x = self._min_FOS_dict['c_x']
        c_y = self._min_FOS_dict['c_y']
        radius = self._min_FOS_dict['radius']
        l_c = self._min_FOS_dict['l_c']
        r_c = self._min_FOS_dict['r_c']

        fig = self._plot_failure_plane(
            fig, c_x, c_y, radius, l_c, r_c, FOS=FOS, show_center=True
        )
        fig = self._plot_annotate_FOS(fig, c_x, c_y, FOS)
        return fig

    def plot_all_planes(self, max_fos: float = 10, material_table=True, legend=True):
        """plot multiple failure planes in the same plot

        Parameters
        ----------
        max_fos : float, optional
            maximum factor of safety to display for planes,
            by default 10.

        Returns
        -------
        plotly figure

        """

        fig = self.plot_critical(material_table=material_table, legend=legend)

        data_validation.assert_strictly_positive_number(max_fos, "max factor of safety (max_fos)")


        fig = self._plot_FOS_legend(fig)

        # JB 20.04.22 - 'hacked' into how plotly works to make faster
        # ultimately not very readible approach compared to the old approach
        # however old approach was too slow
        traces = []

        for i in tqdm(self._search):

            FOS = i['FOS']
            if FOS < max_fos:

                c_x = i['c_x']
                c_y = i['c_y']
                radius = i['radius']
                l_c = i['l_c']
                r_c = i['r_c']

                    
                if FOS > 3:
                    color = COLOUR_FOS_DICT[3.0]
                else:
                    color = COLOUR_FOS_DICT[round(FOS, 1)]

                # generate points for circle, will always generate 64 points (65 in list since start and end are same)
                p = Point(c_x, c_y)
                x, y = p.buffer(radius).boundary.coords.xy

                # empty vectors for circle points that we will actually include
                x_ = []
                y_ = []

                # 65 long list but the last half of points are for the top half of
                # circle and so will never actually be required.
                for i in range(34):
                    # x coordinate should be between left and right
                    # note for y, should be less than left y but can stoop
                    # below right i
                    if x[i] <= r_c[0] and x[i] >= l_c[0] and y[i] <= l_c[1]:
                        x_.append(x[i])
                        y_.append(y[i])

                x_ = [r_c[0]] + x_ + [l_c[0]]
                y_ = [r_c[1]] + y_ + [l_c[1]]

                traces.append(
                    {
                        'hovertemplate': '%{meta[0]}',
                        'line': {'color': color},
                        'meta': [round(FOS,3)],
                        'mode': 'lines',
                        'name': '',
                        'x': x_,
                        'y': y_,
                        'type': 'scatter'
                    }
                )

       
        traces.reverse()
        
        temp = fig.to_dict()
        temp['data'] = tuple(list(temp['data']) + traces)
       
        return go.Figure(temp)


    def _plot_annotate_FOS(self, fig, c_x: float, c_y: float, FOS: float):
        """Annotate FOS on figure.

        Parameters
        ----------
        fig : plotly figure
        c_x : float
            circle center x coordinate.
        c_y : float
            circle center y coordinate.
        FOS : float
            circle factor of safety to be annotated to figure.

        Returns
        -------
        Plotly figure.
        """

        # validate inputs
        data_validation.assert_strictly_positive_number(c_x, "circle center x coordinate")
        data_validation.assert_strictly_positive_number(c_y, "circle center y coordinate")
        data_validation.assert_strictly_positive_number(FOS, "Factor of safety")

        if FOS > 3:
            color = COLOUR_FOS_DICT[3.0]
        else:
            color = COLOUR_FOS_DICT[round(FOS, 1)]

        fig.add_trace(
            go.Scatter(
                x=[c_x],
                y=[c_y],
                mode="lines+text",
                text=[f"{FOS:.3f}"],
                textposition="top right",
                textfont=dict(family="sans serif", size=20, color=color),
                name='',
            )
        )

        return fig

    def _plot_water(self, fig):
        """Add water table to plot"""

        if self._water_RL == None:
            return fig

        y = self._water_RL
        x = self.get_external_x_intersection(y)

        x_line = [0, x]
        y_line = [y, y]

        # if x is less than bot slope then is also same as saying x is less than the edge of the model.
        # basically need to make sure the water table continues along the surface
        # as is conservatively considered in the model
        if x <= self._bot_coord[0]:
            x_line += [self._bot_coord[0], self._external_length]
            y_line += [self._bot_coord[1], self._bot_coord[1]]

        fig.add_trace(
            go.Scatter(
                x=x_line,
                y=y_line,
                mode="lines",
                line_color="blue",
                line_width=4,
                name='',
            )
        )

        fig.add_annotation(
            x=self._top_coord[0] / 4,
            y=y,
            text="▼",
            showarrow=False,
            yshift=10,
            font_size=25,
            font_color="blue",
        )

        fig.add_annotation(
            x=self._top_coord[0] / 4,
            y=y,
            text="_",
            showarrow=False,
            yshift=2,
            font_size=25,
            font_color="blue",
        )

        return fig

    def _plot_limits(self, fig):
        """Add analysis limits to plot """

        l1_x, l2_x = self._limits[0]
        r1_x, r2_x = self._limits[1]

        l1_y = self.get_external_y_intersection(l1_x)
        l2_y = self.get_external_y_intersection(l2_x)
        r1_y = self.get_external_y_intersection(r1_x)
        r2_y = self.get_external_y_intersection(r2_x)

        points_right = [(l1_x, l1_y)]
        points_left = [(r2_x, r2_y)]

        if self._number_limits == 4:
            points_right += [(r1_x, r1_y)]
            points_left += [(l2_x, l2_y)]

        # add outer limits
        for p in points_right:
            fig.add_annotation(
                x=p[0],
                y=p[1],
                text="▶",
                showarrow=False,
                yshift=15,
                xshift=-10,
                font_size=25,
                font_color="black",
            )

        for p in points_left:
            fig.add_annotation(
                x=p[0],
                y=p[1],
                text="◀",
                showarrow=False,
                yshift=15,
                xshift=10,
                font_size=25,
                font_color="black",
            )

        for p in points_left + points_right:
            fig.add_annotation(
                x=p[0],
                y=p[1],
                text="|",
                showarrow=False,
                yshift=15,
                xshift=0,
                font_size=25,
                font_color="black",
            )

        return fig

    def _plot_pl(self, fig, pl):
        """Add pointload to plot"""


        fig = utilities.draw_arrow(
            fig,
            angle = -90,
            force = pl.magnitude,
            x_sup = pl.coord,
            y_sup = self._top_coord[1],
            color = 'black',
            arrowlength= 150,
            show_values = True,
            precision= pl.precision,
            units='kN/m',
            arrowhead=10,
        )

        fig = utilities.draw_arrow(
            fig,
            angle = -90,
            force = pl.magnitude,
            x_sup = pl.coord,
            y_sup = self._top_coord[1],
            color = pl.color,
            arrowlength= 150,
            show_values = False,
            units='kN/m',
            arrowhead=10,
        )


        return fig

    def _plot_udl(self, fig, udl):
        """Add Uniform load to plot"""

        fig = utilities.draw_arrow(
            fig,
            angle = -90,
            force = udl.magnitude,
            x_sup = udl.left,
            y_sup = self._top_coord[1],
            color = udl.color,
            arrowlength= 100 * (udl.magnitude / self._udl_max),
            show_values = False,
            units='kN',
            arrowhead=10,
            precision=udl.precision,
        )

        fig = utilities.draw_arrow(
            fig,
            angle = -90,
            force = udl.magnitude,
            x_sup = (udl.left+udl.right)/2,
            y_sup = self._top_coord[1],
            color = 'black',
            arrowlength= 100 * (udl.magnitude / self._udl_max)+10,
            show_values = True,
            precision=udl.precision,
            units='kPa',
            arrowhead=0,
            line_width=0,
        )

        fig = utilities.draw_arrow(
            fig,
            angle = -90,
            force = udl.magnitude,
            x_sup = udl.right,
            y_sup = self._top_coord[1],
            color = udl.color,
            arrowlength= 100 * (udl.magnitude / self._udl_max),
            show_values = False,
            units='kN',
            arrowhead=10,
        )

        # Draw in line above arrows
        y0 = 100 * (udl.magnitude / self._udl_max)

        shape = dict(
            type="line",
            xref="x", yref="y",
            x0=udl.left, y0=y0, x1=udl.right, y1=y0,
            line_color=udl.color, line_width=2,
            ysizemode='pixel',
            xanchor=udl.left, yanchor=self._top_coord[1])

        fig.add_shape(shape)

        # draw in rectangular area
        shape = dict(
            type="rect",
            xref="x", yref="y",
            x0=udl.left, y0=0, x1=udl.right, y1=y0,
            fillcolor=udl.color,
            opacity=0.2,
            line_width=2,
            ysizemode='pixel',
            xanchor=udl.left, yanchor=self._top_coord[1])

        fig.add_shape(shape)

        return fig

    def _plot_material_table(self, fig):
        """Plot table of material properties"""


        row_h = 0.05
        table_width = 0.4
        table_height = row_h * (len(self._materials)+1)

        # points at the bottom left
        x0, y0 = 0.1,0.1

        # points at the top right
        x1 = x0 + table_width
        y1 = y0 + table_height

        # add header background
        fig.add_shape(
            type="rect",
            xref="x domain", yref="y domain",
            x0=x0, x1=x1, y0=y1-row_h, y1=y1,
            fillcolor='lightgrey',
        )

        # add background
        fig.add_shape(
            type="rect",
            xref="x domain", yref="y domain",
            x0=x0, x1=x1, y0=y0, y1=y1-row_h,
            fillcolor='white'
        )

        # add columns in
        column_unit_positions = [20,15,10,10,10]
        column_rel_positions = []

        total_width = sum(column_unit_positions)

        column_text_unit_xshift = [1,1,4,4,4]
        assumed_graph_width = 1000
        column_rel_xshift = [a/total_width * assumed_graph_width * table_width for a in column_text_unit_xshift]


        

        cum_width = 0
        for col_width in column_unit_positions:
            # get unit position (ie position as percentage of total width)
            column_rel_position = (cum_width + col_width) / total_width
            column_rel_positions.append(column_rel_position)

            cum_width += col_width

            # add in column based on unit position
            x = x0 + column_rel_position *(table_width)

            fig.add_shape(
                type="rect",
                xref="x domain", yref="y domain",
                x0=x, x1=x, y0=y0, y1=y1,
            )


        # add in header text
        table_header = ['MATERIAL','COLOR','γ', "c", "ϕ"]
        table_header = ['<b>'+a+'</b>' for a in table_header]

        x = x0
        for i, c in enumerate(column_rel_positions):
            fig.add_annotation(
                xref="x domain", yref="y domain",
                x=x,
                y=y1-row_h/2,
                text=table_header[i],
                showarrow=False,
                yshift=-13,
                xshift=column_rel_xshift[i],
                font_size=13,
                font_color="black",
            )
            x = x0+c*(table_width)

        # add rows
        for r in range(len(self._materials)):
            y = y1 - row_h - r * row_h

            fig.add_shape(
                type="rect",
                xref="x domain", yref="y domain",
                x0=x0, x1=x1, y0=y, y1=y,
            )

        # add material info

        y = y1-row_h/2
        
        for p, m in enumerate(self._materials):
            x = x0
            y -= row_h
            data = [m.name, 'red', m.unit_weight, m.cohesion, m.friction_angle]

            for i, c in enumerate(column_rel_positions):
                if i==1:
                    fig.add_shape(
                        type="rect",
                        xref="paper", yref="paper",
                        x0=x, x1=x0+column_rel_positions[1]*(table_width),
                        y0=y-row_h/2, y1=y+row_h/2,
                        fillcolor= m.color,
                    )
                else:
                    fig.add_annotation(
                        xref="x domain", yref="y domain",
                        x=x,
                        y=y,
                        text=data[i],
                        showarrow=False,
                        yshift=-13,
                        xshift=column_rel_xshift[i],
                        font_size=13,
                        font_color="black",
                    )
                x = x0+c*(table_width)

        return fig

    def _plot_FOS_legend(self, fig):
        """Plot color legend for factor of safety colors"""

        yi = 0.9
        yf = 0.5

        x0 = 0.9
        x1 = 0.95

        max_fos = max(COLOUR_FOS_DICT)

        fig.add_shape(
            type="rect",
            xref="paper", yref="paper",
            x0=x0-0.02, x1=x1+0.05, y0=yi+0.05, y1=yf-0.03,
            fillcolor='white'
        )

        for k,v in COLOUR_FOS_DICT.items():
            fig.add_shape(type='rect',
                xref="paper", yref="paper",
                x0=x0,
                x1=x1,
                y0=yi+k*(yf-yi)/max_fos,
                y1=yi+(k+0.1)*(yf-yi)/max_fos,
                fillcolor=v,
                line = dict(
                    color='black',
                    width=0.2,
                )
            )

            if round(k,1) % 1 == 0:

                # bandaid fix because i cant figure out why the scale shows wrong
                if k < 1.5:
                    y = float(yi)+float(k-0.05)*float(yf-yi)/float(max_fos)
                else:
                    y = float(yi)+float(k+0.05)*float(yf-yi)/float(max_fos)

                fig.add_annotation(
                    xref="paper", yref="paper",
                    x=x1,
                    y=y,
                    text=f"{k}",
                    showarrow=False,
                    yshift=0,
                    xshift=37,
                    font_size=16,
                    font_color="black",
                )

        # add top description
        fig.add_annotation(
            xref="paper", yref="paper",
            x=(x0+x1)/2,
            y=yi,
            text=f"<b>Legend</b>",
            align='center',
            showarrow=False,
            yshift=33,
            xshift=60,
            font_size=20,
            font_color="black",
        )



        return fig

    def _plot_failure_plane(
        self,
        fig,
        c_x: float,
        c_y: float,
        radius: float,
        l_c: tuple,
        r_c: tuple,
        FOS: float,
        show_center=False,
    ):
        """Add failure plane to plot.

        Parameters
        ----------
        fig : plotly figure
            plotly figure to have information added to.
        c_x : float
            failure plane circle center x coordinate.
        c_y : float
            failure plane circle center y coordinate.
        radius : float
            failure plane circle radius
        l_c : tuple
            left intersection point between failure plane and external boundary.
        r_c : tuple
            right intersection point between failure plane and external boundary.
        FOS : float
            Factor of safety of slope (used in coloring drawn failure plane)
        show_center : bool, optional
            If true will project to the center of circle and show, by default false.

        Returns
        -------
        plotly figure
        """

        # data validation
        data_validation.assert_strictly_positive_number(c_x, "circle center x coordinate")
        data_validation.assert_strictly_positive_number(c_y, "circle center y coordinate")
        data_validation.assert_strictly_positive_number(radius, "radius")
        data_validation.assert_length(l_c, 2, "l_c")
        data_validation.assert_length(r_c, 2, "r_c")
        data_validation.assert_strictly_positive_number(FOS, "Factor of safety")

        if FOS > 3:
            color = COLOUR_FOS_DICT[3.0]
        else:
            color = COLOUR_FOS_DICT[round(FOS, 1)]

        # generate points for circle, will always generate 64 points (65 in list since start and end are same)
        p = Point(c_x, c_y)
        x, y = p.buffer(radius).boundary.coords.xy

        # empty vectors for circle points that we will actually include
        x_ = []
        y_ = []

        # 65 long list but the last half of points are for the top half of
        # circle and so will never actually be required.
        for i in range(34):
            # x coordinate should be between left and right
            # note for y, should be less than left y but can stoop
            # below right i
            if x[i] <= r_c[0] and x[i] >= l_c[0] and y[i] <= l_c[1]:
                x_.append(x[i])
                y_.append(y[i])

        if show_center:
            x_ += [l_c[0], c_x, r_c[0], x_[0]]
            y_ += [l_c[1], c_y, r_c[1], y_[0]]
        else:
            x_ = [r_c[0]] + x_ + [l_c[0]]
            y_ = [r_c[1]] + y_ + [l_c[1]]

        # THIS IS TOO SLOW (in experimentation the real
        # problem is with plotly, even with minimal data
        # adding everything in is slow)
        fig.add_trace(
            go.Scatter(
                x=x_,
                y=y_,
                mode="lines",
                line_color=color,
                meta=[round(FOS, 3)],
                hovertemplate="%{meta[0]}",
                name='',
            )
        )

        return fig


if __name__ == "__main__":


    start = time.time()

    s = Slope(height=3, angle=30, length=None)

    m1 = Material(unit_weight=20,friction_angle=45,cohesion=2,depth_to_bottom=2, name='Fill', color='blue')
    m2 = Material(20,30,2,5, name = 'sand', color='orange')

    u1 = Udl(magnitude = 100, offset=2, length=1, dynamic_offset=True, color='red')
    u2 = Udl(magnitude = 20, color='green')

    p1 = LineLoad(10,3, 'purple')

    s.set_udls(u1, u2)
    s.set_lls(p1)

    s.set_materials(m1,m2)

    s.set_water_table(4)

    s.update_water_analysis_options(auto=True)

    s.update_analysis_options(slices=50, iterations=10000)    

    print('takes this long to initialise:')
    print(time.time()-start)
    start = time.time()
    