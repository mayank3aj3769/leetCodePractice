class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag=True
        N=len(s)
        sp=0
        w=0
        for i in range(0,N):      # flag= false --> same word , true indicates new word
            if s[i]!=' ' and flag==True:
                flag=False
                w=i
            elif s[i]==' ':
                flag=True


        count=0
        while(w<N):
            if s[w]!=' ':
                count+=1
                w+=1
            else:
                break
            
        
        return count
