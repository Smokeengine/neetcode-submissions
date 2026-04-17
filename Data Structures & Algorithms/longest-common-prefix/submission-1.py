class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            flag = True
            c = strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != c:
                    flag = False
                    break
            if flag == False:
                return res
            else:
                res+= c
        return res
        