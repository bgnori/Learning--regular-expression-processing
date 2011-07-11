

from retoken import *

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
from exceptions import Exception

class ParserError(Exception):
  pass

class REParser:
  '''
    R -> expr eof | Empty
    expr -> choice morechoice  
    morechoice -> Or choice morechoice | Empty
    choice -> seq | moreseq
    moreseq -> seq moreseq | Empty
    seq -> term ZeroOrMore | term
    term -> ( expr ) | letter
    letter -> alpha | escaped

  '''
  def __init__(self, emitter):
    self.tokenizer = Tokenizer()
    self.emitter = emitter

  def reset(self):
    self.emitter.reset()
    self.buf = None

  def error(self, msg):
    print self.emitter.result()
    raise ParserError(msg)


  def feed(self, s):
    self.tokenizer.feed(s)


  def expr(self):
    ''' 
      expr -> choice morechoice
      morechoice -> Or choice morechoice | Empty
    '''
    print 'expr', self.lookahead
    self.choice()
    while self.lookahead.name == 'or':
      self.match_token(self.lookahead)
      self.choice()
      self.emitter.Or(self.lookahead)

  def choice(self):
    '''
      choice -> seq | morese
      moreseq -> seq moreseq | Empty
    '''
    print 'choice', self.lookahead
    self.seq()
    t = self.lookahead
    while self.lookahead:
      self.seq()
      self.emitter.Cat(self.lookahead)

  def seq(self):
    ''' seq -> term ZeroOrMore | term '''
    print 'seq', self.lookahead
    self.term()
    t = self.lookahead
    if t.name == 'ZeroOrMore':
      self.match_token(t)
      self.emitter.ZOM(t)

  def term(self):
    ''' term -> ( expr ) | letter '''
    print 'term', self.lookahead
    t = self.lookahead
    if t.name == 'LP':
      self.LP()
      self.expr()
      # self.RP()
    elif t.name == 'RP':
      self.RP() # ???
    elif t.name == 'Token' or t.name == 'Escaped':
      self.letter()
    else:
      self.error('bad term around %s, name = %s'%(repr(t), t.name))

  def letter(self):
    print 'letter', self.lookahead
    t = self.lookahead
    if t.name == 'Token':
      self.alpha()
    elif t.name == 'Escaped':
      self.escaped()
    else:
      self.error('bad token %s, name=%s'%(t, t.name))

  def alpha(self):
    t = self.lookahead
    self.emitter.alpha(t)
    self.match_token(t)

  def escaped(self):
    t = self.lookahead
    self.emitter.alpha(t)
    self.match_token(t)

  def LP(self):
    print 'LP'
    t = self.lookahead
    self.match_token(t)
    self.emitter.LP(t)

  def RP(self):
    print 'RP'
    t = self.lookahead
    self.match_token(t)
    self.emitter.RP(t)


  def match_token(self, t):
    assert self.lookahead == t
    print 'consumed', t.raw
    self.next_token()

  def next_token(self):
    self.lookahead = self.tokenizer.get_token()
    return self.lookahead

  def parse(self, s):
    self.feed(s)
    self.next_token()
    t = self.lookahead
    if t:
      self.expr()
    return self.emitter.result()
    


class Emitter:
  def reset(self):
    pass

  def result(self):
    pass

  def empty(self):
    ''' rule 1:
      ->[i] -(e)-> [[f]]
      i: initial state
      f: finish state
      input: None
      result: NFA
    '''
    pass

  def alpha(self, a):
    ''' rule 2:
      ->[i] -(a)-> [[f]]
      a: str
      result: NFA
    '''
      
  
  def Or(self, a):

    '''
      s|t -> N(s|t)
      Ns, Nt : NFA
      result : NFA
  
    '''
    pass   

  def Cat(self, a):
    '''
      st -> N(st)
      Ns, Nt : NFA
      result : NFA
    '''
    pass   
  
  def ZOM(self, s):
    '''
      s* -> N(s*)
      Ns : NFA
      result : NFA, N(s*)
    '''
    pass   
  


class RPNStringEmitter(Emitter):
  def __init__(self):
    self._result = []

  def result(self):
    return ''.join(self._result)

  def empty(self, t):
    self._result.append('')

  def alpha(self, t):
    self._result.append(t.raw)

  def Or(self, t):
    self._result.append('|')
    

  def Cat(self, t):
    self._result.append('+')

  def ZOM(self, Ns):
    self._result.append('*')


  def LP(self, t):
    pass

  def RP(self, t):
    pass


