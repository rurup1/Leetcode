from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Non-binary search solution
        # h_score -> nums[i] >= len(nums) - i
        # return len(nums) - i

        # [0,1,3,5,6]
        # [1,2,100]
        # [100]
        res = 0
        l, r = 0, len(citations) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if citations[m] >= len(citations) - m:
                res = len(citations) - m
                r = m - 1
            else:
                l = m + 1

        return res
    
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        # [0,1,3,5,6]
        # They published 5 papers.
        # Of those, 3 papers got published more than 3 times
        # max(nums[i] == i + 1 for i in range(len(nums)))


        # Non-binary search solution?
        # 
        res = set()
        # h_score -> nums[i] >= len(nums) - i
        # return len(nums) - i


        for i in range(len(citations)):
            if citations[i] >= len(citations) - i:
                res.add(len(citations) - i)

        return max(res) if res else 0