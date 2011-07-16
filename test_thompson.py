


import unittest
from reparser import REParser
from thompson import Thompson


class TestThompson(unittest.TestCase):
  def setUp(self):
    self.parser = REParser(Thompson())

  def test_Empty(self):
    nfa = self.parser.parse('')
    self.assert_(set(nfa.states[nfa.initial]['']) &set(self.finals))

  def test_a(self):
    nfa = self.parser.parse('')
    self.assert_(set(nfa.states[nfa.initial]['a']) & set(self.finals))
    
  
