class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=''
                   # start at mid
        maxl=0
        for i in range(len(s)):
          l=i  # len of s is odd
          r=i
          while(l>=0 and r<len(s) and(s[l]==s[r])):
            if (r-l+1)>maxl:
                  maxl=r-l+1
                  res=s[l:r+1]
            l-=1
            r+=1
          
          l=i
          r=i+1  # len of s is even
          while(l>=0 and r<len(s) and (s[l]==s[r])):
            if(r-l+1)>maxl:
                  maxl=r-l+1
                  res=s[l:r+1]
            l-=1
            r+=1
          
        return res


