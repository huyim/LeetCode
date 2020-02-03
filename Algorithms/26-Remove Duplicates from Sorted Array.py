class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 1
        
        for i in range(len(nums) - 1):   
            if (nums[i + 1] > nums[i]):
                nums[length] = nums[i + 1]
                length += 1
                  
        return length
