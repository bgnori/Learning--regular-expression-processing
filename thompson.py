

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


class REParser:
  '''
    R -> exp
    exp -> term | term Or term | term Cat term | term Mul
    term -> ( exp ) | letter
    letter -> alpha | escaped

  '''
  def __init__(self, emitter):
    self.tk = Tokenizer()
    self.emitter = emitter

  def reset(self):
    self.emitter.reset()
    self.buf = None
    
    pass

  def feed(self, s):
    self.tk.feed(s)

  def expr(self):
    pass

  def term(self):
    pass

  def match(self):
    pass

  def next_token(self):
    self.lookahead = self.tk.get_token()
    return self.lookahead
  
  def parse(self, s):
    self.feed(s)
    while self.nextToken():
      break

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

  def Alpha(self, a):
    ''' rule 2:
      ->[i] -(a)-> [[f]]
      a: str
      result: NFA
    '''
      
  
  def op_or(self, Ns, Nt):
    '''
      s|t -> N(s|t)
      Ns, Nt : NFA
      result : NFA
  
    '''
    pass   

  def op_cat(self, Ns, Nt):
    '''
      st -> N(st)
      Ns, Nt : NFA
      result : NFA
    '''
    pass   
  
  def op_repeat(self, Ns):
    '''
      s* -> N(s*)
      Ns : NFA
      result : NFA, N(s*)
    '''
    pass   
  
  def string(self, s):
    '''
      s -> N(s)
      s : str
      result : NFA
    '''
    pass   


class RPNStringEmitter(Emitter):
  def __init__(self):
    self._result = ''

  def empty(self):
    return ''

  def alpha(self, a):
    return a

  def op_or(self, Ns, Nt):
    return ''.join((Ns, Nt, '|'))

  def op_cat(self, Ns, Nt):
    return ''.join((Ns, Nt, '+'))

  def op_repeat(self, Ns):
    return ''.join((Ns, '*'))

  def string(self, s):
    return s


