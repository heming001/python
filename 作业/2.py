# -*- coding: utf-8 -*-

import math

def quadratic(a,b,c):
    if not isinstance (a,(int,float)):
        raise TypeError('bad operand type')
    middle = b**2 - 4 * a * c
    if middle < 0 :
        return None
    elif middle  == 0 :
        return -b/2/a
    else :
        print(-b + math.sqrt(middle))
        return (-b + math.sqrt(middle))/2/a , (-b - math.sqrt(middle))/2/a
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')