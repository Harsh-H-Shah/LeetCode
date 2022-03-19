class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        braces = {"{":"}", "(":")","[":"]"}
        
        for c in s:
            if c in braces:
                arr.append(c)
            elif len(arr) != 0 and c == braces[arr[-1]]:
                arr.pop()
            else:
                return False
        if len(arr) == 0:
            return True
        else:
            return False