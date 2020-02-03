class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = []
        
        if (s == ""):
            l.append(0)
        
        for i in range(len(s)):
            temp = ""
            temp += s[i]
            if (i == len(s) - 1):
                l.append(len(temp))
            else:
                for j in s[i+1:]:
                    if j in temp:
                        l.append(len(temp))
                        temp = ""
                        break;
                    else:
                        temp += j
                l.append(len(temp))
                
        return max(l)
