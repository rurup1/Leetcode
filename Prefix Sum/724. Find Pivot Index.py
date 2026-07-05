from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Ideas:
        # 1. Solve this similarly to how I solve Find Pivot Integer
        # 2. This time the array is not sorted, I cannot do n(n+1)/2
        
        # This would be done by finding left prefix sum - right prefix sum
        
        # O(n) time and space
        # Optimal? Thinking no.....
        # I can solve by just computing the total sum from the left and
        # storing the total sum.

        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            # This is the key here.
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i

            left_sum += num
        return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Ideas:
        # 1. Solve this similarly to how I solve Find Pivot Integer
        # 2. This time the array is not sorted, I cannot do n(n+1)/2
        
        # This would be done by finding left prefix sum - right prefix sum

        left = [0] * len(nums)
        left_total = 0
        for i in range(len(nums)):
            left_total += nums[i]
            left[i] = left_total

        right = [0] * len(nums)
        right_total = 0
        for j in range(len(nums) - 1, -1, -1):
            right_total += nums[j]
            right[j] = right_total

        res = [0] * len(nums)
        for k in range(len(nums)):
            res[k] = left[k] - right[k]

            if res[k] == 0:
                return k

        return -1

