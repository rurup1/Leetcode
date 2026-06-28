from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        #  Find First and Last Positions binary search solution
        def searchRange(nums: List[int], target: int) -> List[int]:
            
            def binary_search(arr: List[int], target: int, find_first: bool) -> int:
                start, end = 0, len(arr) - 1
                res = -1

                while start <= end:
                    mid = start + ((end - start) // 2)
                    if arr[mid] == target:
                        res = mid
                        if find_first:
                            end = mid - 1
                        else:
                            start = mid + 1
                    elif arr[mid] < target:
                        start = mid + 1
                    else:
                        end = mid - 1

                return res


            return [binary_search(nums, target, True), binary_search(nums, target, False)]

        nums.sort()
        res = searchRange(nums, target)
        return list(range(res[0], res[1] + 1)) if res != [-1,-1] else []
    

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        # O(n) time O(1) space solution
        less = 0
        equal = 0
        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                equal += 1

        return list(range(less, less + equal))
    
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        # Claude solution - same as my O(n) solution but uses boolean-sum trick.
        less = sum(x < target for x in nums)
        equal = sum(x == target for x in nums)
        return list(range(less, less + equal))