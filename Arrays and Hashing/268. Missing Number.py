from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
    
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        len_sum = (n * (n+1)) // 2
        nums_sum = sum(nums)

        return len_sum - nums_sum