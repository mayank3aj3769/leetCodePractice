'''
Approach is :- for every i , find all pairs in remaining array whose sum of elements is -i .. Do this for entire list .
Result would be a 2D list [[i,x,y],[i,x1,y1],....[i,xn,yn]...]

'''


'''
Approach is :- for every i , find all pairs in remaining array whose sum of elements is -i .. Do this for entire list .
Result would be a 2D list [[i,x,y],[i,x1,y1],....[i,xn,yn]...]

'''


class Solution:
    def threeSum(self, nums): 
        res=[]
        for i in range(0,len(nums)):
            if i+1 < len(nums)-3:
                target=0-nums[i]
                if target==0:
                    continue
                temp=self.twoSum(nums[i+1:],target)
                if temp !=None  and temp!=[]:
                
                    for k in temp:
                        k.append(nums[i])
                        k[0]=nums[i+1+k[0]]
                        k[1]=nums[i+1+k[1]]
                        k.sort()   
                    
                    for x in temp:
                        if x not in res:
                            res.append(x)
                else:
                    continue
            else:
                if nums[-3]+nums[-2]+nums[-1]== 0:
                    t=[nums[-3],nums[-2],nums[-1]]
                    if t not in res:
                        res.append(t)
        
        return res
    
    def twoSum(self, nums,target):
        ans=[]
        for i in range(0,len(nums)):
            res=[]
            if i+1  < len(nums)-1:
                temp=nums[i+1:]
                if target-nums[i] not in temp:
                    continue
                else:
                    ind=nums[i+1:].index(target-nums[i])
                    res.append(i)
                    res.append(ind+i+1)
                   
            else:
                temp=nums[-1] 
                if temp == target-nums[i]:
                    res.append(len(nums)-2)
                    res.append(len(nums)-1)
                
            if res not in ans and res!=[]:
                ans.append(res)
        return ans

t=[3,0,-2,-1,1,2]
sol=Solution()
print(sol.threeSum(t))