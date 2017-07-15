#!/usr/bin/env python3
class A: pass
class B: pass
class C(A, B): pass
class D(B): pass
class E(D, C): pass
print(E.mro())
# [<class '__main__.E'>, <class '__main__.D'>, <class '__main__.C'>,
#  <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
