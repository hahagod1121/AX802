# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:40:00 2020

@author: Jason
"""

try:
    while True:
        length = int(input(""))
            
            
        datas = input("")
        datas = datas.split(" ")
        datas = list(map(int, datas))
                
                
        datas.sort()
        
        datas = list(map(str, datas))
        
        print(" ".join(datas))


except EOFError:
    pass