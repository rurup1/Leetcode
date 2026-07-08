from typing import List
import math

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Ideas:
        # I need to find a contiguous subarray with an equal number of 0s and 1s
        # My idea: curr_sum * 2 == j - i + 1
        # Claude's idea: If we see a 1: +1, if we see a 0: -1.
        # How could I incorporate this into O(1) lookups?
        # Hashmap of every single time we hit a 0.

        # It is symmetric. [1,2,3,4,3,2,1]
        # Length is indices from 1....1

        # Bad practice...
        # if len(nums) == 2 and sum(nums) == 1:
        #     return 2

        
        table = {0: -1}
        res = -math.inf
        total = 0
        for i in range(len(nums)):
            total += 1 if nums[i] == 1 else -1
            if total in table:
                res = max(res, i - table[total])
            else:
                table[total] = i

        return res if res != -math.inf else 0