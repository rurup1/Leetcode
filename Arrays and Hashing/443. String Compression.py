from typing import List

class Solution:
    def compress(self, chars: List[str]):
        
        def add_count_in_arr(s, index, count) -> int:
            if count == 1:
                return index
            if count < 10:
                s[index] = str(count)
                index += 1
            else:
                for num in str(count):
                    s[index] = str(num)
                    index += 1

            return index
        
        if len(chars) == 1:
            return 1

        i = 0
        j = 1
        write = 0

        while j < len(chars):
            chars[write] = chars[i]
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            
            write = add_count_in_arr(chars, write + 1, j - i)
            i = j

        return write