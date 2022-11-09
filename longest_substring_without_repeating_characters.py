## Naive approach  . Used sliding window with 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp=[]
        ans=0
        res=0
        i=0
        while i in range(0,len(s)):
            if s[i] not in temp:
                if temp==[]:
                    curr=i
                temp.append(s[i])
                if len(temp) >ans:
                    ans=len(temp)
                if ans > res:
                    res=ans
                i+=1
            else:
                ans=0
                i=curr+1
                curr=i
                temp=[]
    
                temp.append(s[i])
                if len(temp) > ans:
                    ans=len(temp)
                if ans > res:
                    res=ans
                i+=1
            
        
        return res

sol=Solution()
s="pwwkew"
n=sol.lengthOfLongestSubstring(s)
print(n)