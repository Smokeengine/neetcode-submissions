class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
            else:
                skip_left = self.isPalindrome(s, l+1, r)
                skip_right = self.isPalindrome(s,l,r-1)
                return skip_left or skip_right
        return True

    def isPalindrome (self, s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True

        

 