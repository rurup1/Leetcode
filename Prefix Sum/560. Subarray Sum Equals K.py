from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # pref[i] - pref[j-1] == k
        # pref[i] = pref[j-1] + k

        # sum(i, j) == pref[j] - pref[i - 1]
        # Does pref[j] - pref[i - 1] == k???

        # If we are at pref[j], then does pref[j] == pref[i - 1] + k??

        # This keeps track of the totals we have seen so far...
        seen = {0: 1}

        # result count
        count = 0

        # current running total
        curr = 0
        for num in nums:
            curr += num
            count += seen.get(curr - k, 0)
            seen[curr] = 1 + seen.get(curr, 0)

        return count