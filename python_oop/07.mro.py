# Method Resolution Order (DFS)

class A(object):
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num) # 1
print(D.mro()) # [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>]
print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)

class X(object):
  pass

class Y(object): 
  pass

class Z(object):
  pass

class A(X,Y):
  pass

class B(Y,Z):
  pass

class M(B,A,Z):
  pass

print(M.__mro__) # (<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <type 'object'>)