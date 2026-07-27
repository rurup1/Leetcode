from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        res = [nums[0]]
        for num in nums:
            if num >= res[-1]:
                res.append(num)

        return len(res) - 1