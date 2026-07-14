class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        encoded_string = ""

        for item in s:
            if item.isdigit():
                k = (k * 10) + int(item)
            elif item == "[":
                stack.append((k, encoded_string))
                k = 0
                encoded_string = ""
            elif item == "]":
                prevK, prevEncodedString = stack.pop()
                encoded_string = prevEncodedString + (prevK * encoded_string)
            else:
                encoded_string += item

        return encoded_string