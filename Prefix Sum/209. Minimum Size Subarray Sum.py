from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # This screams prefix sum because we are summing over subarrays
        # But how could I do it?

        # I think I can solve it with sliding window as well.
        # [2,3,1,2,4,3]
        # How do I know when grow or shrink the window?

        i = 0
        j = 0
        total = 0
        res = math.inf
        count = 0
        while i < len(nums) and j < len(nums):
            total += nums[j]

            while total >= target:
                res = min(j - i + 1, res)
                total -= nums[i]
                i += 1
            j += 1
        
        return res if res != inf else 0