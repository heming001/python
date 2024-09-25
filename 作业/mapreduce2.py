# -*- coding: utf-8 -*-
#def my_abs(x):
#    if not isinstance(x,(int,float)):
#        raise TypeError('bad operand type')
#    if x>0:
#        print(x)
#    else:
#        print(-x)
#
#abs('a')

# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')