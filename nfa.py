


class Converter:
  '''
    sample from p142 fig 3.27
    it should accept (a|b)*abb
    >>> dg = {0: {'': [1, 7],},\
              1: {'': [2, 4],},\
              2: {'a': [3,]},\
              3: {'': [6,], },\
              4: {'b': [5,], },\
              5: {'': [6,], },\
              6: {'': [1, 7,], },\
              7: {'a': [8,], },\
              8: {'b': [9,], },\
              9: {'b': [10,], },\
              10: {}\
             }
        
    >>> c = Converter(dg, 0, {10,})
  '''
  
  def __init__(self, dg, initial, accepts):
    self.states = dg
    self.initial = initial
    self.Dstates = {}

  def eclosure(self, T):
    '''
      from p142 fig 3.26
    '''
    stack = list(T)
    result = set(T)
    while stack:
      print 'stack', stack
      t = stack.pop()
      print 'node', t
      try:
        nodes = self.states[t]['']
      except:
        nodes = []

      for u in nodes:
        if u not in result:
          print '...', u
          result.add(u)
          stack.append(u)
    return frozenset(result)

  def get_unmarked_T_in_Dstates(self):
    for T in self.Dstates:
      if not self.Dstates[T]:
        return T
    return None

  def move(self, T, a):
    result = set()
    for s in T:
      for v in self.states[s].values():
        result.update(set(v))
    return frozenset(result)
    
  def build(self):
    '''
      from p141
    '''
    
    self.Dstates = {self.eclosure((self.initial,)): False} #unmarked eclosure(s0)

    Dtran = {}
    T = self.get_unmarked_T_in_Dstates()
    while T:
      print 'marking', T
      self.Dstates[T] = True
      input = {}
      for s in T:
        for a in self.states[s]:
          input.update({a:None})
        
      for a in input:
        U = self.eclosure(self.move(T, a))
        if U not in self.Dstates:
          self.Dstates.update({U: False})
        t = Dtran.get(T, {})
        t[a] = U
      T = self.get_unmarked_T_in_Dstates()
    return Dtran 
    



if __name__ == '__main__':
  import doctest
  doctest.testmod()
