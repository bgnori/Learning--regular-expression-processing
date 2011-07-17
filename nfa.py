


class NFA:
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
        
    >>> c = Converter(dg, 0, frozenset((10,)))
  '''
  
  def __init__(self, dg, initial, finals):
    self.states = dg
    self.initial = initial
    self.finals = finals
    self.Dstates = {}

  def eclosure(self, T):
    '''
      from p142 fig 3.26
    '''
    stack = list(T)
    result = set(T)
    while stack:
      t = stack.pop()
      try:
        nodes = self.states[t]['']
      except:
        nodes = []

      for u in nodes:
        if u not in result:
          result.add(u)
          stack.append(u)
    return frozenset(result)

  def get_unmarked_T_in_Dstates(self):
    for T in self.Dstates:
      if not self.Dstates[T]:
        return T
    return None

  def move(self, T, a):
    assert a
    result = set()
    for s in self.eclosure(T):
      for e in self.states[s]:
        if a == e:
          result.update(set(self.states[s][a]))
    return frozenset(result)
    
  def makeDFA(self):
    '''
      from p141
      subset construction
    '''
    
    self.Dstates = {self.eclosure((self.initial,)): False} #unmarked eclosure(s0)

    Dtran = {}
    T = self.get_unmarked_T_in_Dstates()
    while T:
      print 'marking', T
      self.Dstates[T] = True
      input = set()
      for s in T:
        for a in self.states[s]:
          input.add(a)
        
      for a in input:
        if not a:
          # skip ''
          continue
        U = self.eclosure(self.move(T, a))
        if U not in self.Dstates:
          self.Dstates.update({U: False})
        t = Dtran.get(T, {})
        t[a] = U
        Dtran[T] = t
      T = self.get_unmarked_T_in_Dstates()
    
    for n in Dtran:
      print n
      print '...', Dtran[n]
    return Dtran 


  def feed(self, s):
    '''
      from page 150
    '''

    S = self.eclosure((self.initial,))
    for a in s:
      S = self.eclosure(self.move(S, a))
    return bool(S & set(self.finals))


  _node = 0
  @classmethod
  def new_node(cls):
    cls._node += 1
    return cls._node


  @classmethod
  def build_empty(cls):
    ini = cls.new_node()
    fin = cls.new_node()
    return NFA({ini: {'': [fin],}, fin:{}}, ini, [fin])
    

  @classmethod
  def build_a(cls, a):
    ini = cls.new_node()
    fin = cls.new_node()
    return NFA({ini: {a: [fin],}, fin:{}}, ini, [fin])


  @classmethod
  def build_or(cls, a, b):
    ini = cls.new_node()
    fin = cls.new_node()
    dg = {}
    assert not ( set(a.states) & set(b.states))
    dg.update(a.states)
    dg.update(b.states)
    dg.update({ini: {"":[a.initial, b.initial]}})
    for s in a.finals:
      assert dg[s] == {}
      # because Thompson alogorith does not produce NFAs have fins with outgoing edges

      dg[s] = {'': [fin]}

    for s in b.finals:
      assert dg[s] == {}
      # because Thompson alogorith does not produce NFAs have fins with outgoing edges

      dg[s] = {'': [fin]}

    dg[fin] = {}
    return NFA(dg, ini, [fin])


  @classmethod
  def build_cat(cls, a, b):
    dg = {}
    assert not ( set(a.states) & set(b.states))

    ini = a.initial 
    fin = b.finals
    dg.update(a.states)
    dg.update(b.states)

    del dg[b.initial]
    for j in a.finals:
      e = dict()
      e.update(b.states[b.initial])
      dg[j] = e

    return NFA(dg, ini, fin)


  @classmethod
  def build_zom(cls, a):
    dg = {}
    ini = cls.new_node()
    fin = cls.new_node()
    dg.update(a.states)


    dg[ini] = {'':[a.initial, fin]}
    print dg
    for f in a.finals:
      assert dg[f] == {}
      dg[f] = {'': [a.initial, fin]}
    
    dg[fin] = {}
    return NFA(dg, ini, [fin])



