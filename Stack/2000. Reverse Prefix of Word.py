class Solution:
    # Stack solution
    # 1. Find append characters to the stack until we find the index of ch
    # 2. Then, stack.pop() to return in reverse order from index 0 ... index_of_ch
    # 3. Then, add the rest of the characters in word

    # NOTE: This is a suboptimal solution. The more optimal solution is one that has O(1) auxiliary space,
    # which is the two pointers solution
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        found = False
        idx = 0
        for char in word:
            stack.append(char)
            if char == ch:
                found = True
                break

            idx += 1

        if not found:
            return word

        res = ""

        while stack:
            res += stack.pop()

        for i in range(idx+1, len(word)):
            res += word[i]

        return res

class Solution:

    # Regular two pointers reverse solution.
    # 1. Find the index of first appereance of ch
    # 2. If present, continue to 3, else nothing to do
    # 3. Reverse from [0,i], where i is the index we found

    # NOTE: We strings do not support item assignment. We must convert to list and
    # then back to a string.
    def reversePrefix(self, word: str, ch: str) -> str:
        res = -1
        for i, char in enumerate(word):
            if char == ch:
                res = i
                break

        if res == -1:
            return word
        
        return self.reverse(word, 0, res)

    def reverse(self, word: str, start: int, end: int) -> str:
        word = list(word)
        i, j = start, end
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

        return ''.join(word)

