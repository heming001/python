# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [L.lower() for L in L1 if isinstance(L,str)]

print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')