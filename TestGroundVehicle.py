#Matthew Luerman
#PSet 1
#8 February 2018

import unittest
import random
import math
from GroundVehicle import GroundVehicle

random.seed(125)


class TestGroundVehicle(unittest.TestCase):
    """
    Tests for the GroundVehicle class. Checks responses to initialization. Checks nominal funcitoning of each
    method, including edge cases and out of bounds cases in order to check proper response/clamping.
    """
    def testInputs_nominal(self):
        """Tests creation of GroundVehicle instance with valid inputs"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.pose, pose)
        self.assertEqual(g.s, s)
        self.assertEqual(g.omega, w)

    def testInputX_high(self):
        """Tests creation of GroundVehicle instance with invalid x parameter"""
        pose = [100.1, random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputX_low(self):
        """Tests creation of GroundVehicle instance with invalid x parameter"""
        pose = [-.1, random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputX_edgehigh(self):
        """Tests creation of GroundVehicle instance with edge case x parameter"""
        pose = [100, random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition()[0], pose[0])

    def testInputX_edgelow(self):
        """Tests creation of GroundVehicle instance with edge case x parameter"""
        pose = [0, random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition()[0], pose[0])

    def testInputY_high(self):
        """Tests creation of GroundVehicle instance with invalid y parameter"""
        pose = [random.uniform(0, 100), 100.1, random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputY_low(self):
        """Tests creation of GroundVehicle instance with invalid y parameter"""
        pose = [random.uniform(0, 100), -.1, random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputY_edgehigh(self):
        """Tests creation of GroundVehicle instance with edge case y parameter"""
        pose = [random.uniform(0, 100), 100, random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition()[1], pose[1])

    def testInputY_edgelow(self):
        """Tests creation of GroundVehicle instance with edge case y parameter"""
        pose = [random.uniform(0, 100), 0, random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition()[1], pose[1])

    def testInputTheta_high(self):
        """Tests creation of GroundVehicle instance with invalid theta parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), 4]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputTheta_low(self):
        """Tests creation of GroundVehicle instance with invalid theta parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), -4]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputTheta_edgehigh(self):
        """Tests creation of GroundVehicle instance with invalid theta parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), math.pi]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition()[2], pose[2])

    def testInputTheta_edgelow(self):
        """Tests creation of GroundVehicle instance with invalid theta parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), -math.pi]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition()[2], pose[2])

    def testInputS_high(self):
        """Tests creation of GroundVehicle instance with invalid s parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = 10.1
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputS_low(self):
        """Tests creation of GroundVehicle instance with invalid s parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = 4.9
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputS_edgehigh(self):
        """Tests creation of GroundVehicle instance with edge case s parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = 10
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.s, s)

    def testInputS_edgelow(self):
        """Tests creation of GroundVehicle instance with edge case s parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = 5
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.s, s)

    def testInputOmega_high(self):
        """Tests creation of GroundVehicle instance with invalid omega parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5,10)
        w = math.pi/4 + .1
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputOmega_low(self):
        """Tests creation of GroundVehicle instance with invalid omega parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5,10)
        w = -math.pi/4 - .1
        with self.assertRaises(ValueError):
            g = GroundVehicle(pose, s, w)

    def testInputOmega_edgehigh(self):
        """Tests creation of GroundVehicle instance with edge case omega parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5,10)
        w = math.pi/4
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.omega, w)

    def testInputOmega_edgelow(self):
        """Tests creation of GroundVehicle instance with edge case omega parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5,10)
        w = -math.pi/4
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.omega, w)

    def testGetPosition(self):
        """Tests nominal functioning of getPosition() method"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getPosition(), pose)

    def testGetVelocity(self):
        """Tests nominal functioning of getVelocity() method"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        self.assertEqual(g.getVelocity(), [g.xdot, g.ydot, g.omega])

    def testSetPosition_nominal(self):
        """Tests nominal functioning of setPosition() method"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), new_pose)

    def testSetPosition_high(self):
        """Tests proper functioning of setPosition() method when the input values are too high"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [100.1, 100.1, 3.2]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), [100, 100, math.pi])

    def testSetPosition_low(self):
        """Tests proper functioning of setPosition() method when the input values are too low"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [-.1, -.1, -3.2]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), [0, 0, -math.pi])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGroundVehicle)
    unittest.TextTestRunner().run(suite)