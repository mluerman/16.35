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
        self.ControlsSet = False
        self.control_dictionary = {}

    def getCurrentSec(self):
        """Return current seconds component of the simulator clock"""
        return self.sec

    def getCurrentMSec(self):
        """Return current milliseconds component of the simulator clock"""
        return self.msec

    def getControl(self, sec, msec):
        if type(sec) not in [int, float]:
            raise TypeError("Seconds parameter must be an integer or float")
        if type(msec) not in [int, float]:
            raise TypeError("Milliseconds parameter must be an integer or float")
        if sec < 0:
            raise ValueError("Seconds parameter must be nonzero")
        if msec < 0:
            raise ValueError("Milliseconds parameter must be nonzero")
        time = sec + (msec * 0.001)
        try:
            return self.control_dictionary[time]
        except:
            pass

    def setNumSides(self, n):
        """Change the number of polygon sides from the default of 5 if input is an
        integer in range [3, 10]"""
        if type(n) is int and 3 <= n <= 10:
            self.n = n

    def createControlSequence(self):
        """Based on the simulation constraints, builds a control dictionary with instances of the Control class to
        drive the Groundvehicle at time intervals determined within this method."""
        # Set predetermined vehicle dynamics constraints
        max_turn_rate = math.pi/4
        max_speed = 10
        min_speed = 5
        circle_radius = 25  # meters, predetermined constraint

        # Determine turn radius for vehicle at max turn rate and minimum speed
        small_circumference = min_speed * 2 * math.pi / max_turn_rate  # C = s * t = s * 2pi / omega
        small_radius = small_circumference / (2 * math.pi)
        # Determine turn time for an N-sided polygon
        turn_angle = 2*math.pi / self.n
        print('turn angle')
        print(turn_angle)
        turn_time = turn_angle / max_turn_rate
        print('turn_time')
        print(turn_time)

        # Determine drive time for straight segments of an N-sided polygon
        # Use the law of cosines to determine chord length, c^2 = a^2 + b^2 - 2ab*cosC
        big_chord = math.sqrt(2 * circle_radius ** 2 * (1 - math.cos(turn_angle)))
        # Use the law of cosines to determine chord length, c^2 = a^2 + b^2 - 2ab*cosC
        small_chord = math.sqrt(2 * small_radius ** 2 * (1 - math.cos(turn_angle)))
        linear_displacement_half_turn = (small_chord * math.cos(turn_angle)) / 2
        straight_segment_length = big_chord - linear_displacement_half_turn
        straight_segment_time = straight_segment_length / max_speed
        print('straight time')
        print(straight_segment_time)
        print('straight segment length')
        print(straight_segment_length)

        time = 0
        while True:
            self.control_dictionary[time] = Control(max_speed, 0)
            time += round(straight_segment_time, 3)
            self.control_dictionary[time] = Control(min_speed, -max_turn_rate)
            time += round(turn_time, 3)
            if time >= 100:
                self.ControlsSet = True
                break

    def run(self):
        self.sec = 0
        self.msec = 0
        delta_sec = 0  # Increment rate of seconds clock
        delta_msec = 10  # Increment rate of milliseconds clock

        # Initialize GroundVehicle instance with fixed starting inputs
        pose = [35, 20, 0]
        s = 5
        omega = 0
        vehicle = GroundVehicle(pose, s, omega)
        self.createControlSequence()

        while self.sec < 100:
            # Call getControl in order to determine if a new control should be applied to the vehicle
            new_control = self.getControl(self.sec, self.msec)
            if new_control:
                vehicle.controlVehicle(new_control)
            vehicle.updateState(delta_sec, delta_msec)

            # Print the simulator time, x and y position of GroundVehicle, and GroundVehicle orientation in degrees
            p_time = format(self.sec + (self.msec * 0.001), '.2f')
            p_x = format(vehicle.getPosition()[0], '.2f')
            p_y = format(vehicle.getPosition()[1], '.2f')
            p_theta = format(math.degrees(vehicle.getPosition()[2]), '.1f')
            # print(str(p_time) + " " + str(p_x) + " " + str(p_y) + " " + str(p_theta))

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
