class Solution:
    def threeSum(self, nums):
        res=[]
        for i in range(0,len(nums)):
            if i!=len(nums)-1:
                target=0-nums[i]
                temp=self.twoSum(nums[i+1:],target)
                if temp !=None :
                    temp.append(nums[i])
                else:
                    temp=[]
                temp.sort()
                res.append(temp)
                
        return res
    
    def twoSum(self,num,target):
        for i in range(0,len(num)):
            if i < len(num)-i:
                t=target-num[i]
                if t not in num[i+1:]:
                    continue
                else:
                    res=[]
                    ind=num[i+1:].index(t)
                    res.append(i)
                    res.append(ind+i+1)
                    return res
            else:
                res=[]
                if num[-1] == target-num[i]:
                    res.append(i)
                    res.append(len(num)-1)
                    return res
                
                

sol=Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))