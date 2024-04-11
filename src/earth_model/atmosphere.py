"""
Holds the class contains models relating to Earth's atmosphere
"""

import numpy as np


class Atmosphere:
    """
    Class that is used to model the atmosphere
    """

    def __init__(self) -> None:
        # Initialise constants (probably should define this in a constants class or something)
        self.rho_0: float = 1.225  # Air Density at SL (kg/m3)
        self.r_air: float = 287  # Specific Gas Constant of Dry Air
        self.m_earth: float = 5.97219e24  # Mass of Earth (kg)
        self.g_const: float = 6.6743e-11  # Newtons Gravitational constant
        self.r_earth: float = 6.3781e6  # average radius of earth (m)
        self.pressure_0: float = 101.325e3  # pressure at SL (Pa)
        self.scale_height: float = 8.4e3  # sclae height of atmosphere (m)

    def get_graviational_acceleration(self, height: float) -> float:
        """
        Returns the acceleration due to gravity for a given mass and height above mean sea level
        """

        # TODO In future, this model of earth should use a WGS84 ellipsoid model. pyproj

        a_g: float = self.g_const * self.m_earth / (self.r_earth + height) ** 2

        return a_g

    def get_air_density(self, height: float) -> float:
        """
        Returns estimated density value for a given height 
        """
        return self.rho_0 * np.exp(-height/10.4e3)

    def get_static_air_pressure(self, height: float) -> float:
        """
        Returns an estimated static pressure value for a given height
        """
        pressure_h: float = self.pressure_0 * np.exp(-height / self.scale_height)

        return pressure_h

    def get_dynamic_air_pressure(self, height: float, velocity: float) -> float:
        """
        returns the dynamic pressure for a given velocity and height
        """

        # use height to get density
        rho: float = self.get_air_density(height)

        # use rho to get q
        q: float = rho * velocity**2 / 2

        return q
