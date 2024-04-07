"""
Holds the class contains models relating to Earth's atmosphere
"""

class Atmosphere:
    """
    Class that is used to model the atmosphere
    """
    def __init__(self) -> None:
        # Initialise constants (probably should define this in a constants class or something)
        self.rho_0 = 1.225  # Air Density at SL (kg/m3)
        self.r_air = 287  # Specific Gas Constant of Dry Air
        self.m_earth = 5.97219e24  # Mass of Earth (kg)
        self.g_const = 6.674e-11  # Newtons Gravitational constant
        self.r_earth = 6371e3  # average radius of earth (m)

    def get_graviational_acceleration(self, height: float) -> float:
        """
        Returns the acceleration due to gravity for a given mass and height above mean sea level
        """

        # TODO In future, this model of earth should use a WGS84 ellipsoid model.

        a_g: float = self.g_const * self.m_earth / (self.r_earth + height) ** 2

        return a_g

    def get_air_density(self, height: float) -> float:
        """
        """
        return self.rho_0