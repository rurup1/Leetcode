from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Helper functions
        def swap(arr, a, b):
            temp = arr[a]
            arr[a] = arr[b]
            arr[b] = temp

        def reverse(arr, i):
            a,b = i, len(arr) - 1

            while a < b:
                swap(arr, a, b)
                a += 1
                b -= 1

        # We need to solve this problem by finding the "local" max.

        # We know that the largest permutation in some local indices in an array are
        # while nums[i] >= nums[i + 1]. So, we can loop through the array until the condition is
        # not met.

        i = len(nums) - 2

        # While i is valid and nums[i] >= nums[i + 1]
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Now we are one index to the left of a local max. We need to find an index to the right of nums[i]
        # such that it is JUST larger than nums[i]

        # First check if i is even valid
        if i >= 0:
            j = len(nums) - 1
            # Because we are already in decreasing order, know that the first nums[j] that we hit that is
            # greater than nums[i] is GUARANTEED to be the value that is "just" larger than nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            swap(nums, i, j)
        
        # Finally, we just need to reverse the elements that after index i
        reverse(nums, i + 1)