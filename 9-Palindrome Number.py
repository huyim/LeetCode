class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (str(x) == ''.join(reversed(str(x)))):
            return True
        return False
