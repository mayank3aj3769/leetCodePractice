from ast import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        
        res=defaultdict(list) # dict where k= one hot encoded tuple of alphabets ; val= list of strings
        
        for s in strs:
            temp=[0]*26 # empty list of 26 0s
            for i in s:
                temp[ord(i)-ord("a")]+=1 # taking ascii values as indexes ; subs ascii of 'a' from ascii of i 
            res[tuple(temp)].append(s) # make list as tuple since list cant be keys as they are mutable
        
        return res.values()