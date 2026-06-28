from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        # Need to binary search on every row in the grid,
        # target = 0
        # [4,3,2,1,0,-2,-4]
        def binary_search(arr: List[int]):
            start, end = 0, len(arr) - 1
            res = 0
            while start <= end:
                mid = start + ((end - start) // 2)
                if arr[mid] == 0:
                    res = len(arr) - 1 - mid
                    start = mid + 1
                elif arr[mid] > 0:
                    start = mid + 1
                else:
                    end = mid - 1
            
            
            return res if res else len(arr) - start


        res = 0
        for i in range(len(grid)):
            res += binary_search(grid[i])
        
        return res