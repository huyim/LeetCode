class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        common = ""
        while True:
            if_common = True
            for element in strs:
                if len(element) > i and element[i] == strs[0][i]:
                    continue
                else:
                    if_common = False
                    break
            if if_common == True and len(strs) > 0:
                common += strs[0][i]
                i += 1 
            else:
                break

        return common  