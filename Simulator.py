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
        return Control(5, 1)

    def setNumSides(self, n):
        """Change the number of polygon sides from the default of 5 if input is an
        integer in range [3, 10]"""
        if type(n) is int and 3 <= n <= 10:
            self.n = n

    def run(self):
        self.sec = 0
        self.msec = 0

        pose = [50, 10, 0]
        s = 10
        omega = 0

        vehicle = GroundVehicle(pose, s, omega)

        while self.sec < 100:
            act = self.getControl(self.sec, self.msec)
            vehicle.controlVehicle(act)
            vehicle.updateState(self.sec, self.msec)

            self.msec += 10
            # If millisecond counter is at or above 1000, increment second counter and reset millisecond counter
            if self.msec >= 1000:
                self.sec += 1
                self.msec = 0

if __name__ == '__main__':
    pass