import math
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        if k == 1:
            return 0
        
        res = math.inf
        nums.sort()
        
        i = 0
        j = k - 1

        while j < len(nums):
            diff = nums[j] - nums[i]
            if diff < res:
                res = diff
            
            i += 1
            j += 1
        
        return res
    
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        # i is smallest in window
        # i + k - 1 is largest in window

        return min(nums[i + k - 1] - nums[i] for i in range(len(nums) - k + 1))
        
        