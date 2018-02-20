#Matthew Luerman
#PSet 1
#8 February 2018

import unittest
import random
from Simulator import *

random.seed(125)


class TestSimulator(unittest.TestCase):
    """
    Tests for the Simulator class. Checks nominal funcitoning of each method, including edge cases and out of bounds
    cases in order to check proper responses.
    """
    def testGetCurrentSec1(self):
        """Test simulator second count is zero prior to running"""
        s = Simulator()
        self.assertEqual(s.getCurrentSec(), 0)

    def testGetCurrentSec2(self):
        """Test simulator second count is correct after 5.43 seconds of simulated time"""
        s = Simulator()
        s.time_limit = 5.430
        s.run()
        self.assertEqual(s.getCurrentSec(), 5)

    def testGetCurrentMsec1(self):
        """Test simulator millisecond count is zero prior to running"""
        s = Simulator()
        self.assertEqual(s.getCurrentMSec(), 0)

    def testGetCurrentMsec2(self):
        """Test simulator millisecond count is correct after 5.43 seconds of simulated time"""
        s = Simulator()
        s.time_limit = 5.430
        s.run()
        self.assertEqual(s.getCurrentMSec(), 440)

    def testGetControl_no_control(self):
        """Test getControl when there is no control for the given time input"""
        s = Simulator()
        self.assertEqual(s.getControl(random.randint(0,100), random.randint(0, 1000)), None)

    def testGetControl_nominal(self):
        """Tests getControl when there is a control for the given time input"""
        s = Simulator()
        new_control = Control(7, math.pi/9)
        s.control_dictionary[50.98] = new_control
        self.assertEqual(s.getControl(50, 980), new_control)

    def testGetControl_invalid_sec1(self):
        """Tests correct error raised when seconds input is wrong type"""
        s = Simulator()
        new_Control = Control(7, math.pi/9)
        s.control_dictionary[50.98] = new_Control
        with self.assertRaises(TypeError):
            s.getControl('test_input', 980)

    def testGetControl_invalid_sec2(self):
        """Tests correct error raised when seconds input is negative"""
        s = Simulator()
        new_Control = Control(7, math.pi/9)
        s.control_dictionary[50.98] = new_Control
        with self.assertRaises(ValueError):
            s.getControl(-2, 980)

    def testGetControl_invalid_msec1(self):
        """Tests correct error raised when seconds input is wrong type"""
        s = Simulator()
        new_Control = Control(7, math.pi/9)
        s.control_dictionary[50.98] = new_Control
        with self.assertRaises(TypeError):
            s.getControl(50, 'test_input')

    def testGetControl_invalid_msec2(self):
        """Tests correct error raised when milliseconds input is negative"""
        s = Simulator()
        new_Control = Control(7, math.pi/9)
        s.control_dictionary[50.98] = new_Control
        with self.assertRaises(ValueError):
            s.getControl(50, -980)

    def testSetNumSides_nominal(self):
        """Test setting number of polygon sides in the nominal case"""
        s = Simulator()
        sides = random.randint(3, 10)
        s.setNumSides(sides)
        self.assertEqual(s.n, sides)

    def testSetNumSides_high(self):
        """Test that setting the number of polygon sides does not work with too high of a number"""
        s = Simulator()
        s.setNumSides(11)
        self.assertEqual(s.n, 5)

    def testSetNumSides_low(self):
        """Test that setting the number of polygon sides does not work with too low of a number"""
        s = Simulator()
        s.setNumSides(2)
        self.assertEqual(s.n, 5)

    def testSetNumSides_edgehigh(self):
        """Test setting the number of polygon sides to the upper bound"""
        s = Simulator()
        s.setNumSides(10)
        self.assertEqual(s.n, 10)

    def testSetNumSides_edgelow(self):
        """Test setting the number of polygon sides to the lower bound"""
        s = Simulator()
        s.setNumSides(3)
        self.assertEqual(s.n, 3)

    def testSetNumSides_invalid_type(self):
        """Test that passing in a non-integer type has no effect on polygon sides"""
        s = Simulator()
        s.setNumSides(6.5)
        self.assertEqual(s.n, 5)

    def testCreateControlSequence(self):
        """Test that CreateControlSequence method creates a dictionary of Control class objects"""
        s = Simulator()
        s.createControlSequence()
        for key in s.control_dictionary.keys():
            self.assertIsInstance(s.control_dictionary[key], Control)

    def testRun(self):
        """Tests correct end state of a completed vehicle simulation for a 4 sided polygon"""
        s = Simulator()
        s.setNumSides(4)
        s.run()
        self.assertEqual(s.getCurrentSec(), 100)
        self.assertEqual(s.getCurrentMSec(), 10)
        self.assertEqual(round(s.vehicle.getPosition()[0], 2), 28.14)
        self.assertEqual(round(s.vehicle.getPosition()[1], 2), 44.52)
        self.assertAlmostEqual(s.vehicle.getPosition()[2], -math.pi/2)
        self.assertAlmostEqual(s.vehicle.getVelocity()[0], 0)
        self.assertAlmostEqual(s.vehicle.getVelocity()[1], -10)
        self.assertAlmostEqual(s.vehicle.getVelocity()[2], 0)
        self.assertEqual(s.n, 4)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimulator)
    unittest.TextTestRunner().run(suite)
