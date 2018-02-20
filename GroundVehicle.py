#Matthew Luerman
#PSet 1
#8 February 2018

import math
from Control import Control
from CustomExceptions import *


class GroundVehicle:
    """
    Creates a ground vehicle capable of possessing 2-dimensional position and motion. Position and velocity variables
    can be updated, and vehicle dynamics and position can be updated based on velocity and time elapsed.
    Position constraints: 0 <= x <= 100, 0 <= y <= 100, -pi <= theta <= pi
    Speed constraint: 5 <= s <= 10
    Rotational velocity constraint: -pi/4 <= omega <= pi/4
    """
    def __init__(self, pose, s, omega):
        """Initialization of ground vehicle, invalid parameters result in ValueError"""
        if type(pose[0]) not in [int, float]:
            raise TypeError("x-position input must be an integer or float")
        if type(pose[1]) not in [int, float]:
            raise TypeError("y-position input must be an integer or float")
        if type(pose[2]) not in [int, float]:
            raise TypeError("Theta input must be an integer or float")
        if type(s) not in [int, float]:
            raise TypeError("Speed input must be an integer or float")
        if type(omega) not in [int, float]:
            raise TypeError("Omega input must be an integer or float")
        if not 0 <= pose[0] <= 100:
            raise ValueError("x-position must be in range [0, 100]")
        if not 0 <= pose[1] <= 100:
            raise ValueError("y-position must be in range [0, 100]")
        if not -math.pi <= pose[2] <= math.pi:
            raise ValueError("Theta must be in range [-pi, pi]")
        if not 5 <= s <= 10:
            raise ValueError("Speed input must be in range [5, 10] in m/sec")
        if not -math.pi/4 <= omega <= math.pi/4:
            raise ValueError("Rotational velocity input must be in range [-pi/4, pi/4] in rad/sec")
        self.pose = pose
        self.s = s
        self.omega = omega
        self.xdot = self.s * math.cos(self.pose[2])
        self.ydot = self.s * math.sin(self.pose[2])
        self.setVelocity([self.xdot, self.ydot, self.omega])
        # Check that velocity meets the speed constraint
        assert 5.0 <= (self.xdot**2 + self.ydot**2)**.5 <= 10.0

    def getPosition(self):
        """Returns the current position of the vehicle"""
        return self.pose

    def getVelocity(self):
        """Returns the current velocity of the vehicle"""
        return [self.xdot, self.ydot, self.omega]

    def clampTheta(self, theta):
        """Determine correct value of theta based on its position on a unit circle"""
        if type(theta) not in [int, float]:
            raise TypeError("Theta parameter must be an integer or float")
        # Return in range theta
        if -math.pi <= theta <= math.pi:
            return theta
        # Otherwise, find theta mod 2 pi and manipulate in as needed to maintain position on unit circle
        elif theta > math.pi:
            mod_t = theta % (math.pi * 2)
            if mod_t <= math.pi:
                return mod_t - math.pi
            elif mod_t > math.pi:
                return mod_t - (2 * math.pi)
        else:
            mod_t = theta % (math.pi * 2)
            if mod_t <= math.pi:
                return mod_t
            else:
                return mod_t - math.pi

    def setPosition(self, pose):
        """Sets the vehicle position and orientation. If any input values exceed the constraints,
        they are clamped to the nearest valid value."""
        if type(pose[0]) not in [int, float]:
            raise TypeError("x-position parameter must be an integer or float")
        if type(pose[1]) not in [int, float]:
            raise TypeError("y-position parameter must be an integer or float")
        if type(pose[2]) not in [int, float]:
            raise TypeError("Theta parameter must be an integer or float")
        self.pose = pose
        # Clamp self.pose elements if necessary
        if self.pose[0] < 0:
            self.pose[0] = 0
        elif self.pose[0] > 100:
            self.pose[0] = 100
        if self.pose[1] < 0:
            self.pose[1] = 0
        elif self.pose[1] > 100:
            self.pose[1] = 100
        # Using clamping method to set theta appropriately
        self.pose[2] = self.clampTheta(self.pose[2])
        # Check that final pose values are valid
        assert 0 <= self.pose[0] <= 100
        assert 0 <= self.pose[1] <= 100
        assert -math.pi <= self.pose[2] <= math.pi

    def setVelocity(self, vel):
        """Set the velocity of the vehicle. If the given values exceed velocity constraints,
        then velocity is clamped while maintaining the value for theta that would correspond to
        the values of xdot and ydot originally attempted."""
        if type(vel[0]) not in [int, float]:
            raise TypeError("xdot must be an integer or float")
        if type(vel[1]) not in [int, float]:
            raise TypeError("ydot must be an integer or float")
        if type(vel[2]) not in [int, float]:
            raise TypeError("omega must be an integer or float")
        self.xdot = vel[0]
        self.ydot = vel[1]
        self.omega = vel[2]
        self.s = (self.xdot**2 + self.ydot**2)**.5

        # Determine new theta based on new velocity input
        # If zero velocity, use current orientation
        if self.xdot == 0 and self.ydot == 0:
            theta = self.getPosition()[2]
        # Positive vertical motion
        elif self.xdot == 0 and self.ydot > 0:
            theta = math.pi / 2
        # Negative vertical motion
        elif self.xdot == 0 and self.ydot < 0:
            theta = -math.pi / 2
        # Positive horizontal motion
        elif self.xdot > 0 and self.ydot == 0:
            theta = 0
        # Negative horizontal motion
        elif self.xdot < 0 and self.ydot == 0:
            theta = math.pi
        # All other motion in the positive x direction
        elif self.xdot > 0:
            theta = math.atan(self.ydot / abs(self.xdot))
        # All other motion in the negative x direction
        else:
            theta = math.pi - math.atan(self.ydot / abs(self.xdot))
        # Set vehicle position (handles theta clamping as well)
        self.setPosition([self.pose[0], self.pose[1], theta])

        # If below speed bound, recalculate xdot and ydot for a speed of 5 m/s
        if self.s < 5:
            self.s = 5
            self.xdot = self.s * math.cos(theta)
            self.ydot = self.s * math.sin(theta)
        # If above speed bound, recalculate xdot and ydot for a speed of 10 m/s
        elif self.s > 10:
            self.s = 10
            self.xdot = self.s * math.cos(theta)
            self.ydot = self.s * math.sin(theta)

        # Allow epsilon tolerance for small rounding errors in speed calculation, check new velocity is valid
        eps = .000000000000001
        assert 5.0 - eps <= (self.xdot**2 + self.ydot**2)**.5 <= 10.0 + eps, "speed is not in bounds"

    def controlVehicle(self, c):
        """Updates vehicle velocity based on Control class instance"""
        if not isinstance(c, Control):
            raise TypeError("Parameter c must be an instance of the Control class")
        # Calculate new translational velocities based on speed and current pose
        self.s = c.getSpeed()
        xdot = c.getSpeed() * math.cos(self.getPosition()[2])
        ydot = c.getSpeed() * math.sin(self.getPosition()[2])
        # Use of class method will carry out any necessary clamping
        self.setVelocity([xdot, ydot, c.getRotVel()])

    def updateState(self, sec, msec):
        """Updates the pose, speed, and velocity of the vehicle after time t in seconds and milliseconds."""
        if type(sec) not in [int, float]:
            raise TypeError("Seconds parameter must be an integer or float")
        if type(msec) not in [int, float]:
            raise TypeError("Milliseconds parameter must be an integer or float")
        if sec < 0:
            raise ValueError("Seconds parameter must be nonzero")
        if msec < 0:
            raise ValueError("Milliseconds parameter must be nonzero")

        dt = sec + (msec * 0.001)
        # Do not proceed further if no time has elapsed
        if dt == 0:
            return
        # Determine current orientation of the vehicle
        dtheta = self.omega * dt
        theta = self.pose[2] + dtheta
        # Update velocity values in case speed has changed
        self.xdot = self.s * math.cos(theta)
        self.ydot = self.s * math.sin(theta)

        # Exception block just in case, but omega constraints and small time steps being used should keep the vehicle
        # far from exceeding this limit. Might help catch any egregious delta_t bugs
        if dtheta > math.pi:
            raise InvalidDynamicsInput("Model does not tolerate more than 180 degree change in heading per time step")
        elif dtheta == 0:
            # Update position for the straight line motion case
            distance = self.s * dt
            new_x = self.getPosition()[0] + (distance * math.cos(theta))
            new_y = self.getPosition()[1] + (distance * math.sin(theta))
            self.setPosition([new_x, new_y, theta])
        else:
            # Start position update by determining the radius of circular motion of the vehicle, arclength/dtheta
            radius = self.s * dt / dtheta
            # Use the law of cosines to determine chord length, c^2 = a^2 + b^2 - 2ab*cosC
            chord = math.sqrt(2 * radius**2 * (1 - math.cos(dtheta)))
            # Determine average theta from raw start and end values
            avg_theta = (self.getPosition()[2] + theta) / 2.0
            # Update position as though the vehicle moved directly along the chord line, and then update theta based on
            # the previously calculated dtheta from omega and the amount of elapsed time
            new_x = self.getPosition()[0] + (chord * math.cos(avg_theta))
            new_y = self.getPosition()[1] + (chord * math.sin(avg_theta))
            self.setPosition([new_x, new_y, theta])
