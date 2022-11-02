## Leetcode 1  

class Solution:
    def twoSum(self, nums,target):
        for i in range(0,len(nums)):
            if i+1  != len(nums)-1:
                temp=nums[i+1:]
                if target-nums[i] not in temp:
                    continue
                else:
                    res=[]
                    ind=nums[i+1:].index(target-nums[i])
                    res.append(i)
                    res.append(ind+i+1)
                    return res
            else:
                res=[]
                temp=nums[-1] 
                if temp == target-nums[i]:
                    res.append(i)
                    res.append(i+1)
                    return res
                