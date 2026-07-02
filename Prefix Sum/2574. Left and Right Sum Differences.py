from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        # O(n) time and O(1) space      
        ans = [0] * len(nums)

        left_sum = 0
        for i in range(len(nums)):
            ans[i] = left_sum
            left_sum += nums[i]

        right_sum = 0
        for j in range(len(nums) - 1, -1, -1):
            ans[j] = abs(ans[j] - right_sum)
            right_sum += nums[j]

        return ans

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        # O(n) time and O(n) space
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        res = [0] * len(nums)

        total = sum(nums)
        for i in range(len(nums)):
            total -= nums[i]
            rightSum[i] = total
        
        total = sum(nums)
        for j in range(len(nums) - 1, - 1, -1):
            total -= nums[j]
            leftSum[j] = total

        for k in range(len(nums)):
            res[k] = abs(leftSum[k] - rightSum[k])

        return res
