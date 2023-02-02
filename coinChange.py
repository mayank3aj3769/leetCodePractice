from ast import List


class Solution:
    def coinChange(self, coins, amount):
        res=[amount+1]*(amount+1)  # res stores no. of coins for amount 'i' 
        res[0]=0 # for amount ==0 return 0 
        ### 1 D array where initial value is more than max to check res[i] shows min no. of coins needed to make sum =i 
        
        for a in range(1,amount+1):
            for c in coins:
                if a>=c:
                    res[a]=min(res[a],1+res[a-c])
        
        if res[amount]!=amount+1:
            return res[amount]
        else:
            return -1

sol=Solution()
x=sol.coinChange([1,3,5,7],11)
y=3
assert x==y