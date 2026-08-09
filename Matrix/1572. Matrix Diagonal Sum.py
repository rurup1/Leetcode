from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i, j = 0, 0
        total = 0
        while i < len(mat) and j < len(mat):
            total += mat[i][j]
            i += 1
            j += 1

        i = 0
        j -= 1
        while i < len(mat) and j > -1:
            total += mat[i][j] if i != j else 0
            i += 1
            j -= 1

        return total