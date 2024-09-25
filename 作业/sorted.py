# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L)
print(L2)

def by_score(t):
  #  print(t[1])
    return t[1]

L2 = sorted(L, key=by_score)
print(L2)