#! -*- coding: utf-8 -*- 
#L=list(filter(lambda x : x % 2 ==1,list(range(1,20)))) 
#print(L)

#f = filter(lambda x : x % 2 ==1,list(range(1,20)))
#print(f)



#def is_odd(n):
#    return n % 2 == 1

#L = list(filter(is_odd, range(1, 20)))

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0
it = _odd_iter
n = 3
L = filter(_not_divisible(n),it)
list(L)

