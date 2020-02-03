class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #goal = []
        
        #for i in range(len(nums)):
        #    for j in range(len(nums)):
        #        if i != j and nums[i] + nums[i+1:][j] == target:
        #            goal.append(i)
        #            goal.append(j)
        #    if len(goal) != 0:
        #        break
                
        #return goal
                     
        """
        Other people's solution
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
