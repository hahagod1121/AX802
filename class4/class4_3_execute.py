# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:49:41 2020

@author: Jason
"""

from class4_2_tree import node

root = node(100)


Node =  node(5)
root.child.append(Node)
Node = node(80)
root.child.append(Node)

print(root.value)
print(root.child[0].value)
print(root.child[1].value)
