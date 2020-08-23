class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = sorted(nums)
        target = 0

        for i in range(0, len(l), 2):
            if i == len(l) - 1 or l[i] != l[i+1]:
                target = l[i]
                break

        return target

#异或
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for num in nums:
            a = a ^ num
        return a

#注解：异或解法：异或运算满足交换律，a^b^a=a^a^b=b,因此ans相当于nums[0]^nums[1]^nums[2]^nums[3]^nums[4]..... 
#然后再根据交换律把相等的合并到一块儿进行异或（结果为0），然后再与只出现过一次的元素进行异或，这样最后的结果就是，
#只出现过一次的元素（0^任意值=任意值）
