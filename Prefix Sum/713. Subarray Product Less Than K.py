from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Sliding window approach

        i = 0
        total = 1
        res = 0
        for j, num in enumerate(nums):
            total *= num

            while total >= k:
                total //= nums[i]
                i += 1

            res += j - i + 1

        return res