from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        # [17, 14, 9]
        total = 0
        s = list(s)
        for i in range(len(shifts) - 1, - 1, -1):
            total += shifts[i]
            s[i] = self.shift(i, s, total)

        return ''.join(s)
        
    

    def shift(self, index: int, s: str, count: int) -> str:
        return chr((ord(s[index]) - ord('a') + count) % 26 + ord('a'))