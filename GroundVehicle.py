#Matthew Luerman
#PSet 1
#8 February 2018

import math
from Control import Control


class GroundVehicle:
    """
    Constraints:
    0 <= x <= 100
    0 <= y <= 100
    -pi <= theta <= pi
    5 <= s <= 10
    -pi/4 <= omega <= pi/4
    """
    def __init__(self, pose, s, omega):
        """Initialization of ground vehicle, invalid parameters result in ValueError"""
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
        # Check that velocity meets the speed constraint
        assert 5.0 <= (self.xdot**2 + self.ydot**2)**.5 <= 10.0

    def getPosition(self):
        """Returns the current position of the vehicle"""
        return self.pose

    def getVelocity(self):
        """Returns the current velocity of the vehicle"""
        return [self.xdot, self.ydot, self.omega]

    def setPosition(self, pose):
        """Sets the vehicle position and orientation. If any input values exceed the constraints,
        they are clamped to the nearest valid value."""
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
        if self.pose[2] < -math.pi:
            self.pose[2] = -math.pi
        elif self.pose[2] > math.pi:
            self.pose[2] = math.pi
        # Check that final pose values are valid
        assert 0 <= self.pose[0] <= 100
        assert 0 <= self.pose[1] <= 100
        assert -math.pi <= self.pose[2] <= math.pi

    def setVelocity(self, vel):
        """Set the velocity of the vehicle. If the given values exceed velocity constraints,
        then velocity is clamped while maintaining the value for theta that would correspond to
        the values of xdot and ydot originally attempted."""
        self.xdot = vel[0]
        self.ydot = vel[1]
        self.omega = vel[2]
        # If velocity constraint is exceeded, clamp values
        if (self.xdot**2 + self.ydot**2)**2 < 5:
            # Determine new theta
            theta = math.atan(self.ydot/self.xdot)
            # Calculate new xdot and ydot and set theta
            self.xdot = 5 * math.cos(theta)
            self.ydot = 5 * math.sin(theta)
            self.setPosition([self.pose[0], self.pose[1], theta])
        elif (self.xdot ** 2 + self.ydot ** 2) ** 2 > 10:
            # Determine new theta
            theta = math.atan(self.ydot / self.xdot)
            # Calculate new xdot and ydot and set theta
            self.xdot = 10 * math.cos(theta)
            self.ydot = 10 * math.sin(theta)
            self.setPosition([self.pose[0], self.pose[1], theta])
        assert 5.0 <= (self.xdot**2 + self.ydot**2)**2 <= 10.0

    def controlVehicle(self, c):
        """Updates vehicle velocity based on Control class instance"""
        if not isinstance(c, Control):
            raise TypeError("Parameter c must be an instance of the Control class")
        # Calculate new translational velocities based on speed and current pose
        xdot = c.getSpeed() * math.cos(self.getPosition()[2])
        ydot = c.getSpeed() * math.sin(self.getPosition()[2])
        # Use of class method will carry out any necessary clamping
        self.setVelocity([xdot, ydot, c.getRotVel()])

    def updateState(self, sec, msec):
        dt = sec + (msec * 0.001)
        # Update position values
        self.pose[0] = self.pose[0] + (self.xdot * dt)
        self.pose[1] = self.pose[1] + (self.ydot * dt)
        self.pose[2] = self.pose[2] + (self.omega * dt)
        # Update velocity values
        self.xdot = self.s * math.cos(self.pose[2])
        self.ydot = self.s * math.sin(self.pose[2])
