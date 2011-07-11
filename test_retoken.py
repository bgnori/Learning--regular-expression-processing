import unittest

from retoken import *

class TestTokenCase(unittest.TestCase):
  def test_Token(self):
    t = Token('a')

class TestSpecialTokenCase(unittest.TestCase):

  def test_Singular(self):
    s1 = Or('|')
    s2 = Or('|')
    self.assertEqual(id(s1), id(s2))

  def test_name1(self):
    o = Or('|')
    self.assertEqual(o.name, 'or')

  def test_name2(self):
    m = ZOM('*')
    self.assertEqual(m.name, 'ZeroOrMore')

  def test_raw(self):
    o = Or('|')
    self.assertEqual(o.raw, '|')
    
    m = ZOM('*')
    self.assertEqual(m.raw, '*')

    L = LP('(')
    self.assertEqual(L.raw, '(')

    R = RP(')')
    self.assertEqual(R.raw, ')')


  def test_escape(self):
    e = Escapsed('a')
    self.assertEqual(e.raw, '\\a')
    self.assertEqual(e.value, 'a')

  def test_EOF(self):
    e = EOF('')
    self.assertEqual(e.raw, '')
    

class TestTokenizerCase(unittest.TestCase):
  def setUp(self):
    self.tokenizer = Tokenizer()
  
  def test_feed(self):
    self.tokenizer.feed('aaa')
    self.assertEqual(self.tokenizer.buf.getvalue(), 'aaa')

  def test_feed_null(self):
    tk = self.tokenizer
    tk.feed('')
    t = tk.get_token()
    t = tk.get_token()
    self.assertEqual(t.raw, '')
    self.assertEqual(t.name, 'EOF')


  def test_get_token_a(self):
    tk = self.tokenizer
    tk.feed('a')
    t = tk.get_token()
    self.assertEqual(t.raw, 'a')
    t = tk.get_token()
    self.assertEqual(t.raw, '')
    self.assertEqual(t.name, 'EOF')

  def test_get_token_ab(self):
    tk = self.tokenizer
    tk.feed('ab')
    t = tk.get_token()
    self.assertEqual(t.raw, 'a')
    t = tk.get_token()
    self.assertEqual(t.raw, 'b')
    t = tk.get_token()
    self.assertEqual(t.raw, '')
    self.assertEqual(t.name, 'EOF')

  def test_get_token_all(self):
    tk = self.tokenizer
    tk.feed(r'(\()\)*\*|\|\a')

    r = []
    t = tk.get_token()
    while t:
      r.append(str(t))
      t = tk.get_token()
    self.assertEqual(r, ['(', r'\(', ')', r'\)', '*', r'\*', r'|', r'\|', r'\a'])


