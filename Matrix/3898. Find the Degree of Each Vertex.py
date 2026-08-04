class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        res = [0] * len(matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                res[r] += matrix[r][c]

        return res