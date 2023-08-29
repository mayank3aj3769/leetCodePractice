# Definition for a binary tree node.
# LC 572
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
                
        if root is None: # if root doesn't exist , returns false
            return False
        if subRoot is None:
            return True
        if self.isSame(root,subRoot): ## for given  node as root in main tree , check if it is same as subtree or not
            return True  ## if yes , return true
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) #otherwise check if any 1
                                                                            # of remaining nodes of main
                                                                            # tree as root  is same as subtree
    
    def isSame(self,root1,root2): ## checks if two trees are same 
            if root1 is None and root2 is None: ## if both roots are null , they are same
                return True
            if root1 and root2 and root1.val==root2.val: # if both are not null and have same values , check
                                                         # recursively for all the children . if any 1 mismatches return false
                                                         # else return true 
                return self.isSame(root1.right,root2.right) and self.isSame(root1.left,root2.left)
            return False
        