# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast=head
        slow=head
        count=0
        while(count<n):
            fast=fast.next
            count+=1
        
        if fast==None and n==1: ## if list has only 1 element
            return None
        if fast==None and n!=1: ## if list has n elements and nth node is to be removed , return the first node
            return head.next
    
        prev=slow

        while(fast!=None):
            prev=slow
            fast=fast.next
            slow=slow.next

        prev.next=slow.next

        return head

