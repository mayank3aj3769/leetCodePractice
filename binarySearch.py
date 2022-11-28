from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start=0
        end=len(nums)-1
        mid=(end-start)//2
        
        def  f(nums,start,end,target):
            mid=(end+start)//2
            if start > end :
                return -1
            if nums[start]==target:
                return start
            if nums[end]==target:
                return end
         
            else:
                if target == nums[mid]:
                    return mid
                elif target < nums[mid]:
                    return f(nums,start,mid-1,target)
                else:
                    return f(nums,mid+1,end,target)
        
        k=f(nums,start,end,target)
        
        return k

        