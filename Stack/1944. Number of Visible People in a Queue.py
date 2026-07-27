from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0] * len(heights)
        for i, height in enumerate(heights):                
            while stack and stack[-1][0] < height:
                shorter, idx = stack.pop()
                res[idx] += 1
            
            if stack:
                res[stack[-1][1]] += 1
            
            stack.append((height, i))
        return res