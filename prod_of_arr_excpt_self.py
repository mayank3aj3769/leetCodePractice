# leetcode 238

class Solution:
    def productExceptSelf(self, nums):
        ans=[]
        prod=0
        temp=0
        flag1=0
        flag2=0
        count=0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                if flag1==0:
                    prod=nums[i]
                    flag1=1
                else:                    
                    prod*=nums[i]   
            
            else:
                flag2=1
                count+=1
                if count>=2:
                    break
        
        for i in range(0,len(nums)):
            if count==2:
                nums[i]=0
            elif flag2==1 and nums[i]!=0 : ## check for 0 in arr and ele non zero
                nums[i]=0
            elif flag1==1 and nums[i]==0 and count<2:## check for 1 non 0 in arr and ele zero            
                nums[i]=prod
            elif flag1==0: ## all 0 zero in arr
                nums[i]=0
            else:
                nums[i]=int(prod/nums[i])
        
        return nums

s=Solution()
t=s.productExceptSelf([-1,1,0,-3,3])
for i in t:
    print(i)