from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count the number of 0s, 1s, and 2s
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        # Overwrite the values in the array to the count of 0s, 1s, and 2s
        for i in range(zeros):
            nums[i] = 0
        
        for j in range(zeros, zeros + ones):
            nums[j] = 1
        
        for k in range(zeros + ones, len(nums)):
            nums[k] = 2

# This is the same solution as the first one, just cleaned up the 
# manual overwriting.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Count the number of 0s, 1s, and 2s O(n) 
        zeros = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        # Overwrite the values in the array to the count of 0s, 1s, and 2s O(n)

        for i in range(len(nums)):
            if i < zeros:
                nums[i] = 0
            elif i >= zeros and i < zeros + ones:
                nums[i] = 1
            else:
                nums[i] = 2

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr: List[int], i: int, j: int) -> None:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        # There is a Dutch National Flag algorithm
        zeros = 0 # nums[0:zeros] are all the zeros
        ones = 0 # nums[zeros:ones] are all the ones
        twos = len(nums) - 1 # nums[twos+1:] are all the twos


        # Notice that the values that we cannot guarantee yet are the values from
        # nums[ones:twos+1]. Therefore, we loop while ones <= twos. Once this condition is false,
        # there are no more unknowns and the array is sorted.

        while ones <= twos:
            if nums[ones] == 0:
                # Here we found a zero. So we swap it into the zeros subarray.
                # It is safe to increase the zeros pointer here because we just added an element
                # It is also safe to increase the ones pointer here because we know that the element that we just swapped with is guaranteed
                # be in the processed region, so it must be a 0 or a 1.
                swap(nums, zeros, ones)
                zeros += 1
                ones += 1
            elif nums[ones] == 1:
                # Here we found a one. We can safely increment the size of the ones subarray by increasing the ones pointer. No swaps are needed.
                # We do not increment zero because we want zero to point at the end of the zeros subarray and not leak into any ones
                ones += 1
            else:
                # Else, we found a two. We can swap the value at the ones pointer with the value at the twos pointer. Then we can decrement
                # the twos pointer because we just swapped a confirmed two into that subarray. No need to increment the zeros pointer here because all zeros to the left. No need to increment the ones pointer because after the swap, the value of the ones pointer is unknown.
                swap(nums, ones, twos)
                twos -= 1