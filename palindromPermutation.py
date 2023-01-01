class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        res={}
        oddcount=0
        for i in s:
            m=res.get(i,0)
            if m==0:
                res[i]=1
            else:
                res[i]+=1
        
    
        ct=0
        for i in res.keys():
            if res[i]%2!=0:
                ct+=1
        if ct>1:
            return False
        else:
            return True

            
            
