from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # Ignore cards fully
        # This is just the smallest distance between two duplicates


        table = {}
        least = inf

        for i, num in enumerate(cards):
            if num in table:
                least = min(i - table[num] + 1, least)

            table[num] = i

        return least if least != inf else -1
        

            