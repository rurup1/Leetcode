from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Find the max average
        # We can do this by maintaining a set of k values
        # Find the average each iteration
        if k == len(nums):
            return sum(nums) / k

        # 1 12 -5 -6 50 3
        #  1 12 -5 -6 50

        res = -inf

        total = sum(nums[0:k])
        
        for i in range(k, len(nums)):
            if (total / k) > res:
                res = total / k

            total -= nums[i-k]
            total += nums[i]
        
        
        if total / k > res:
            return total / k
        else:
            return res