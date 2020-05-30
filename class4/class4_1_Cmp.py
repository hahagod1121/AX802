# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:14:10 2020

@author: Jason
"""

import random
from functools import cmp_to_key

data1 = [random.randrange(10) for _ in range(10)]

def myCmp(data1:int,data2:int):
    cmp1 = data1 + data1 * 2
    cmp2 = data2 + data2 * 2
     
    if cmp1 > cmp2:
        return 1
    elif cmp1 < cmp2:
        return -1
    else:
        return 0
    
print(data1)
data1.sort(key=cmp_to_key(myCmp))
print(data1)