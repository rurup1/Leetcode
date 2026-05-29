from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 4Sum

        ## How can I solve this:

        ## 3Sum approach. Loop for all nums[a], for all nums[b], then we can use
        # two pointers to find nums[c] and nums[d]

        nums.sort()
        print(f'{nums=}')
        res = []

        for a in range(len(nums)):
            # Standard duplicates check
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            # print(f'{a=}')

            # This tracks if a is incremented or not. We need this for the duplicate check
            # for b.
            incremented = True
            for b in range(a + 1, len(nums)):

                # Duplicate check for b during each iteration of a
                # If a has been incremented, we should not increment b as well
                # because nums[a] + nums[b] != nums[a - 1] + nums[b - 1] even if
                # nums[b] == nums[b - 1]

                ## Therefore, we only check if nums[b] == nums[b - 1] if a
                # has not been immediately incremented
                if b > 1 and nums[b] == nums[b - 1] and not incremented:
                    continue

                # Set incremented to false inside the b loop so incremented only gets set to True
                # if a changes.
                incremented = False
                c, d = b + 1, len(nums) - 1
                find = target - nums[a] - nums[b]

                while c < d:
                    if nums[c] + nums[d] == find:
                        res.append([nums[a], nums[b], nums[c], nums[d]])

                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif nums[c] + nums[d] < find:
                        c += 1
                    else:
                        d -= 1   
        return res