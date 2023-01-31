class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first,second=float('inf'),float('inf')
        ## if you found three smallest numbers in increasing order then true . if list exhausted , then False
        for num in nums:
            if num<=first:   
                first=num
            elif num<=second:
                second=num
            else:
                return True
        
        return False
                