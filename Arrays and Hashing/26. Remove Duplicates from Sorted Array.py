from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                i -= 1

            i += 1

        return len(nums)
    

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # [1,1,2]
        # [1,2]
        # i=1, j=1
        # if nums[j] == nums[i-1]
        # nums[j] = nums[j+1]


        # [0,0,1,1,1,2,2,3,3,4]


        # Initialize pointers
        i = 1
        j = 1

        # The j pointer loops through all elements
        while j < len(nums):

            # This is the case where duplicates are present.
            # We move j past the first set of duplicates
            if nums[j] == nums[i - 1]:
                j += 1
            else: 
                # When we hit this, i and j are distinct elements,
                # We've skipped past the duplicates, so set nums[i] = nums[j]
                # We can finally increment i and work on whatever the next set of duplicates is.
                nums[i] = nums[j]
                i += 1
        
        # We return i because i will point at the last unique element
        # Therefore, i is the length of the unique array.
        return i
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        #Another way to try this is to overwrite dups as we go

        # [0,0,1,1,1,2,2,3,3,4]
        # [0,1,2,3,4,_,_,_,_,_]
            
        # This is the exact same solution as before, just in reverse

        # If nums[j] does not equal nums[i - 1], we can safely overwrite
        # nums[i] to nums[j].

        # This works because in the case that nums[i - 1] == nums[j],
        # we skip past all of these occurences, so j is guaranteed to be
        # a unique value.
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i