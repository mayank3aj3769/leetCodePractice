class Solution:
    ## len(s1) -> N and len(s2)--> M
    ## Take two hashmaps and use sliding window to check hashmap of each substring of len N until either 
    ## you find one or you reach end of string 
    def checkInclusion(self, s1: str, s2: str) -> bool:

        N=len(s1)
        M=len(s2)
        d1=[0]*26
        d2=[0]*26
        l=0
        r=0
        if N>M:
            return False

        for i in range(0,N):
            d1[ord(s1[i])-ord('a')]+=1
            d2[ord(s2[i])-ord('a')]+=1
        
        r=N-1
        l=0
        while(r<=M-1):
            if d1==d2:
                return True
            r+=1
            if(r<M):
                d2[ord(s2[r])-ord('a')]+=1
            d2[ord(s2[l])-ord('a')]-=1
            l+=1
       
        return False