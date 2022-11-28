# Definition for a binary tree node.
from typing import Optional

                 ## pathsum optimum approach --> recursive soln 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,countSum):
            if not root:
                return False
            else:
                countSum+=root.val
                if root.left==None and root.right==None:
                    return countSum==targetSum
                else:
                    return (dfs(root.left,countSum) or dfs(root.right,countSum))
        
        return dfs(root,0)