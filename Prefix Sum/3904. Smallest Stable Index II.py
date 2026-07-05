from typing import List
import math

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # ATTEMPT 1
        # This is a suboptimal solution for sure, need to figure out how to do it without
        # O(n) space.
        
        # Need to find the largest and smallest values from left to right from each index.
        # Let's start with max
        largest = []
        x = -1
        for num in nums:
            x = max(num, x)
            largest.append(x)

        y = math.inf
        res = -1
        for j in range(len(nums) - 1, -1 , -1):
            y = min(y, nums[j])
            if largest[j] - y <= k:
                res = j

        return res