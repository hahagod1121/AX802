# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:21:39 2020

@author: Jason
"""

import time

data = [1,4,3,2]

def bubbleSort(data:list):
    for i in range(len(data)):
        for j in range(len(data) - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

start = time.time()
bubbleSort(data)
end = time.time()

print(data,start - end)


