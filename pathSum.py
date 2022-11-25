# Definition for a binary tree node.
class TreeNode:          ## Recursive approach ---too many iffs passess 113/117 TC  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root==None and targetSum==0:
            return False
        elif root==[]:
            return False
        else:
            flag=0
            ans=0
            def inO(root,targetSum,flag):
                if not root:
                    return 0
                if flag==-10:
                    return 0
               
                if targetSum==0 and root.left==None and root.right==None:
                    return 0
                if targetSum==0 and (root.left!=None or root.right!=None):
                    flag=-10
                    return 0
                if root.val==targetSum and root.right==None and root.left==None:
                    return root.val
                if (root.val==targetSum) and (root.right!=None or root.left!=None):
                    return 0
                
                else:
                    
                    leftsum=inO(root.left,targetSum-root.val,flag)
                    if flag==-10:
                        return 0
                    rightsum=inO(root.right,targetSum-root.val,flag)
                    if flag==-10:
                        return 0
                    if root.val+leftsum==targetSum:
                        leftsum+=root.val
                        return leftsum
                    elif root.val+rightsum==targetSum:
                        rightsum+=root.val
                        return rightsum
                    else:
                        return 0
                        
            
            ans=inO(root,targetSum,flag)
            if ans!=0:
                return True
            else:
                return False