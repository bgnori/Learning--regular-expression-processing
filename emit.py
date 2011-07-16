

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
    print 'Cat'
    self._result.append('+')

  def ZOM(self, Ns):
    self._result.append('*')


  def LP(self, t):
    pass

  def RP(self, t):
    pass


