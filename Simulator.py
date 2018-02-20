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
        self.time_limit = 100
        self.circle_radius = 25
        self.control_dictionary = {}

    def getCurrentSec(self):
        """Return current seconds component of the simulator clock"""
        return self.sec

    def getCurrentMSec(self):
        """Return current milliseconds component of the simulator clock"""
        return self.msec

    def getControl(self, sec, msec):
        """Returns new vehicle control if one exists for the current time input"""
        if type(sec) not in [int, float]:
            raise TypeError("Seconds parameter must be an integer or float")
        if type(msec) not in [int, float]:
            raise TypeError("Milliseconds parameter must be an integer or float")
        if sec < 0:
            raise ValueError("Seconds parameter must be nonzero")
        if msec < 0:
            raise ValueError("Milliseconds parameter must be nonzero")
        time = round(sec + (msec * 0.001), 2)
        # Check if current time is a dictionary key, do nothing if not
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
        self.circle_radius = 25  # meters, predetermined constraint

        # Determine turn radius for vehicle at max turn rate and minimum speed
        small_circumference = min_speed * 2 * math.pi / max_turn_rate  # C = s * t = s * 2pi / omega
        small_radius = small_circumference / (2 * math.pi)
        # Determine turn time for an N-sided polygon
        turn_angle = 2*math.pi / self.n
        turn_time = turn_angle / max_turn_rate

        # Determine drive time for straight segments of an N-sided polygon
        # Use the law of cosines to determine chord length, c^2 = a^2 + b^2 - 2ab*cosC
        big_chord = math.sqrt(2 * (self.circle_radius ** 2) * (1 - math.cos(turn_angle/2.0)))
        # Use the law of cosines to determine chord length, c^2 = a^2 + b^2 - 2ab*cosC
        small_chord = math.sqrt(2 * (small_radius ** 2) * (1 - math.cos(turn_angle/2.0)))
        # Determine straight segment length, to keep motion within inscribing circle, making it necessary to
        # consider linear displacement during turns (use one full turn since there is a half turn at each end)
        linear_displacement_turn = (small_chord * math.cos(turn_angle/2.0))
        # linear_displacement_turn = (small_radius * (1 - math.cos(turn_angle / 2.0)))
        straight_segment_length = big_chord*2 - linear_displacement_turn*2
        straight_segment_time = straight_segment_length / max_speed

        # Get starting positions for ground vehicle for a polygon inscribed by a circle centered at (50, 50)
        self.start_x = 50 - (straight_segment_length / 2.0)
        self.start_y = 50 - (self.circle_radius * math.cos((turn_angle)/2.0)) - (small_radius * (1 - math.cos(turn_angle / 2.0)))

        # Create control dictionary, alternating linear and curved segments spaced by previously determined time intervals
        time = 0
        while True:
            # Add a straight line segment control (linear motion at max speed)
            self.control_dictionary[round(time,2)] = Control(max_speed, 0)
            time += straight_segment_time
            # Add a turn segment control (max turn rate at slowest speed)
            self.control_dictionary[round(time,2)] = Control(min_speed, max_turn_rate)
            time += turn_time
            # Finish if controls for entire simulation have been set, otherwise loop
            if time >= self.time_limit:
                self.ControlsSet = True
                break

    def run(self):
        self.sec = 0
        self.msec = 0
        delta_sec = 0  # Increment rate of seconds clock
        delta_msec = 10  # Increment rate of milliseconds clock

        # Create control sequence dictionary
        self.createControlSequence()

        # Initialize GroundVehicle instance with starting positions determined in createControlSequence
        self.vehicle = GroundVehicle([self.start_x, self.start_y, 0], 10, 0)

        while self.sec + self.msec*.001 - .001 < self.time_limit:
            # Call getControl in order to determine if a new control should be applied to the vehicle
            new_control = self.getControl(self.sec, self.msec)
            if new_control:
                self.vehicle.controlVehicle(new_control)
            self.vehicle.updateState(delta_sec, delta_msec)

            # Print the simulator time, x and y position of GroundVehicle, and GroundVehicle orientation in degrees
            p_time = format(self.sec + (self.msec * 0.001), '.2f')
            p_x = format(self.vehicle.getPosition()[0], '.2f')
            p_y = format(self.vehicle.getPosition()[1], '.2f')
            p_theta = format(math.degrees(self.vehicle.getPosition()[2]), '.1f')
            print(str(p_time) + " " + str(p_x) + " " + str(p_y) + " " + str(p_theta))

            # Increment the simulator clock
            self.msec += delta_msec
            # If millisecond counter is at or above 1000, increment second counter and reset millisecond counter
            if self.msec >= 1000:
                self.sec += 1
                self.msec = 0

if __name__ == '__main__':
    s = Simulator()
    s.setNumSides(5)
    s.run()
