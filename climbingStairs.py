class Solution:
    res=[0]*46
    def climbStairs(self, n: int) -> int:
        
        if n<=3:
            self.res[n-1]=n
            return n
        else:
            if self.res[n-2]==0:
                self.res[n-2]=self.climbStairs(n-1)
            if self.res[n-3]==0:
                self.res[n-3]=self.climbStairs(n-2)
            self.res[n-1]=self.res[n-2]+self.res[n-3]
            return self.res[n-1]