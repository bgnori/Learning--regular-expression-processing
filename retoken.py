import StringIO


class Token(object):
  pass


class Alpha(Token):
  pass

class Escapsed(Token):
  pass

class SingletonToken(Token):
  _instance = None
  name = 'SingletonToken'
  raw = 'void'
  def __new__(cls, *c, **d):
    if cls._instance:
      return cls._instance

    cls._instance = super(SingletonToken, cls).__new__(cls)
    return cls._instance

class Or(SingletonToken):
  name = 'or'
  raw = '|'

class RP(SingletonToken):
  pass

class LP(SingletonToken):
  pass

class Mul(SingletonToken):
  pass

class EOF(SingletonToken):
  pass



class Tokenizer:
  def __init__(self):
    self.buf = None

  def feed(self, x):
    self.buf = StringIO.StringIO(x)

  def getToken(self):
    pass
    
  def handle_alf(self, a):
    pass
  def handle_RP(self, ):
    pass
  def handle_LP(self, ):
    pass
  def handle_or(self):
    pass
  def handle_cat(self):
    pass
  def handle_escape(self):
    pass
  def match(self, x):
    pass
  def peek(self):
    pass


