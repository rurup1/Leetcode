from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        j = 0
        for i in range(1, n + 1):
            if j == len(target):
                break
            
            stack.append('Push')
            if i == target[j]:
                j += 1
            else:
                stack.append('Pop')

        return stack