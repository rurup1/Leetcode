from typing import 
import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second_max = -math.inf

        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            if num < second_max:
                return True
            
            while stack and stack[-1] < num:
                second_max = max(second_max, stack.pop())

            stack.append(num)
            
        return False