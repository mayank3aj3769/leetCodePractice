from ast import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res=[]
        sm=0
        lastInt=0
        for i in range(0,len(operations)):
            N=len(res)
            if operations[i]=='+':
                temp=res[-1]+res[-2]
                res.append(temp)
                sm+=temp
            elif operations[i]=='D':
                temp=2*res[-1]
                res.append(temp)
                sm+=temp
            elif operations[i]=='C':
                temp=res.pop()
                sm-=temp
            else:
                res.append(int(operations[i]))
                sm+=res[-1]
        return sm