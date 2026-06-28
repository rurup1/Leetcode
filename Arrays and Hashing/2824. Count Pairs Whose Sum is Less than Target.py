from typing import List

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        print(f'{nums=}')
        i, j = 0, len(nums) - 1
        res = 0
        while i < j:
            if nums[i] + nums[j] < target:
                res += j - i
                i += 1
            else:
                j -= 1
        
        return res
    
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] < target:
                    res += 1
        
        return res