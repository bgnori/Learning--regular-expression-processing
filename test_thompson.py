


import unittest
from reparser import REParser
from thompson import Thompson


class TestThompson(unittest.TestCase):
  def setUp(self):
    self.parser = REParser(Thompson())

  def test_Empty(self):
    nfa = self.parser.parse('')
    self.assert_(set(nfa.states[nfa.initial]['']) &set(nfa.finals))

  def test_a(self):
    nfa = self.parser.parse('a')
    self.assert_(set(nfa.states[nfa.initial]['a']) & set(nfa.finals))
    
  def test_a_cat_b(self):
    nfa = self.parser.parse('ab')
    before_b = nfa.states[nfa.initial]['a']
    self.assert_(before_b)
    self.assertEqual(len(before_b), 1)
    b = before_b[0]
    print nfa.finals
    self.assert_(set(nfa.states[b]['b']) & set(nfa.finals))
  
  def test_a_or_b(self):
    nfa = self.parser.parse('a|b')
    for s in  nfa.states[nfa.initial]['']:
      if 'a' in nfa.states[s]:
        an = nfa.states[s]['a']

      if 'b' in nfa.states[s]:
        bn = nfa.states[s]['b']

    ax = set()
    print nfa.states
    for x in an:
      print nfa.states[x]
      ax |= set(nfa.states[x][''])

    bx = set()
    for x in bn:
      bx |= set(nfa.states[x][''])

    self.assert_(set(ax) & set(nfa.finals))
    self.assert_(set(bx) & set(nfa.finals))

  def test_a_zom(self):
    nfa = self.parser.parse('a*')

    self.assert_(set(nfa.states[nfa.initial]['']) & set(nfa.finals))

    for s in nfa.states[nfa.initial]['']:
      if s not in nfa.finals:
        break
    Nsi = s

    xs = nfa.states[Nsi]['a']
    self.assertEqual(len(xs), 1)
    Nsf = xs[0]
      
    for s in nfa.states[Nsf]['']:
      self.assert_(s in nfa.finals or Nsi == s)
    
      
  def test_LP_a_or_b_RP_c(self):
    nfa = self.parser.parse('(a|b)c')
    print 'b -> '
    self.assertFalse(nfa.feed('b'))
    print 'bc -> '
    self.assert_(nfa.feed('bc'))

  def test_LP_a_or_b_RP_c_2(self):
    nfa = self.parser.parse('(a|b)c')
    print 'a -> '
    self.assertFalse(nfa.feed('a'))
    print 'ac -> '
    self.assert_(nfa.feed('ac'))





