#！-*- coding: utf-8 -*-
def YangHui():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L,L+[0])]


o = YangHui()
n = 8
for i in o:
    print(i)
    n = n-1
    if n == 0:
        break



