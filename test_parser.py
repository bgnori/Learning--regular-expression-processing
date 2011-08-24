import unittest

from retoken import *
from reparser import REParser
from emit import RPNStringEmitter




class TestParseCase(unittest.TestCase):
  '''testing with RPNEmitter'''

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
    self.assertEqual(self.parser.parse('ab'), 'ab+')

  def test_cat_abc(self):
    self.assertEqual(self.parser.parse('abc'), 'ab+c+')

  def test_LP_a_RP(self):
    self.assertEqual(self.parser.parse('(a)'), 'a')

  def test_LPLP_a_RPRP(self):
    self.assertEqual(self.parser.parse('((a))'), 'a')

  def test_a_cat_a_or_b(self):
    self.assertEqual(self.parser.parse('aa|b'), 'aa+b|')

  def test_LP_aa_RP_or_b(self):
    self.assertEqual(self.parser.parse('(aa)|b'), 'aa+b|')

  def test_a_LP_a_or_b_RP(self):
    self.assertEqual(self.parser.parse('a(a|b)'), 'aab|+')

  def test_amutli_or_b(self):
    self.assertEqual(self.parser.parse('a*|b'), 'a*b|')

  def test_escapse(self):
    self.assertEqual(self.parser.parse('\|'), '\|')

  def test_escapse2(self):
    self.assertEqual(self.parser.parse('\|a'), '\|a+')

  def test_a_or_bmutli(self):
    self.assertEqual(self.parser.parse('a|b*'), 'ab*|')

  def test_LP_a_or_b_RP_mutli(self):
    self.assertEqual(self.parser.parse('(a|b)*'), 'ab|*')


  def test_a_or_b_or_c(self):
    self.assertEqual(self.parser.parse('a|b|c'), 'ab|c|')

  def test_LP_a_m_RP_m(self):
    self.assertEqual(self.parser.parse('(a*)*'), 'a**')

  def test_a_mm(self):
    self.assertEqual(self.parser.parse('a**'), 'a**')

  def test_LP_a_RP_b(self):
    self.assertEqual(self.parser.parse('(a)b'), 'ab+')

  def test_LP_a_m_RP_b(self):
    self.assertEqual(self.parser.parse('(a)*b'), 'a*b+')

  def test_LP_a_m_RP_b_b(self):
    self.assertEqual(self.parser.parse('(a)*bb'), 'a*b+b+')

