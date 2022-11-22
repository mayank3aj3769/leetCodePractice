class Solution:
    def characterReplacement(self,s, k):          ## partial correct ; inefficient approach

        curr=0
        ans=0
        N=self.findlon(s)
        if k==0:
            return N
        else:                
            n=k
            temp=[]
            for i in range(0,len(s)):
                if i!=len(s)-1:
                    if s[curr]==s[i]:
                        temp.append(s[curr])
                        ans=max(ans,len(temp))
                    else:
                        if n>0:
                            temp.append(s[curr])
                            n-=1
                            ans=max(ans,len(temp))
                        else:
                            curr=i
                            temp=[]
                            n=k
                else:
                    if n>0:
                        temp.append(s[curr])
                        ans=max(ans,len(temp))
                    else:
                        n=k
                        temp.append(s[curr])
                        n-=1
            
        if N+k<len(s):
            ans=N+k
        else:
            ans=len(s)

        return ans

    def findlon(self,st):
        res=1
        s=0
        ind=0
        for i in range(0,len(st)):
            if i<len(st)-1:
                if st[ind]==st[i]:
                    s+=1
                    res=max(res,s)
                else:
                    ind=i
                    s=1
            else:
                if st[ind]==st[i]:
                    s+=1
                    res=max(res,s)
                 
        return res        


sol=Solution()
t="KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
k=4
print(sol.characterReplacement(t,k))