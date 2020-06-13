# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:23:09 2020

@author: Jason
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is not None:
            if root.left is None and root.right is None:
                return 1
            elif root.left is None and root.right is not None:
                right = self.minDepth(root.right)
                return right + 1
            elif root.right is None and root.left is not None:
                left = self.minDepth(root.left)
                return left + 1
            elif root.right is not None and root.left is not None:
                left = self.minDepth(root.left)
                right = self.minDepth(root.right)
                if left < right:
                    return left + 1
                if right < left:
                    return right + 1
                else:
                    return right + 1
        else:
            return 0