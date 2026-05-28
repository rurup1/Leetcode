from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Target: O(logn) -> Binary search

        # Start at the middle, if the middle element is less than the target, 
        # increment by m / 2.
        #
        # If the middle element is greater than the target, decrement the pointer by m / 2

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1