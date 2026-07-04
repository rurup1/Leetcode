class Solution:
    def pivotInteger(self, n: int) -> int:

        def leftRightDifference(nums: List[int]) -> List[int]:
            # O(n) time and O(1) space      
            ans = [0] * len(nums)

            left_sum = 0
            for i in range(len(nums)):
                ans[i] = left_sum
                left_sum += nums[i]

            right_sum = 0
            for j in range(len(nums) - 1, -1, -1):
                ans[j] = abs(ans[j] - right_sum)
                right_sum += nums[j]

            return ans
        
        nums = list(range(1,n+1))
        res = leftRightDifference(nums)
        for i, num in enumerate(res):
            if num == 0: return i + 1
        return -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        res = (n * (n+1)) // 2
        pivot = int(res ** 0.5)

        return pivot if pivot ** 2 == res else -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        
        total = 0
        table = [0] * (n)
        for i in range(1,n+1):
            total += i
            table[i-1] = total
        
        table_reverse = [0] * n
        total = 0
        for j in range(n-1, -1, -1):
            total += (j+1)
            table_reverse[j] = total

        for k in range(len(table)):
            if table[k] == table_reverse[k]:
                return k + 1

        return -1          