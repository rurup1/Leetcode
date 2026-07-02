from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        
        
        banned = set(banned)
        total = 0
        res = 0

        for i in range(1, n+1):
            if i in banned:
                continue
            
            total += i
            if total > maxSum:
                break
            
            res += 1

        return res