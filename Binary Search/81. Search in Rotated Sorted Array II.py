from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        return self.binary_search(nums, target)

    def binary_search(self, arr: List[int], target: int) -> bool:

        # [0,1,2,2,4,4,4,5,6,6,7]
        # [4,5,6,6,7,0,1,2,4,4]
        # [4,5,6,6,7 ......]


        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if arr[m] == target:
                return True
            elif arr[m] == arr[l] == arr[r]:
                r -= 1
                l += 1
                continue
            
            if arr[m] >= arr[l]:
                if arr[m] >= target >= arr[l]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if arr[m] <= target <= arr[r]:
                    l = m + 1
                else:
                    r = m - 1



        return False