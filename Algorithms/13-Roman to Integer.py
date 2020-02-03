class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        
        rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s)):
            if i > 0 and rome[s[i]] > rome[s[i - 1]]:
                sum = sum + rome[s[i]] - 2 * rome[s[i - 1]]
            else:
                sum += rome[s[i]]
                    
        return sum
