"""
Tests the atmosphere class for the Earth model
"""

import unittest
import os
import sys

import numpy as np

sys.path.append(f"{os.getcwd()}\\src")

from earth_model.atmosphere import Atmosphere


class TestAtmosphere(unittest.TestCase):
    """
    Primary Test class for the Atmosphere class
    """

    def setUp(self) -> None:

        self.atmos = Atmosphere()

    def test_get_gravitational_acceleration(self):
        """
        Tests that the correct value is returned for
        acceleration due to gravity.
        """

        test_height: float = 0

        self.assertAlmostEqual(
            np.round(self.atmos.get_graviational_acceleration(test_height), 2),
            9.80,
            places=2,
        )

    
