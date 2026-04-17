class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key in res:
                res[key].append(strs[i])
            else:
                res[key] = [strs[i]]
        return list(res.values())