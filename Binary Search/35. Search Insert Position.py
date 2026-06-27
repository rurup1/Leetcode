from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Standard binary search.
        # When low == high, return the index that we stopped that.
        # That index is the one to return

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        # start always holds the index that we need to 
        # insert the element at if it does not already exist inside the array
        return start