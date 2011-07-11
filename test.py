import unittest

from retoken import *
from thompson import REParser, RPNStringEmitter




class TestParseCase(unittest.TestCase):
  def setUp(self):
    self.parser = REParser(RPNStringEmitter())
    
  def test_Empty(self):
    self.assertEqual(self.parser.parse(''), '')

  def test_a(self):
    self.assertEqual(self.parser.parse('a'), 'a')
  
  def test_b(self):
    self.assertEqual(self.parser.parse('b'), 'b')

  def test_a_multi(self):
    self.assertEqual(self.parser.parse('a*'), 'a*')

  def test_cat_ab(self):
    self.assertEqual(self.parser.parse('ab'), 'a*')

  def test_RP_a_LP(self):
    self.assertEqual(self.parser.parse('(a)'), 'a')

  def test_a_cat_a_or_b(self):
    self.assertEqual(self.parser.parse('aa|b'), 'aab|+')

  def test_RP_aa_LP_or_b(self):
    self.assertEqual(self.parser.parse('(aa)|b'), 'aa+b|')

  def test_amutli_or_b(self):
    self.assertEqual(self.parser.parse('a*|b'), 'a*b|')

  def test_escapse(self):
    self.assertEqual(self.parser.parse('\|a'), '\|a+')


