


import unittest
from nfa import Converter

class TestNFAConverter(unittest.TestCase):
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
        
    self.sim = Converter(self.dg, 0, frozenset([10]))

  def test_eclosure_0(self):
    given = frozenset((0,))
    expected = frozenset((0, 1, 2, 4, 7))
    self.assertEqual(self.sim.eclosure(given), expected)

  def test_eclosure_2(self):
    given = frozenset((2,))
    expected = frozenset((2,))
    self.assertEqual(self.sim.eclosure(given), expected)

  def test_move(self):
    given = frozenset((2,))
    expected = frozenset((3,))
    self.assertEqual(self.sim.move(given, 'a'), expected)
    
  def test_build(self):
    '''
      from p143
    '''
    A = frozenset([0, 1, 2, 4, 7])
    B = frozenset([1, 2, 3, 4, 6, 7, 8])
    C = frozenset([1, 2, 3, 4, 6, 7])
    D = frozenset([1, 2, 4, 5, 6, 7, 9])
    E = frozenset([1, 2, 4, 5, 6, 7, 10])

    expected = {
      A: {'a': B, 'b': C},
      B: {'a': B, 'b': D},
      C: {'a': B, 'b': C},
      D: {'a': B, 'b': E},
      E: {'a': B, 'b': C},
    }
    self.assertEqual(self.sim.build(), expected)
    

