class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # traverse backwards to avoid dependency
        # append 0 in the end , start at i=N-3  till i=-1
        # return min of cost[0] and cost[1] , it has been provided that there are 2 elements at least
        
        
        cost.append(0)
        
        for i in range(len(cost)-3,-1,-1):
            cost[i]+=min(cost[i+1],cost[i+2])
        
        return min(cost[0],cost[1])

