from typing import List

class Solution:
    # This is clearly a monotonic stack problem. We want the stack to be strictly decreasing, 
    # such that for some day, we just find the local max, not the global max.

    # The stack holds past temperatures. If we hit a future temperature that is larger than the top
    # of the stack, we have found the days it takes for a future temperature to be larger.
    # Therefore, we pop that day, and subract the two indices between days.

    # We must store temp and index on the stack so we can compare temps and then subtract indices.
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                prevTemp, index = stack.pop()
                res[index] = i - index

            stack.append((temp, i))

        return res