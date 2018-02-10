#Matthew Luerman
#PSet 1
#8 February 2018

import math


class Control:
    """
    Provides a set of controls which provide useful and common functionality for a given simulated vehicle.
    Speed constraint: 5 <= s <= 10 in m/sec
    Rotational velocity constraint: -pi/4 <= w <= pi/4 in rad/sec
    """
    def __init__(self, s, omega):
        """Initializes values for class if inputs are valid"""
        if not 5 <= s <= 10:
            raise ValueError("Speed input must be in range [5, 10] in m/sec")
        if not -math.pi/4 <= omega <= math.pi/4:
            raise ValueError("Rotational velocity input must be in range [-pi/4, pi/4] in rad/sec")
        self.s = s
        self.omega = omega

    def getSpeed(self):
        """Returns the current speed value"""
        return self.s

    def getRotVel(self):
        """Returns the current rotational velocity value"""
        return self.omega
