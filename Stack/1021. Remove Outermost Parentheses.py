class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        depth = 0
        res = ""
        for item in s:
            if item == "(":
                depth += 1
            else:
                depth -= 1
            
            stack.append(item)
            if not depth:
                res += ''.join(stack[1:-1])
                stack = []
        return res            