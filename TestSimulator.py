#Matthew Luerman
#PSet 1
#8 February 2018

import unittest
import random
from Simulator import *

random.seed(125)


class TestSimulator(unittest.TestCase):
    """

    """
    def testGetCurrentSec1(self):
        """Test simulator second count is zero prior to running"""
        s = Simulator()
        self.assertEqual(s.getCurrentSec(), 0)

    def testGetCurrentSec2(self):
        pass

    def testGetCurrentMsec1(self):
        """Test simulator millisecond count is zero prior to running"""
        s = Simulator()
        self.assertEqual(s.getCurrentMSec(), 0)

    def testGetCurrentMsec2(self):
        pass

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


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSimulator)
    unittest.TextTestRunner().run(suite)