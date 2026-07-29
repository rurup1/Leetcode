from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat

        reshaped = [[0] * c for _ in range(r)]
        for i in range(m * n):
            reshaped[i // c][i % c] = mat[i // n][i % n]

        return reshaped

class Solution:
    def flatten(self, mat):
        res = []

        for row in mat:
            for item in row:
                res.append(item)

        return res

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m * n != r * c:
            return mat


        reshaped = [[0] * c for _ in range(r)]
        mat = self.flatten(mat)[::-1]
        for i in range(r):
            for j in range(c):
                reshaped[i][j] = mat.pop()

        return reshaped