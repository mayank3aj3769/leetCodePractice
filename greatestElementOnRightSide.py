### Here it's faster to start comparing from last ind,otherwise it would be O(n^2)

class Solution:
  
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxt=-1
        for i in range(len(arr)-1,-1,-1):
           newMax=max(arr[i],maxt)
           arr[i]=maxt
           maxt=newMax
        
        

        return arr
 