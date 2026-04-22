class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1hmap = {}
        s2hmap = {}
        
        l = 0
        k = len(s1)
        for i in range(len(s1)):
            s1hmap[s1[i]] = 1 + s1hmap.get(s1[i], 0)
            
            
        for r in range(len(s2)):
            s2hmap[s2[r]] = 1 + s2hmap.get(s2[r], 0)
            if r - l + 1 > k:
                s2hmap[s2[l]] -= 1
                if s2hmap[s2[l]] == 0:
                    del s2hmap[s2[l]]
                l+=1
            if s2hmap == s1hmap:
                return True
        return False

            
        