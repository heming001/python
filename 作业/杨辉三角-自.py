# -*- conding:utf-8 -*-

def triangles():
    L = [1]
    while True:
        yield L
        print(range(len(L)+ 1))
        L = [ L[i] + L[i-1] if i > 0 and i < len(L) else 1 for i in range( len(L) + 1 )]
    
a = triangles()

print(next(a))
print(next(a))
print(next(a))
print(next(a))
