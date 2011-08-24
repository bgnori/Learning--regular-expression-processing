
from retoken import *

from nfa import NFA
from emit import Emitter

class Thompson(Emitter):
  def __init__(self):
    self._result = []

  def reset(self):
    self._result = []

  def result(self):
    if len(self._result) == 1:
      return self._result[0]
    elif len(self._result) == 0:
      return NFA.build_empty()
    else:
      print 'got multiple nfas?!'
      for n in self._result:
        print n, n.states
      assert False

  def push(self, x):
    self._result.append(x)

  def pop(self):
    return self._result.pop()


  def alpha(self, t):
    nfa = NFA.build_a(t.raw) #ugh! t.value?
    self.push(nfa)

  def Or(self, t):
    b = self.pop()
    a = self.pop()
    ab = NFA.build_or(a, b)
    self.push(ab)

  def Cat(self, t):
    b = self.pop()
    a = self.pop()
    ab = NFA.build_cat(a, b)
    self.push(ab)

  def ZOM(self, Ns):
    a = self.pop()
    azom = NFA.build_zom(a)
    self.push(azom)


  def LP(self, t):
    pass

  def RP(self, t):
    pass



if __name__ == "__main__":
  from reparser import REParser
  parser = REParser(Thompson())
  nfa = parser.parse('(a|b)*abb')
  print nfa.states
  print 'abb ==>', nfa.feed('abb')
  print '--'
  print 'babb ==>', nfa.feed('babb')
  print '--'
  print 'bbabb ==>', nfa.feed('bbabb')
  
