class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sliding window
        
        start at i --> check until either you get smaller prices[i] or till n --> store in max
        
        return max
        '''
        maxSoFar=0
        minVal=10000
        for i in range(0,len(prices)):
            if prices[i]<minVal:
                minVal=prices[i]
            if maxSoFar < prices[i]-minVal:
                maxSoFar=prices[i]-minVal
        
        return maxSoFar