# -*- coding: utf-8 -*-
import time,functools
def metric(text):
    def decorator(func):
        @functools.wraps(func)
        def wrappers(*args,**kw):
            print(text)
            print('begin call')
            r = func(*args,**kw)
            print('end call')
            return r
        return wrappers
    return decorator
# 测试
@metric('梦')
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric('园')
def slow(x, y, z):
    time.sleep(0.1234)
    print('succ')
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')