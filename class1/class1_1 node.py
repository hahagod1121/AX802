# -*- coding: utf-8 -*-
"""
Created on Sat May  9 09:37:22 2020

@author: Jason
"""

import class1_2_linkinglist as ll
        
mylist = ll.linkinglist()
mylist.trace()
for i in range(10):
    mylist.append(i)
mylist.delete(3)
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