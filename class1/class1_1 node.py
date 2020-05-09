# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:37:22 2020

@author: Jason
"""

class node:
    def __init__(self,value):
        self.value = value
        self.next = None

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
        
mylist = linkinglist()
mylist.trace()
for i in range(100):
    mylist.append(i)
mylist.trace()

        
        

"""
a = node(10)

a.next = node(20)
a.next.next = node(30)
a.next.next.next = node(40)
a.next.next.next.next = node(50)


run = a
while run.next != None:
    run = run.next
    b = run.value
b += 10
run.next = node(b)

run = a
while run != None:
    print(run.value)
    run = run.next   
"""