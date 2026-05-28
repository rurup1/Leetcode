from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums[i] + nums[j] + nums[k] ~ target
        # target - nums[i] = nums[j] + nums[k]

        # Run a similar two-pointer approach to normal 3Sum.

        nums.sort()
        # print(f'{nums=}')
        closest = float('inf')
        for i in range(len(nums) - 2):
            # Each target is searched exhaustively on one iteration, skip if duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j,k = i+1, len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # print(f'{total=}') 
                # print(f'Res: {abs(target-total)}')
                #  print(f'{i=}, {j=}, {k=}')
                #  print(f'{res=}')
                # print(f'Closest Before: {closest}')
                if abs(target - total) < abs(target - closest):
                    closest = total
                
                # print(f'Closest After: {closest}')

                if total == target: 
                    return target
                elif total < target:
                    j += 1
                else:
                    k -= 1
        return closest
    

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # nums[i] + nums[j] + nums[k] ~ target
        # target - nums[i] = nums[j] + nums[k]

        # Run a similar two-pointer approach to normal 3Sum.
        res = {}

        nums.sort()
        print(f'{nums=}')
        for i in range(len(nums) - 2):
            # Each target is searched exhaustively on one iteration, skip if duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            j,k = i+1, len(nums) - 1
            closest = target - nums[i]

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # print(f'{total=}') 
                # print(f'Res: {abs(target-total)}')             
                # res.add(abs(target - total))
                res[total] = abs(target - total)
                #  print(f'{i=}, {j=}, {k=}')
                #  print(f'{res=}')

                if nums[j] + nums[k] == closest: 
                    return target
                elif nums[j] + nums[k] < closest:
                    j += 1
                else:
                    k -= 1

        
        return min(res, key=res.get)