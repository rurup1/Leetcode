from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # [4,5,6,7,0,1,2]
        # [3,4,5,1,2]
        # [1,2,3,4,5,6,0]
        # [0,1,2,3,4,5,6,7]
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (end + start) // 2
            if nums[mid] < nums[end]:
                end = mid
            else:
                start = mid + 1

        return nums[start]
            
        
        