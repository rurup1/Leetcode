class Solution:
    def isValid(self, s: str) -> bool:
        # Loop through s:
        #   if opening bracket: add to stack
        #   if closing bracket: check if stack.pop() is the correspondent

        stack = []
        for item in s:
            if item in "({[":
                stack.append(item)
            elif stack:
                if item == "}":
                    if stack.pop() != "{":
                        return False
                elif item == ")":
                    if stack.pop() != "(":
                        return False
                else:
                    if stack.pop() != "[":
                        return False
            else:
                return False
        
        return not stack