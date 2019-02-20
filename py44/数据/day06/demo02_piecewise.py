# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
piecewise.py  测试数组处理函数
'''
import numpy as np

a = np.array([11, 23, 94, 65, 23, 60, 84, 56, 23])
d = np.piecewise(
    a,
    [(20 < a) & (a < 60), a == 60, a > 60],
    [-1, 0, 1])
print(d)
