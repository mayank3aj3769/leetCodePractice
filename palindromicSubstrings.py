class Solution:
    def countSubstrings(self, s: str) -> int:
        tempSt=''
        front=0
        back=0
        count=0
        #tots=set(list(s))
        '''
        if self.checkPalin(s)==True:
            if len(s)==1:
                return count
        else:
            count=len(set(list(s)))
        
        while(front<len(s)-1):
            tempSt=s[back:front]
            if (self.checkPalin(tempSt)==True and len(tempSt)!=1):
                count+=1
            front+=1
        back+=1
        while(back<=len(s)-1):
            tempSt=s[back:front]
            if (self.checkPalin(tempSt)==True and len(tempSt)!=1):
                count+=1
            back+=1  
        temp=set(list(s))
        '''
        res = [s[i: j] for i in range(len(s))
          for j in range(i + 1, len(s) + 1)]

        for i in res:
            if self.checkPalin(i)==True:
                count+=1
        return count

    def checkPalin(self,s):
        if s==[]:
            return False
        if len(s)==1:
            return True
        
        front =0
        back=len(s)-1
        while(back >=front):
            if s[front]!=s[back]:
                return False
            front+=1
            back-=1
        
        return True