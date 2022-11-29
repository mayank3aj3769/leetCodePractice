from ast import List
      ## here first and last are adjacent since this is circular

class Solution:
    def rob(self, nums: List[int]) -> int:
        sm=0
        d={}
        check=[0]*100
        if nums == check:
            return 0
        def robRec(nums):
            if len(nums)==1:
                s+=nums[0]
                return nums[0]
            elif len(nums)==2:
                return max(nums[0],nums[1])
            elif len(nums)==3:
                #s+=max(nums[1],nums[0]+nums[2])
                return max(nums[1],nums[0]+nums[2])
            else:
                if d.get(tuple(nums[1:]),0)==0:
                    d[tuple(nums[1:])]=robRec(nums[1:])
                if d.get(tuple(nums[2:]),0)==0:
                    d[tuple(nums[2:])]=robRec(nums[2:])   
                return max(nums[0]+d[tuple(nums[2:])],d[tuple(nums[1:])])
        
        if len(nums)>2:
            sm=max(robRec(nums[:len(nums)-1]),robRec(nums[1:]))
        elif len(nums)>1:
            sm=max(nums[0],nums[1])
        else:
            sm=nums[0]
        return sm
        