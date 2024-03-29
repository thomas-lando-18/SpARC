"""
Holds the class contains models relating to Earth's atmosphere
"""

class Atmosphere:
    """
    Class that is used to model the atmosphere
    """
    def __init__(self) -> None:
        # Initialise constants (probably should define this in a constants class or something)
        rho_0 = 1.225  # Air Density at SL (kg/m3)
        r_air = 287  # Specific Gas Constant of Dry Air
        m_earth = 5.97219e24  # Mass of Earth (kg)
        g_const = 6.674e-11  # Newtons Gravitational constant