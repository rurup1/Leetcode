from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        start, end = 0, len(matrix) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            row = matrix[mid]
            if row[0] <= target <= row[-1]:
                break
            elif target > row[-1]:
                start = mid + 1
            else:
                end = mid - 1
        
        start, end = 0, len(row) - 1
        while start <= end:
            mid = start + ((end - start) // 2)
            if row[mid] == target:
                return True
            elif row[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False
    