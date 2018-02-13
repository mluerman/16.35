#Matthew Luerman
#PSet 1
#8 February 2018

import unittest
import random
import math
from Control import Control

random.seed(125)


class TestControl(unittest.TestCase):
    """
    Tests for the Control class. Checks responses to initialization with valid and invalid parameters, as well as
    nominal functioning of the getSpeed() and getRotVel() methods.
    """
    def testInputs_nominal(self):
        """Tests creation of Control instance with valid inputs"""
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        c = Control(s, w)
        self.assertEqual(c.s, s)
        self.assertEqual(c.omega, w)

    def testInputS_low(self):
        """Tests creation of Control instance with invalid s parameter"""
        s = 4.9
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            c = Control(s, w)

    def testInputS_high(self):
        """Tests creation of Control instance with invalid s parameter"""
        s = 10.1
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(ValueError):
            c = Control(s, w)

    def testInputS_edgelow(self):
        """Tests creation of Control instance with edge case s parameter"""
        s = 5
        w = random.uniform(-math.pi/4, math.pi/4)
        c = Control(s, w)
        self.assertEqual(c.s, s)

    def testInputS_edgehigh(self):
        """Tests creation of Control instance with edge case s parameter"""
        s = 10
        w = random.uniform(-math.pi/4, math.pi/4)
        c = Control(s, w)
        self.assertEqual(c.s, s)

    def testInputS_wrongtype(self):
        """Tests creation of a Control class instance with an invalid speed input"""
        s = 'input test'
        w = random.uniform(-math.pi/4, math.pi/4)
        with self.assertRaises(TypeError):
            c = Control(s, w)

    def testInputOmega_low(self):
        """Tests creation of Control instance with invalid omega parameter"""
        s = random.uniform(5, 10)
        w = -math.pi/4 - .1
        with self.assertRaises(ValueError):
            c = Control(s, w)

    def testInputOmega_high(self):
        """Tests creation of Control instance with invalid omega parameter"""
        s = random.uniform(5, 10)
        w = math.pi/4 + .1
        with self.assertRaises(ValueError):
            c = Control(s, w)

    def testInputOmega_edgelow(self):
        """Tests creation of Control instance with edge case omega parameter"""
        s = random.uniform(5, 10)
        w = -math.pi/4
        c = Control(s, w)
        self.assertEqual(c.s, s)

    def testInputOmega_edgehigh(self):
        """Tests creation of Control instance with edge case omega parameter"""
        s = random.uniform(5, 10)
        w = math.pi/4
        c = Control(s, w)
        self.assertEqual(c.s, s)

    def testInputOmega_wrongtype(self):
        """Tests creation of Control instance with invalid omega parameter"""
        s = random.uniform(5, 10)
        w = 'test input'
        with self.assertRaises(TypeError):
            c = Control(s, w)

    def testGetSpeed(self):
        """Tests nominal functioning of getSpeed() method"""
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        c = Control(s, w)
        self.assertEqual(c.getSpeed(), s)

    def testGetRotVel(self):
        """Tests nominal functioning of getRotVel() method"""
        s = random.uniform(5, 10)
        w = random.uniform(-math.pi/4, math.pi/4)
        c = Control(s, w)
        self.assertEqual(c.getRotVel(), w)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestControl)
    unittest.TextTestRunner().run(suite)
