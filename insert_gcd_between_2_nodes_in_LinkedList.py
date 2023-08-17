# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def gcd(self,a,b):  ## function to find gcd using euclidean method
        if a==b:
            return a
        elif a>b:
            return self.gcd(a-b,b)
        elif a<b:
            return self.gcd(a,b-a)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head

        while(curr!=None):   # add a new node between every two nodes 
            nextNode=curr.next     
            if curr.next!=None:
                a,b=curr.val,nextNode.val # if there are odd number of nodes leave the last node untouched
            else:
                break
            n=self.gcd(a,b)
            newNode=ListNode(n,None)
            newNode.next=nextNode
            curr.next=newNode
            curr=nextNode       # skip the added node to move ahead
        
        return head