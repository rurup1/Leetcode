class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s) - 2):
            a, b, c = s[i], s[i + 1], s[i + 2]
            if a != b and b != c and a != c:
                res += 1
        
        return res
    


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        i = 0
        j = 2
        res = 0
        while j < len(s):
            substring = s[i:j+1]
            if len(set(substring)) == 3:
                res += 1
            
            i += 1
            j += 1

        return res