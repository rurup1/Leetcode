from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        valid = list(range(1,n+1))
        banned = set(banned)

        for num in valid:
            if num in banned:
                valid.remove(num)

        while sum(valid) > maxSum:
            valid.pop()

        return len(valid)