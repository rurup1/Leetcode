class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        stack = []

        for i, item in enumerate(s):
            if item in stack:
                continue
            
            while stack and item < stack[-1]:
                if stack[-1] not in s[i:]:
                    break
                
                stack.pop()
            
            stack.append(item)
        return ''.join(stack)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i

        seen = set()
        stack = []

        for i, char in enumerate(s):
            if char in seen:
                continue
            
            while stack and stack[-1] > char and i < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())

            seen.add(char)
            stack.append(char)

        return ''.join(stack)

