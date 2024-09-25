# -*- conding: utf-8 -*-

from collections.abc import Iterable
def findMinAndMax(L):
    if len(L) == 0:
        return (None,None)
    elif isinstance(L,Iterable):
        min = max = L[0]
        for i in L:
            if i < min:
                min = i
            if i > max:
                max = i
        return (min,max)
    else:
        return (None,None)
    
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

print(findMinAndMax([7, 1, 3, 9, 5]))