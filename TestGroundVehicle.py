#Matthew Luerman
#PSet 1
#8 February 2018

import unittest
import random
import math
from GroundVehicle import GroundVehicle
from Control import Control

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

    def testInputX_invalid(self):
        """Tests creation of GroundVehicle instance with invalid x parameter"""
        pose = [[123], random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(TypeError):
            g = GroundVehicle(pose, s, w)

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

    def testInputY_invalid(self):
        """Tests creation of GroundVehicle instance with invalid y parameter"""
        pose = [random.uniform(0, 100), [123], random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(TypeError):
            g = GroundVehicle(pose, s, w)

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

    def testInputTheta_invalid(self):
        """Tests creation of GroundVehicle instance with invalid theta parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), [123]]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(TypeError):
            g = GroundVehicle(pose, s, w)

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

    def testInputS_invalid(self):
        """Tests creation of GroundVehicle instance with invalid s parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = True
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(TypeError):
            g = GroundVehicle(pose, s, w)

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

    def testInputOmega_invalid(self):
        """Tests creation of GroundVehicle instance with invalid omega parameter"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = False
        with self.assertRaises(TypeError):
            g = GroundVehicle(pose, s, w)

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

    def testClampTheta_wrongtype(self):
        """Tests that clamping function raises type error when invalid input is entered"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        with self.assertRaises(TypeError):
            g.clampTheta('invalid input test')

    def testClampTheta_no_clamping(self):
        """Tests clamping function when no clamping is needed"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(math.pi/8)
        self.assertEqual(new_theta, math.pi/8)

    def testClampTheta_clamp_high1(self):
        """Tests clamping function when input is above the upper bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(3.2)
        self.assertEqual(new_theta, -2 * math.pi + 3.2)

    def testClampTheta_clamp_high2(self):
        """Tests clamping function when input is above the upper bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(10)
        self.assertEqual(new_theta, -math.pi + (10 - math.pi * 3))

    def testClampTheta_clamp_low1(self):
        """Tests clamping function when theta is below the lower bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(-3.2)
        self.assertEqual(new_theta, 2 * math.pi - 3.2)

    def testClampTheta_clamp_low2(self):
        """Tests clamping function when theta is below the lower bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(-11.5)
        self.assertEqual(new_theta, math.pi + (-11.5 + 3 * math.pi))

    def testClampTheta_clamp_edgehigh(self):
        """Tests clamping function at upper boundary"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(math.pi)
        self.assertEqual(new_theta, math.pi)

    def testClampTheta_clamp_edgelow(self):
        """Tests clamping function at lower boundary"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_theta = g.clampTheta(-math.pi)
        self.assertEqual(new_theta, -math.pi)

    def testSetPosition_nominal(self):
        """Tests nominal functioning of setPosition() method"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), new_pose)

    def testSetPosition_x_invalid(self):
        """Tests that an error is raised when the x element type is invalid"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [[123], random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        with self.assertRaises(TypeError):
            g.setPosition(new_pose)

    def testSetPosition_y_invalid(self):
        """Tests that an error is raised when the y element type is invalid"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [random.uniform(0, 100), [123], random.uniform(-math.pi, math.pi)]
        with self.assertRaises(TypeError):
            g.setPosition(new_pose)

    def testSetPosition_theta_invalid(self):
        """Tests that an error is raised when the theta element type is invalid"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [random.uniform(0, 100), random.uniform(0, 100), [123]]
        with self.assertRaises(TypeError):
            g.setPosition(new_pose)

    def testSetPosition_high(self):
        """Tests proper functioning of setPosition() method when the input values are too high"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [100.1, 100.1, 3.2]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), [100, 100, -2*math.pi+3.2])

    def testSetPosition_low(self):
        """Tests proper functioning of setPosition() method when the input values are too low"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [-.1, -.1, -3.2]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), [0, 0, 2*math.pi-3.2])

    def testSetPosition_edgehigh(self):
        """Tests proper functioning of setPosition() method at the upper bound of inputs"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [100, 100, math.pi]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), new_pose)

    def testSetPosition_edgelow(self):
        """Tests proper functioning of setPosition() method at the lower bound of inputs"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_pose = [0, 0, -math.pi]
        g.setPosition(new_pose)
        self.assertEqual(g.getPosition(), new_pose)

    def testSetVelocity_xdot_invalid(self):
        """Tests proper functioning of setVelocity() method when the xdot input is an invalid type"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = ['invalid input', random.uniform(5, 10), random.uniform(-math.pi/4, math.pi/4)]
        with self.assertRaises(TypeError):
            g.setVelocity(new_vel)

    def testSetVelocity_ydot_invalid(self):
        """Tests proper functioning of setVelocity() method when the ydot input is an invalid type"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [random.uniform(5, 10), 'invalid input', random.uniform(-math.pi/4, math.pi/4)]
        with self.assertRaises(TypeError):
            g.setVelocity(new_vel)

    def testSetVelocity_omega_invalid(self):
        """Tests proper functioning of setVelocity() method when the omega input is an invalid type"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [random.uniform(5, 10), random.uniform(5, 10), 'invalid input']
        with self.assertRaises(TypeError):
            g.setVelocity(new_vel)

    def testSetVelocity_zero_input(self):
        """Tests setVeloctiy method when both numerical inputs are zero. Vehicle goes to min speed for previous theta."""
        pose = [random.uniform(0, 100), random.uniform(0, 100), math.pi/2]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [0, 0, 0]
        g.setVelocity(new_vel)
        self.assertAlmostEqual(g.getVelocity()[0], 0)
        self.assertEqual(g.getVelocity()[1], 5)
        self.assertEqual(g.getVelocity()[2], new_vel[2])

    def testSetVelocity_x_only(self):
        """Tests nominal functioning of setVeloctiy method with only an x velocity input"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [random.uniform(5, 10), 0, random.uniform(-math.pi/4, math.pi/4)]
        g.setVelocity(new_vel)
        self.assertEqual(g.getVelocity(), new_vel)

    def testSetVelocity_x_only_low(self):
        """Tests nominal functioning of setVeloctiy method with only an x velocity input below the lower bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [-2.5, 0, random.uniform(-math.pi/4, math.pi/4)]
        g.setVelocity(new_vel)
        self.assertAlmostEqual(g.getVelocity()[0], -5)
        self.assertAlmostEqual(g.getVelocity()[1], new_vel[1])
        self.assertAlmostEqual(g.getVelocity()[2], new_vel[2])

    def testSetVelocity_x_only_high(self):
        """Tests nominal functioning of setVeloctiy method with only an x velocity input above the upper bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [10.1, 0, random.uniform(-math.pi/4, math.pi/4)]
        g.setVelocity(new_vel)
        self.assertAlmostEqual(g.getVelocity()[0], 10)
        self.assertAlmostEqual(g.getVelocity()[1], new_vel[1])
        self.assertAlmostEqual(g.getVelocity()[2], new_vel[2])

    def testSetVelocity_y_only(self):
        """Tests nominal functioning of setVelocity method with only a y velocity input"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), math.pi/2]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [0, random.uniform(5, 10), random.uniform(-math.pi/4, math.pi/4)]
        g.setVelocity(new_vel)
        self.assertEqual(g.getVelocity(), new_vel)

    def testSetVelocity_y_only_low(self):
        """Tests nominal functioning of setVelocity method with only a y velocity input below the lower bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), math.pi/2]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [0, 4.9, random.uniform(-math.pi/4, math.pi/4)]
        g.setVelocity(new_vel)
        self.assertAlmostEqual(g.getVelocity()[0], new_vel[0])
        self.assertAlmostEqual(g.getVelocity()[1], 5)
        self.assertAlmostEqual(g.getVelocity()[2], new_vel[2])

    def testSetVelocity_y_only_high(self):
        """Tests nominal functioning of setVelocity method with only a y velocity input above the upper bound"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), math.pi/2]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_vel = [0, -10.1, random.uniform(-math.pi/4, math.pi/4)]
        g.setVelocity(new_vel)
        self.assertAlmostEqual(g.getVelocity()[0], new_vel[0])
        self.assertAlmostEqual(g.getVelocity()[1], -10)
        self.assertAlmostEqual(g.getVelocity()[2], new_vel[2])

    def testControlVehicle_Invalid(self):
        """Tests ControlVehicle method functionality with invalid Control parameters"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        c = 'invalid input test'
        with self.assertRaises(TypeError):
            g.controlVehicle(c)

    def testControlVehicle_Valid(self):
        """Tests ControlVehicle method functionality with valid Control parameters"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        new_s = random.uniform(5, 10)
        new_omega = random.uniform(-math.pi/4, -math.pi/4)
        c = Control(new_s, new_omega)
        g.controlVehicle(c)
        self.assertEqual(g.s, new_s)
        self.assertEqual(g.getVelocity()[2], new_omega)

    def testUpdateState_InputSec_Invalid1(self):
        """Tests correct error raised when Update State receives invalid second input type"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        with self.assertRaises(TypeError):
            g.updateState('sec', 50)

    def testUpdateState_InputSec_Invalid2(self):
        """Tests correct error raised when Update State receives negative second input"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        with self.assertRaises(ValueError):
            g.updateState(-10, 50)

    def testUpdateState_InputMSec_Invalid1(self):
        """Tests correct error raised when Update State receives invalid millisecond input type"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        with self.assertRaises(TypeError):
            g.updateState(0, 'msec')

    def testUpdateState_InputMSec_Invalid2(self):
        """Tests correct error raised when Update State receives negative millisecond input"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        with self.assertRaises(ValueError):
            g.updateState(0, -10)

    def testUpdateState_zerotime(self):
        """Tests that no change in vehicle state occurs if vehicle state is updated with no change in time (zero time input)"""
        pose = [random.uniform(0, 100), random.uniform(0, 100), random.uniform(-math.pi, math.pi)]
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        g = GroundVehicle(pose, s, w)
        xdot = g.xdot
        ydot = g.ydot
        g.updateState(0, 0)
        self.assertEqual(g.getVelocity()[0], xdot)
        self.assertEqual(g.getVelocity()[1], ydot)
        self.assertEqual(g.getVelocity()[2], w)
        self.assertEqual(g.getPosition(), pose)

    def testUpdateState_right_movement(self):
        """Tests proper functioning of UpdateState for rightward straight line motion"""
        pose = [10, 20, 0]
        g = GroundVehicle(pose, 8, 0)
        g.updateState(2, 500)
        self.assertEqual(g.getPosition(), [30, 20, 0])

    def testUpdateState_left_movement(self):
        """Tests proper functioning of UpdateState for leftward straight line motion"""
        pose = [100, 20, -math.pi]
        g = GroundVehicle(pose, 10, 0)
        g.updateState(3, 200)
        self.assertAlmostEqual(g.getPosition()[0], 68)
        self.assertAlmostEqual(g.getPosition()[1], 20)
        self.assertAlmostEqual(g.getPosition()[2], -math.pi)

    def testUpdateState_up_movement(self):
        """Tests proper functioning of UpdateState for upward straight line motion"""
        pose = [50, 50, math.pi/2]
        g = GroundVehicle(pose, 5, 0)
        g.updateState(0, 500)
        self.assertEqual(g.getPosition(), [50, 52.5, math.pi/2])

    def testUpdateState_down_movement(self):
        """Tests proper functioning of UpdateState for downward straight line motion"""
        pose = [50, 50, -math.pi/2]
        g = GroundVehicle(pose, 5, 0)
        g.updateState(1, 0)
        self.assertEqual(g.getPosition(), [50, 45, -math.pi/2])

    def testUpdateState_upright_movement(self):
        """Tests proper functioning of UpdateState for straight line motion to upper right"""
        pose = [50, 50, math.pi/4]
        g = GroundVehicle(pose, 10, 0)
        g.updateState(1, 0)
        self.assertEqual(g.getPosition(), [50+g.xdot, 50+g.ydot, math.pi/4])

    def testUpdateState_upleft_movement(self):
        """Tests proper functioning of UpdateState for straight line motion to upper left"""
        pose = [50, 50, 3*math.pi/4]
        g = GroundVehicle(pose, 5, 0)
        g.updateState(2, 0)
        self.assertEqual(g.getPosition(), [50+2*g.xdot, 50+2*g.ydot, 3*math.pi/4])

    def testUpdateState_downright_movement(self):
        """Tests proper functioning of UpdateState for straight line motion to lower right"""
        pose = [50, 50, -math.pi/4]
        g = GroundVehicle(pose, 5, 0)
        g.updateState(2, 300)
        self.assertAlmostEqual(g.getPosition()[0], 50+2.3*g.xdot)
        self.assertAlmostEqual(g.getPosition()[1], 50+2.3*g.ydot)
        self.assertAlmostEqual(g.getPosition()[2], -math.pi/4)

    def testUpdateState_downleft_movement(self):
        """Tests proper functioning of UpdateState for straight line motion to upper left"""
        pose = [50, 50, -3*math.pi/4]
        g = GroundVehicle(pose, 5, 0)
        g.updateState(2, 0)
        self.assertEqual(g.getPosition(), [50+2*g.xdot, 50+2*g.ydot, -3*math.pi/4])


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGroundVehicle)
    unittest.TextTestRunner().run(suite)
