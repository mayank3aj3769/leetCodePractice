  ## leetcode 1742

class Solution:
    def sumofdigits(self,n):
        ans=0
        while(n!=0):
            ans+=n%10
            n=int(n/10)
        
        return ans
    
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        res={}
        N=highLimit-lowLimit+1
        maxval=1
        
        for i in range(lowLimit,highLimit+1):
            s=self.sumofdigits(i)
            t={s,i}
            x=res.get(s)
            if res.get(s)==None:
                res[s]=i                                        
            else:
                if type(res[s])==list:
                    temp=res[s]
                    temp.append(i)            
                    res.update([(s,temp)])
                
                else:
                    temp=[res.get(s),i]
                    res.update([(s,temp)])
        
               
        for i in res.values():
            if type(i)==list:
                tempval=len(i)
                if maxval<tempval:
                    maxval=tempval
        
        return maxval
    


        

s=Solution()
print(s.countBalls(11,104))