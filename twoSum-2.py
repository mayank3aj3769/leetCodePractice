class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # use two pointers left and right
        res=[]
        left=0
        right=len(numbers)-1

        while left<right:
           
            if numbers[left]+numbers[right]==target:  # found target
                res.append(left+1)
                res.append(right+1)
                break
            elif numbers[left]+numbers[right]<=target: # increase sum so shift left by 1
                left+=1
            else:    # sum is more than target , so decrease right
                right-=1

            ## ****** This approach works only if array is sorted

        return res