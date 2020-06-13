# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:30:35 2020

@author: Jason
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p != None and q != None:
            if p.val == q.val:
                left = self.isSameTree(p.left, q.left)
                right = self.isSameTree(p.right, q.right)
                return left and right
            else:
                return False
        elif p == None and q == None:
            return True
        else:
            return False