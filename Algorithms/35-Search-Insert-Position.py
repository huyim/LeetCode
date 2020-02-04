class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        position = -1
        
        for i in range(len(nums)):
            if (target > nums[i]):
                if ((i + 1) == len(nums) or target <= nums[i + 1]):
                    position = i + 1
                    break
            elif (target <= nums[i]):
                position = i
                break
                
        return position
