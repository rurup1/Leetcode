from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
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
    
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        start = 0
        end = len(nums) - 1
        mid = -1

        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                # Find last occurence
                ending_pos, starting_pos = mid, mid
                while ending_pos < len(nums) and nums[ending_pos] == target:
                    ending_pos += 1
                
                
                # Find first occurence
                while starting_pos >= 0 and nums[starting_pos] == target:
                    starting_pos -= 1

                return [starting_pos + 1, ending_pos - 1]
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return [-1,-1]
