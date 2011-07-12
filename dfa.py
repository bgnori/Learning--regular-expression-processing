

  
class DFA:
  '''
    sample from p139
    it should accept (a|b)*abb

    >>> dg = {0: {'a': 1, 'b':0},\
              1: {'a': 1, 'b': 2},\
              2: {'a': 1, 'b': 3},\
              3: {'a': 1, 'b': 0}\
             }
        
    >>> s = DFA(dg, 0, {3})
    >>> s.reset()
    >>> s.feed('a')
    False
    
    >>> s.reset()
    >>> s.feed('b')
    False

    >>> s.reset()
    >>> s.feed('ab')
    False

    >>> s.reset()
    >>> s.feed('aba')
    False

    >>> s.reset()
    >>> s.feed('bbabb')
    True

  '''

  def __init__(self, dg, initial, accepts):
    self.states = dg
    self.initial = initial
    self.current = initial
    self.accepts = accepts

  def reset(self):
    self.current = self.initial

  def handle(self, c):
    state = self.states[self.current]
    self.current = state[c]

  def feed(self, s):
    for c in s:
      self.handle(c)
    return self.current in self.accepts
  

  
if __name__ == '__main__':
  import doctest
  doctest.testmod()

