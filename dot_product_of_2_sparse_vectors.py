import collections
from typing import List

# LC 1570 

class SparseVector:
    def __init__(self, nums: List[int]):
        self.v1=nums
        self.d=collections.defaultdict(int)  # when initializing , create a dict of non zero index and their values
        for i in range(len(nums)):
            if nums[i]!=0:
                self.d[i]=nums[i]

        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans=0
        for k,v in self.d.items(): # iterate over dict of one of objects 
            if k in vec.d:            # if common key exists in both dicts that means , non-zero values at same index
                    ans+=v*vec.d[k]
        return ans

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)