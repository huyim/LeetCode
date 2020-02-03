class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        
        while (index < len(nums)):
            if (nums[index] == val):
                nums.remove(val)
                index -= 1
            
            index += 1
            
        return len(nums)
