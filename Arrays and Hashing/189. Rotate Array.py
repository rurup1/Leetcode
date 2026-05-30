from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [1,2,3,4,5,6,7], k=3
        # [5,6,7,1,2,3,4]

        # [7,6,5,4,3,2,1]
        # [5,6,7,4,3,2,1]
        # [5,6,7,1,2,3,4]
        def swap(arr, i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # One full reverse
        i, j = 0, len(nums) - 1
        while i < j:
            swap(nums, i, j)
            i += 1
            j -= 1

        print(f'{nums=}')
        
        # Reverse the first k
        
        i = 0
        j = (k % len(nums)) - 1
        while i < j:
            swap(nums, i, j)
            i += 1
            j -= 1

        print(f'{nums=}')

        
        # Reverse last k
        i = k % len(nums)
        j = len(nums) - 1
        while i < j:
            swap(nums, i, j)
            i += 1
            j -= 1

        print(f'{nums=}')

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        for _ in range(k):
            nums.insert(0, nums.pop())


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
