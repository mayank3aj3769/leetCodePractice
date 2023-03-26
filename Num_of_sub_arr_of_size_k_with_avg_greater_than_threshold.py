class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0
        l=0
        r=0
        win=[]
        sm=sum(arr[:k-1]) # take sum of first k elements as starting point 
        for l in range(len(arr)-k+1):
            sm+=arr[l+k-1] # now array would start from kth index till len(arr)-k+1
            if sm/k>=threshold: #check threshold condition
                res+=1
            sm-=arr[l] #to slide the window remove the current (left most) element
     
        return res


