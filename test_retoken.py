import unittest

from retoken import *

class TestTokenCase(unittest.TestCase):
  def test_Token(self):
    t = Token()

class TestSingletonTokenCase(unittest.TestCase):
  def test_Token(self):
    t = Token()
  def test_SingletonToken(self):
    s1 = SingletonToken()
    s2 = SingletonToken()
    self.assertEqual(id(s1), id(s2))

  def test_name(self):
    o = Or()
    self.assertEqual(o.name, 'Or')
  def test_raw(self):
    o = Or()
    self.assertEqual(o.raw, '|')
    
