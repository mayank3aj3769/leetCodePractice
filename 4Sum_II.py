import collections
from typing import List

  # LC 454
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        dd=collections.defaultdict() # to store count of a+b in a hashmap
        for a in nums1:
            for b in nums2:
                if a+b in dd:
                    dd[a+b]+=1
                else:
                    dd[a+b]=1
        
        # Now in 2 loops for c+d , check if -(a+b) exits in hashmap and increment count by dd[-(a+b)]
        target=0
        for c in nums3:
            for d in nums4:
                if -(c+d) in dd:
                    target+=dd[-(c+d)]
        
        return target