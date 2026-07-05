from typing import List

class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # How to solve this using prefix sum?
        # Ideas:
        # 1. Build left prefix sum and right prefix sum
        # 2. Subtract left from right, and determine if solution is odd

        left_sum = 0
        res = 0
        total = sum(nums)
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            left_sum += num
            if (right_sum - left_sum) % 2 == 0:
                res += 1

        return res - 1 if res else 0
    
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # optimal solution
        # O(n), O(1) space
        return 0 if sum(nums) % 2 else len(nums) - 1