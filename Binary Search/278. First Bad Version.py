# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # [1, 2, .. n]
        start, end = 1, n
        while start <= end:
            m = start + ((end - start) // 2)
            if isBadVersion(m):
                end = m - 1
            else:
                start = m + 1

        return start
