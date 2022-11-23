# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def inO(p,q):
            if p and q:
                if p.val!=q.val:
                    return False
                else:
                     return inO(p.left,q.left) and inO(p.right,q.right)
            elif p==None and q==None:
                 return True
            else:
                 return False
        
        return inO(p,q)