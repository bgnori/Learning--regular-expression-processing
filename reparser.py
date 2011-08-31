
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
    print '  trying expr', self.lookahead
    self.choice()
    self.morechoice()

  def morechoice(self):
    print '  trying morechoice', self.lookahead
    if self.lookahead.name == 'or':
      self.match_token(self.lookahead)
      self.choice()
      self.emitter.Or(self.lookahead)
      self.morechoice() #ugh! risk of stack over flow

  def choice(self):
    '''
      choice -> seq | morese
      moreseq -> seq moreseq | Empty
    '''
    print '  trying choice', self.lookahead
    self.seq()
    self.moreseq()

  def moreseq(self):
    print '  trying moreseq', self.lookahead
    if self.lookahead:
      #if not isinstance(self.lookahead, SingletonToken):
      if self.lookahead.name not in ('or', 'ZeroOrMore', 'RP'):
        # == term
        self.seq()
        print 'moreseq:cat', self.emitter._result
        self.emitter.Cat(self.lookahead)
        #self.match_token(self.lookahead)
      else:
        print '    moreseq:SingletonToken', self.lookahead
    else:
      pass

  def seq(self):
    ''' seq -> term ZeroOrMore | term '''
    print '  trying seq', self.lookahead
    self.term()
    t = self.lookahead
    if t.name == 'ZeroOrMore':
      self.match_token(t)
      self.emitter.ZOM(t)

  def term(self):
    ''' term -> ( expr ) | letter '''
    print '  trying term', self.lookahead
    t = self.lookahead
    if t.name == 'LP':
      self.LP()
      self.expr()
      self.RP()
    elif t.name == 'Token' or t.name == 'Escaped':
      self.letter()
    else:
      self.error('bad term around %s, name = %s'%(repr(t), t.name))

  def letter(self):
    print '  trying letter', self.lookahead
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
    print '  trying LP'
    t = self.lookahead
    self.match_token(t)
    self.emitter.LP(t)

  def RP(self):
    print '  trying RP'
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
    
    

