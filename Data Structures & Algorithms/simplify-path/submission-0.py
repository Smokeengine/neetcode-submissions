class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        paths = path.split('/')
        for c in paths:
            if c == '' or c == '.':
                continue
            if c == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(c)
        return "/" + '/'.join(stk)
