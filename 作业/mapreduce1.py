#！ -*- coding: utf-8 -*-
def normalize(name):
    n = 0
    b=None
    a = len(name)
    for i in range(a):
        if i == 0:
            b =name[i].upper()
        else:
            b = b+name[i].lower()
        n = n+1
    return b

print(normalize('admin'))
        
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
        
