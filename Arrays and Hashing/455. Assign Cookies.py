from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # g[i] -> represents the size of a cookie that a kid will accept
        # s[i] represents the size of the cookie that I have

        # My Issue:
        # I need to assign a valid cookie to every possible kid I have,
        # but after I assign a cookie, I cannot assign THAT cookie again

        # Transform s from List[int] into List[(int, bool)]
        g.sort()
        s.sort()

        i = 0
        j = 0

        while i < len(s) and j < len(g):
            if s[i] >= g[j]:
                j += 1
            i += 1
        
        return j