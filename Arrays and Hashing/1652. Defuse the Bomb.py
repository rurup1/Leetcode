from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        final = [0] * len(code)

        for i in range(len(code)):
            res = 0
            # If k = 0, then ith number is 0
            if k == 0:
                final[i] = 0
                continue
            elif k > 0:
                # Replace the ith number with the sum of the next k numbers
                for j in range(1,k+1):
                    res += code[(i+j) % len(code)]

                final[i] = res
            else:
                for j in range(1,abs(k)+1):
                    res += code[(i-j) % len(code)]

                final[i] = res


        return final
