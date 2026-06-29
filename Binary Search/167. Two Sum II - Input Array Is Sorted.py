from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        # O(n) optimal solution
        # Two pointers
        i, j = 0, len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binary_search(start: int, end: int, target: int) -> int:
            while start <= end:
                mid = start + ((end - start) // 2)
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            
            return -1
        # nums[i] + nums[j] == target
        res = []

        for i in range(len(numbers)):
            start, end = i + 1, len(numbers) - 1
            find = target - numbers[i]
            res = [i+1, binary_search(start, end, find)+1]
            if res[1] != 0:
                return res