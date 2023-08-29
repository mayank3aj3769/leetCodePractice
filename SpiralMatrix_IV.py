# Definition for singly-linked list.
# LC 2326
from typing import Optional,List
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        top=0
        bottom=m-1
        left=0
        right=n-1
        mat=[[-1 for _ in range(n)] for _ in range(m)] # careful with matrix initialization
        while top<=bottom and left<=right: ## sequence of spiral traversal is right --> down -->left-->up 
            
            #move right
            for j in range(left,right+1):
                if head==None:
                    return mat
                data=head.val
                head=head.next
                mat[top][j]=data
            top+=1
            #move down
            for j in range(top,bottom+1):
                if head==None:
                    return mat
                data=head.val
                head=head.next
                mat[j][right]=data
            right-=1

            #move left
            if top<=bottom: # avoids revisiting
                for j in range(right,left-1,-1):
                    if head==None:
                        return mat
                    data=head.val
                    head=head.next
                    mat[bottom][j]=data
                bottom-=1

            #move up
            if left<=right:
                for j in range(bottom,top-1,-1):
                    if head!=None:
                        data=head.val
                        head=head.next
                        mat[j][left]=data
                left+=1

        return mat