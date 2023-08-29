# Definition for a binary tree node.
from typing import Optional
# LC 101

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isMirror(root1,root2): ##Auxilliary recursive function
            if root1==None and root2==None:  # if both nodes are none , then they are same 
                return True
            else:
                if (root1!=None and root2!=None): # if both nodes are not none, compare values , then match left node with 
                                                  # right of another and vice versa 
                    return (root1.val==root2.val) and isMirror(root1.left,root2.right) and isMirror(root1.right,root2.left)
                else:
                    return False # if one of nodes is None and other is not None , it is not a mirror

        return isMirror(root,root) ## to check if the tree is a mirror image of itself
        