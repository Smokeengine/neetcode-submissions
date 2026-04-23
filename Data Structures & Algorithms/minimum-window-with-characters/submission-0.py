class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}
        smap = {}
        for i in range(len(t)):
            tmap[t[i]] = 1 + tmap.get(t[i], 0)
        l = 0
        have = 0
        need = len(tmap)
        res = ""
        for r in range(len(s)):
            smap[s[r]] = 1 + smap.get(s[r], 0)
            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have += 1
            while have == need:
                if not res or r-l+1 < len(res):
                    res = s[l:r+1]
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]]< tmap[s[l]]:
                    have -= 1
                l += 1
        return res
                

                
        