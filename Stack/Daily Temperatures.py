from typing import *

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute force:
        # Start at index i: traverse until reach a larger temperature
        # Store the # of days in res array
        res = [0] * len(temperatures)
        for i in range(len(temperatures)): # loop through each temp
            for j in range(i + 1, len(temperatures)): # loop until we reach a higher temp
                if temperatures[j] > temperatures[i]: # if future_temp > ith_temp
                    res[i] = j - i
                    break
                continue

        return res
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Stack solution:

        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            ## While the stack is not empty and the current temperature is greater 
            ## than the top of the stacK:

            while len(stack) and temp > stack[-1][0]:
                ## This means we have hit a day where past days are at a smaller temperature
                ## Pop that past day off the stack, compute the dist between days
                top = stack.pop()
                res[top[1]] = i - top[1]
            
            ## If the current temp is less than past days, push it onto the stack
            stack.append((temp, i))

        return res
