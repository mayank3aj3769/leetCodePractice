from ast import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # instead of searching for all substrings in dict do the opposite, search dictionary words for prefix
        d={}
         
        def f(s,wordDict):
            if s in wordDict:
                return True
        
            for i in range(len(wordDict)):
                temp=wordDict[i]
                n=len(temp)
                if s[:n]==temp:
                    test=s[n:]
                    if d.get(test,-1)!=-1:
                        if d[test]==1:
                            return True
                        else:
                            return False
                    else:

                        if test in wordDict:
                            d[test]=1
                            return True
                        else:
                            t=f(test,wordDict)
                            if t==False:
                                d[test]=0
                                continue
                            else:
                                d[test]=1
                                return True
                                
        
            return False

        return f(s,wordDict)
        