class Solution:
    def mySqrt(self, x: int) -> int:
        
        # Binary search on all integers.
        start = 0
        end = x

        while start <= end:
            mid = start + ((end - start) // 2)
            curr = mid * mid
            if curr == x:
                return mid
            elif curr > x:
                end = mid - 1
            else:
                start = mid + 1

        # Same concept as 35. Insert Search Position.
        # If the target is not a perfect square, the rounded down
        # number will be the end index.
        return end