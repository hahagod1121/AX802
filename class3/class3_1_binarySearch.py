# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:27:05 2020

@author: Jason
"""

import time

data = [0,1,2,3,4,5,6,7,8,9]

def binarySearch(data:list,value:int):
    upper = len(data) - 1
    lower = 0
    
    while lower <= upper:
        mid = (upper + lower) // 2
        midValue =  data[mid]
        
        if midValue < value:
            lower = mid + 1
        elif midValue > value:
            upper = mid - 1
        else:
            return mid


start = time.time()     
print(binarySearch(data,7))
end = time.time()

print(start - end)