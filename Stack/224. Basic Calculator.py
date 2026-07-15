class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        curr_sum, number, sign = 0, 0, 1
        for item in s:
            if item == "(":
                stack.append((curr_sum, sign))
                sign = 1
                curr_sum = 0
            elif item == ")":
                prev_sum, saved_sign = stack.pop()
                curr_sum += sign * number
                curr_sum = (curr_sum * saved_sign) + prev_sum
                number = 0
            elif item.isdigit():
                number = (10 * number) + int(item)
            else:
                curr_sum += sign * number
                number = 0

                sign = -1 if item == '-' else 1

        curr_sum += sign * number
        return curr_sum