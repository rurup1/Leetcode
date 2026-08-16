from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        i = 1
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                matrix[top][j] = i
                i += 1
            top += 1
            for k in range(top, bottom + 1):
                matrix[k][right] = i
                i += 1
            right -= 1

            if left <= right:
                for l in range(right, left - 1, -1):
                    matrix[bottom][l] = i
                    i += 1
                bottom -= 1
            
            if top <= bottom:
                for m in range(bottom, top - 1, -1):
                    matrix[m][left] = i
                    i += 1
                left += 1
        
        return matrix