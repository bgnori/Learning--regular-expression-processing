
from retoken import *

from emit import Emitter

class Thompson(Emitter):
  def __init__(self):
    self._result = []

  def result(self):
    return ''.join(self._result)

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


