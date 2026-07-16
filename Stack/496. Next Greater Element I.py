from typing import List
from collections import defaultdict

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        def find_next_greatest(index):
            j = index
            while index < len(nums2) - 1:
                if nums2[j] < nums2[index + 1]:
                    return nums2[index + 1]

                index += 1
            return -1
        
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ans.append(find_next_greatest(j))

        return ans

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ng = defaultdict(lambda: -1)

        for num in nums2:
            while stack and stack[-1] < num:
                ng[stack.pop()] = num
            
            stack.append(num)

        return [ng[num] for num in nums1]