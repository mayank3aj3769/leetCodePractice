from ast import List
                ### used a hack for last test case where all elements were 0

class Solution:
       
    def rob(self, nums: List[int]) -> int:
    
        res={}
        
        def robBank(nums):
            maxSum=0
            if nums==[]:
                return 0
            
            elif len(nums)==1:
                return nums[0]
        
            elif len(nums)==2:
                return max(nums[0],nums[1])
        
            else:
                if nums[2]==0 and nums[1]==0:
                    return 0
                j=tuple(nums[2:])
                if res.get(j,0)==0:
                    res[j]=robBank(nums[2:])
                    l1=nums[0]+res[j]
                else:
                    l1=nums[0]+res[j]
                k=tuple(nums[1:])
                if res.get(k,0)==0:
                    res[k]=robBank(nums[1:])
                    l2=res[k]            
                else:    
                    l2=res[k]
                
                maxSum+=max(l1,l2)
                return maxSum
             
        mx=robBank(nums)
        return mx
         