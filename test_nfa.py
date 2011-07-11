


import unittest
from nfa import Simulator

class TestNFASimulator(unittest.TestCase):
  def setUp(self):
    self.dg = {
          0: {'': [1, 7],},
          1: {'': [2, 4],},
          2: {'a': [3,]},
          3: {'': [6,], },
          4: {'b': [5,], },
          5: {'': [6,], },
          6: {'': [1, 7,], },
          7: {'a': [8,], },
          8: {'b': [9,], },
          9: {'b': [10,], },
          10: {}
    }
        
    self.sim = Simulator(self.dg, 0, frozenset([10]))

  def test_eclosure_0(self):
    given = frozenset((0,))
    expected = frozenset((0, 1, 2, 4, 7))
    self.assertEqual(self.sim.eclosure(given), expected)

  def test_eclosure_2(self):
    given = frozenset((2,))
    expected = frozenset((2,))
    self.assertEqual(self.sim.eclosure(given), expected)

