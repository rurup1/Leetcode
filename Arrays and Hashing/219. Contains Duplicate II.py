from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Sliding window while maintaining hash set.

        window = set()

        for i in range(len(nums)):
            if nums[i] in window:
                return True
            
            window.add(nums[i])

            # This is the key part. With this, we make sure that the window is at most
            # length k. 
            if len(window) > k:
                window.remove(nums[i - k])

        return False

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # We can also use a hash table approach to maintain num-index pairs

        res = {}
        for i, num in enumerate(nums):
            if num in res and abs(i - res[num]) <= k:
                return True
            
            res[num] = i

        return False
        