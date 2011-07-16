


import unittest
from nfa import NFA 


class TestNFA(unittest.TestCase):
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
        
    self.nfa = NFA(self.dg, 0, frozenset([10]))

  def test_eclosure_0(self):
    given = frozenset((0,))
    expected = frozenset((0, 1, 2, 4, 7))
    self.assertEqual(self.nfa.eclosure(given), expected)

  def test_eclosure_2(self):
    given = frozenset((2,))
    expected = frozenset((2,))
    self.assertEqual(self.nfa.eclosure(given), expected)

  def test_move_2_3(self):
    given = frozenset((2,))
    expected = frozenset((3,))
    self.assertEqual(self.nfa.move(given, 'a'), expected)

  def test_move_6_8(self):
    given = frozenset((6,))
    expected = frozenset((3, 8,))
    self.assertEqual(self.nfa.move(given, 'a'), expected)
    
  def test_makeDFA(self):
    '''
      from p143
    '''
    A = frozenset([0, 1, 2, 4, 7])
    B = frozenset([1, 2, 3, 4, 6, 7, 8])
    C = frozenset([1, 2, 4, 5, 6, 7])
    D = frozenset([1, 2, 4, 5, 6, 7, 9])
    E = frozenset([1, 2, 4, 5, 6, 7, 10])

    expected = {
      A: {'a': B, 'b': C},
      B: {'a': B, 'b': D},
      C: {'a': B, 'b': C},
      D: {'a': B, 'b': E},
      E: {'a': B, 'b': C},
    }
    self.assertEqual(self.nfa.makeDFA(), expected)
    


class TestNFAComposition(unittest.TestCase):
  def test_Empty(self):
    emp = NFA.build_empty()
    self.assert_(emp.initial)
    self.assert_(emp.finals)
    self.assertEqual(len(emp.states) , 2)
    self.assertEqual(
      emp.states[emp.initial],
      dict({'': emp.finals})
    )

  def test_a(self):
    a = NFA.build_a('a')
    self.assert_(a.initial)
    self.assert_(a.finals)
    self.assertEqual(len(a.states) , 2)
    self.assertEqual(
      a.states[a.initial],
      dict({'a': a.finals})
    )

  def test_or(self):
    a = NFA.build_a('a')
    b = NFA.build_a('b')
    ab = NFA.build_or(a, b)

    self.assert_(ab.initial)
    self.assert_(ab.finals)


  def test_cat(self):
    a = NFA.build_a('a')
    b = NFA.build_a('b')
    ab = NFA.build_cat(a, b)

    self.assert_(ab.initial)
    self.assert_(ab.finals)


  def test_zom(self):
    a = NFA.build_a('a')
    azom = NFA.build_zom(a)
  
    self.assert_(azom.initial)
    self.assert_(azom.finals)

