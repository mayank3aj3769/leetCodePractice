class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ## backtracking recursive solution
        res=[]

        if len(nums)==1:           # base case for 1 element left
            return [nums[:]]

        for i in range(len(nums)):
            n=nums.pop(0) # take the first element of list
            perms=self.permute(nums)  # recursive call fn on remainder list --> return 2D list

            for j in perms:
                j.append(n) ## add n back to all the lists
            res.extend(perms)  ## since adding multiple lists to one list
            nums.append(n) # adding back the initial element removed

        return res  