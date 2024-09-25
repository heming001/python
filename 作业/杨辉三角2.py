#! -* - coding: utf-8 -*-
def YangHui():
    L = [1]
    while True:
        yield L
        for i in range(1,len(L)):
            L[i]=pre[i]+pre[i-1]
        L.append(1)
        pre = L[:]
        



o = YangHui()
n = 8
for i in o:
    print(i)
    n = n-1
    if n == 0:
        break
   