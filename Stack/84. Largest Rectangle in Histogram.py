from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        
        for i, height in enumerate(heights):
            start_idx = i
            while stack and stack[-1][1] > height:
                j, prev_height = stack.pop()
                area = prev_height * (i - j)
                res = max(res, area)
                start_idx = j
            
            stack.append((start_idx, height))
        
        for i, height in stack:
            res = max(res, height * (len(heights) - i))

        return res