class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Less overhead. All we really need to know if whether i - j == 1, but this will be true 
        # if the prev_score is 0 as well. So, we can use max() to achieve the same solution.
        stack = [0]
        for item in s:
            if item == "(":
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(2 * val, 1)

        return stack[-1]
    
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        curr_score = 0
        for i, item in enumerate(s):
            if item == "(":
                stack.append((i, curr_score))
                curr_score = 0
            else:
                j, prev_score = stack.pop()
                if i - j == 1:
                    curr_score = prev_score + 1
                else:
                    curr_score = prev_score + (2 * curr_score)
        return curr_score