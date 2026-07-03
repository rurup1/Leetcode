from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Actually do not need an array here.
        total = 0
        highest = 0

        for height in gain:
            total += height
            highest = max(total, highest)

        return highest

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pref = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            pref[i + 1] = pref[i] + gain[i]


        return max(pref)