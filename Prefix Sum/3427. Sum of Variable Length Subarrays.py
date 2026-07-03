from typing import List

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # Avoids continuous sums
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = nums[i] + prefix[i]

        print(f'{prefix=}')
        res = 0
        for i in range(len(nums)):
            start = max(0, i - nums[i])
            res += prefix[i + 1] - prefix[start]
        
        return res
    
class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        # start = max(0, i - nums[i])
        # [2,3,1]
        # 2, 2 - 1. Max(0,1) = 1. -> [1..2]

        # Not a prefix sum solution. O(n^2)
        res = 0
        for i, num in enumerate(nums):
            start = max(0, i - nums[i])
            total = sum(nums[start:i+1])
            res += total

        return res