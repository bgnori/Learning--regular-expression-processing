


class Simulator:
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
        
    >>> s = Simulator(dg, 0, {10,})
    >>> s.reset()
    >>> s.feed('abb')
    True

    >>> s.reset()
    >>> s.feed('aabb')
    True

    >>> s.reset()
    >>> s.feed('babb')
    True

    >>> s.reset()
    >>> s.feed('aaabb')
    True
  '''
  
  def __init__(self, dg, initial, accepts):
    self.states = dg
    self.initial = initial

  def reset(self):
    self.current = self.initial

  def handle(self, c):
    state = self.states[self.current]
    self.current = state[c]

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
    return result
    


  def feed(self, s):

    return True


if __name__ == '__main__':
  import doctest
  doctest.testmod()
