from typing import List

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # Something to do with uppercase

        # query = queries[0]

        # print(f'{query=}')
        # print(f'{pattern=}')

        # i = 0 
        # j = 0
        # res = []
        # while i < len(query) and j < len(pattern):
        #     if query[i] == pattern[j]:
        #         j += 1
        #     elif query[i].isupper():
        #         return False
        #     i += 1

        # return True


        res = []
        for query in queries:
            i = 0
            j = 0
            add = True
            while i < len(query):
                if j < len(pattern) and query[i] == pattern[j]:
                    j += 1
                elif query[i].isupper():
                    add = False
                    break
                i += 1

            res.append(add if j == len(pattern) else False)

        return res
            

