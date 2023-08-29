# Definition for a binary tree node.
#LC 879
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder=[]

        def inorderT(root):
            nonlocal inorder
            if root ==None:
                return 
            else:
                inorderT(root.left)
                inorder.append(root.val)
                inorderT(root.right)

        inorderT(root)

        temp=TreeNode()
        curr=temp
        for i in inorder:
            curr.right=TreeNode(i)
            curr=curr.right
        
        return temp.right


