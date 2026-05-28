class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # nums[i] + nums[j] + nums[j] == 0
        # -nums[i] = nums[j] + nums[j]

        # Set target as -nums[i]
        # Run a two pointer approach for j and k
        # if nums[j] + nums[k] = -nums[i]:
        # .add([nums[i], nums[j], nums[j]])


        # We need to sort the array in increasing order so that we Q# # can increment/decrement # the two pointers properly
        nums.sort()
        res = []
        

        for i in range(len(nums)):
            # Avoid duplicated targets:
            if i > 0 and nums[i] == nums[i- 1]:
                continue

            j, k = i + 1, len(nums) - 1 # set two pointers
            target = -nums[i]

            while j < k:
                if nums[j] + nums[k] == target:
                    print(f'{nums=}')
                    print(f'{i=}, {j=},{k=}')
                    res.append([nums[i], nums[j], nums[k]])

                    ## After finding a solution and next values are the same (avoid duplicates)
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        
        return res


