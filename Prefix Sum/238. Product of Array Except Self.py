from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        total = 1
        for i, num in enumerate(nums):
            ans[i] = total
            total *= num

        total = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] = ans[j] * total
            total *= nums[j]

        return ans
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Without division operation??
        # O(n)

        # I don't think I am doing this right....
        # Prefix is total from 0 ... i
        # Suffix is total from i + 1 ... len(nums)

        prefix = [0] * len(nums)
        total = 1
        for i, num in enumerate(nums):
            prefix[i] = total
            total *= num

        print(f'{prefix}')
        suffix = [0] * len(nums)
        total = 1
        for j in range(len(nums) - 1, -1 ,-1):
            suffix[j] = total
            total *= nums[j]

        ans = []
        for k in range(len(nums)):
            ans.append(prefix[k] * suffix[k])

        return ans

        