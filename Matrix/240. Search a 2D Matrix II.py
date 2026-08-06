from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        m, n = len(matrix), len(matrix[0])

        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        
        return False

class Solution:
    def binary_search(self, row: List[int], target: int) -> bool:
        l, r = 0, len(row) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if row[m] == target:
                return True
            elif row[m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binary_search(row, target):
                return True

        return False