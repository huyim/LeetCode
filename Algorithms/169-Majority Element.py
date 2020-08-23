class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for element in nums:
            if element not in counter:
                counter[element] = 1
            else:
                counter[element] += 1
        
        return max(counter, key=counter.get)