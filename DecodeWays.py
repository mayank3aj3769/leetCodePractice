class Solution:
    def numDecodings(self, s: str) -> int:
        dp={len(s):1} ## only 1 string of length N
        # dfs(i) checks for no. of possibilities of string of len(i+1) for 's' 
        #  
        def dfs(i):
            res=0
            if i in dp:
                return dp[i]   # already check for string of this length
            if s[i]=='0':
                return 0   # No character with 0, it starts from 1 till 26
            else:
                res=dfs(i+1) # generic recursive call in the normal case

            if( (i+1<len(s) and s[i]=='1') or ( i+1<len(s) and s[i]=='2' and s[i+1] in '0123456')  ):
                res+=dfs(i+2)  # if string is not over and s[i] is 1 , then s[i+1] can be anything 
                               # if string is not over and s[i] is 2 , then s[i+1] has to be between 0 to 6
            dp[i]=res
            return res
        
        return dfs(0)
    
'''
 bottom up approach 

 run for loop from last index :
 if s[i] ==0 
   dp[i]=0

else:
    dp[i]=dp[i+1]
    if( (i+1<len(s) and s[i]=='1') or ( i+1<len(s) and s[i]=='2' and s[i+1] in '0123456')  ):
      dp[i]+=dp[i+2]

return dp[0]








'''