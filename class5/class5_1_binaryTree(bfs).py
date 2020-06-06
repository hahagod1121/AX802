# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 10:44:35 2020

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

def countBfs(root:node):
    if root is None:
        print("None")
        return 0
    queue = [root]
    count = 1
    print("value:") 
    while queue:
        node = queue.pop(0)
        
        
        if node.left:
            queue.append(node.left)
            count += 1
        
        if node.right:
            queue.append(node.right)
            count += 1
        
        print(node.value)
    print("count:")
    print(count)
    

countBfs(root)


        
