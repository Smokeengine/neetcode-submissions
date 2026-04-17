class Solution:
    def isPalindrome(self, s: str) -> bool:
        res =""
        for l in s:
            if l == " ":
                continue
            if l.isalnum():
                res += l
        res = res.lower()
        temp=""
        for r in range(len(res)-1,-1,-1):
            temp+=res[r]
        if(temp==res):
            return True
        else:
            return False


        