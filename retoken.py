import StringIO


class Token(object):
  def __init__(self, raw):
    self.raw = raw

  def __str__(self):
    return self.raw
    
  def __nonzero__(self):
    return bool(self.raw)


class Escapsed(Token):
  def __init__(self, value):
    super(Escapsed, self.__class__).__init__(self, '\\'+value)
    self.value = value


class SingletonToken(Token): #Ugh!
  pool = {}
  def __init__(self, name, raw):
    super(SingletonToken, self.__class__).__init__(self, raw)
    self.name = name

  @classmethod
  def make(cls, name, raw):
    cls.pool[name] = SingletonToken(name, raw)

    def builder(raw):
      tk = cls.pool[name]
      assert tk.raw == raw
      return tk
    return builder


# short cuts
# may be better to use singlton with meta class.
Or = SingletonToken.make(name='or', raw='|')
LP = SingletonToken.make(name='LP', raw='(')
RP = SingletonToken.make(name='RP', raw=')')
Mul = SingletonToken.make(name='Mul', raw='*')
EOF = SingletonToken.make(name='EOF', raw='')



'''
#parse
|
() 
'\\' escape
*

''
'a'
'b'
'a*'
'ab'
'a|b'
'(a)'
'aa|b'
'(aa)|b'
'a*|b'
'\|a'
'''

class Tokenizer:
  def __init__(self):
    self.buf = None
    self.readahead = ''

  def feed(self, x):
    self.buf = StringIO.StringIO(x)
    self.read_char()

  def get_token(self):
    c = self.readahead
    if c == '':
      return self.handle_eof(c)
    elif c == '\\':
      return self.handle_escape(c)
    elif c == '|':
      return self.handle_or(c)
    elif c == '*':
      return self.handle_mul(c)
    elif c == '(':
      return self.handle_LP(c)
    elif c == ')':
      return self.handle_RP(c)
    else: 
      '''any thing else'''
      return self.handle_default(c)
    assert False

    
  def handle_eof(self, a):
    self.match_char('')
    return EOF(a)
    
  def handle_default(self, a):
    self.match_char(a)
    return Token(a)

  def handle_RP(self, a):
    self.match_char(a)
    return RP(a)
    
  def handle_LP(self, a):
    self.match_char(a)
    return LP(a)

  def handle_or(self, a):
    self.match_char(a)
    return Or(a)

  def handle_mul(self, a):
    self.match_char(a)
    return Mul(a)

  def handle_escape(self, a):
    b = self.peek_char()
    self.match_char(a)
    self.match_char(b)
    return Escapsed(b)

  def matchToken(self, token):
    pass

  def read_char(self):
    c = self.buf.read(1)
    self.readahead = c
    return c
  
  def peek_char(self):
    c = self.buf.read(1)
    if c != '': #eof.
     self.buf.seek(-1, 1)
    return c

  def match_char(self, m):
    assert self.readahead == m
    self.read_char()



