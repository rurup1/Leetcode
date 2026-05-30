from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        print(f'{nums=}')
        for i in range(1, len(nums)):
            print(f'{i=}') 
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                i -= 1

        return len(nums)
