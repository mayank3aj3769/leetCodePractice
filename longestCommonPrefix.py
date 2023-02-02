class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        commonSoFar=strs[0]
        res=''
        for i in range(1,len(strs)):
            temp=strs[i]
            ch=''
            for j in range(0,min(len(commonSoFar),len(temp))):
                if temp[j]==commonSoFar[j]:
                    ch+=temp[j]
                else:
                    break
            commonSoFar=ch
        
        return commonSoFar
