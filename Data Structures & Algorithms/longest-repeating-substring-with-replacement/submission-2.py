class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hmap = {}
        maxf = 0
        res = 0
        for r in range(len(s)):
            hmap[s[r]] = 1 + hmap.get(s[r], 0)
            maxf = max(maxf, hmap[s[r]])
            if (((r-l+1) - maxf) <= k):
                res = max(res, r-l+1)
            else:
                hmap[s[l]] -=1
                l+=1
        return res
        