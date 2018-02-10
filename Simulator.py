#Matthew Luerman
#PSet 1
#8 February 2018

from Control import Control
from GroundVehicle import GroundVehicle
import math


class Simulator:
    """

    """
    def __init__(self):
        """Initialize simulator clock, set to zero until run() is called"""
        self.sec = 0
        self.msec = 0
        self.n = 5

    def getCurrentSec(self):
        """Return current seconds component of the simulator clock"""
        return self.sec

    def getCurrentMSec(self):
        """Return current milliseconds component of the simulator clock"""
        return self.msec

    def getControl(self, sec, msec):
        return Control(5, .3)

    def setNumSides(self, n):
        """Change the number of polygon sides from the default of 5 if input is an
        integer in range [3, 10]"""
        if type(n) is int and 3 <= n <= 10:
            self.n = n

    def run(self):
        self.sec = 0
        self.msec = 0
        delta_sec = 0  # Increment rate of seconds clock
        delta_msec = 10  # Increment rate of milliseconds clock

        # Initialize GroundVehicle instance with fixed starting inputs
        pose = [35, 10, 0]
        s = 5
        omega = 0
        vehicle = GroundVehicle(pose, s, omega)

        while self.sec < 100:
            # Call getControl in order to determine if a new control should be applied to the vehicle
            new_control = self.getControl(self.sec, self.msec)
            if new_control:
                vehicle.controlVehicle(new_control)
            vehicle.updateState(delta_sec, delta_msec)

            # Print the simulator time, x and y position of GroundVehicle, and GroundVehicle orientation in degrees
            p_time = round(self.sec + (self.msec * 0.001), 2)
            p_x = round(vehicle.getPosition()[0], 2)
            p_y = round(vehicle.getPosition()[1], 2)
            p_theta = round(math.degrees(vehicle.getPosition()[2]), 1)
            print(str(p_time) + " " + str(p_x) + " " + str(p_y) + " " + str(p_theta))

            # Increment the simulator clock
            self.msec += delta_msec
            # If millisecond counter is at or above 1000, increment second counter and reset millisecond counter
            if self.msec >= 1000:
                self.sec += 1
                self.msec = 0

if __name__ == '__main__':
    s = Simulator()
    s.setNumSides(3)
    s.run()
