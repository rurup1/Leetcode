from typing import List

class Solution:
    def flipAndInvertRow(self, row):
        i, j = 0, len(row) - 1
        while i <= j:
            row[i] = 0 if row[i] == 1 else 1
            if i != j:
                row[j] = 0 if row[j] == 1 else 1
            
            row[i], row[j] = row[j], row[i]
            i += 1
            j -= 1
        
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            self.flipAndInvertRow(row)

        return image