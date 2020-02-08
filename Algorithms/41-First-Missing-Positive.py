class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mp = 1
        
        while (mp in nums):
            mp += 1
            
        return mp
