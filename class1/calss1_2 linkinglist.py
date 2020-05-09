# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:17:21 2020

@author: Jason
"""

class linkinglist:
    def __init__(self):
        self.head = node(0)
    def trace(self):
        run = self.head.next
        while run != None:
            print(run.value)
            run = run.next
    def append(self,value):
        run = self.head
        while run.next != None:
            run = run.next
        run.next = node(value)