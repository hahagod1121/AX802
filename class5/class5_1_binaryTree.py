# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 09:48:56 2020

@author: Jason
"""

class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
root = node(0)
root.left = node(1)
root.right = node(2)
root.left.left = node(3)
root.left.right = node(4)
root.right.left = node(5)
root.right.right = node(6)


def dfs(node:node):
    if not node:
        return 0
    leftnum = dfs(node.left)
    rightnum = dfs(node.right)
    
    return leftnum + rightnum + 1
    
    

dfs(root)