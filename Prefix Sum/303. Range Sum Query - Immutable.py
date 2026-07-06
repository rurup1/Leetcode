from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

        # Build prefix table
        self.res = [0] * len(self.nums)
        total = 0 
        for i in range(len(self.nums)):
            total += self.nums[i]
            self.res[i] = total

    def sumRange(self, left: int, right: int) -> int:
        return self.res[right] - self.res[left -1] if left > 0 else self.res[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)