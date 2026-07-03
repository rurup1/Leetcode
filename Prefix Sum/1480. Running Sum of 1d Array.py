from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Use prefix sum for this, in-place solution as well
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total

        return nums