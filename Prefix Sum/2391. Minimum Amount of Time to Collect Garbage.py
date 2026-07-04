from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Need to figure out ways to not visit each house.

        # IDEAS:
        # 1. The length of all the elements of the array are guaranteed to be 1. So, I don't
        # even need individual paper_count, glass_count, metal_count.

        count = 0
        for items in garbage:
            count += len(items)

        # 2. Now if I rebuild that prefix table and then locate the highest index where each element is, then we know it is guaranteed that we must travel that far.
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        
        # Finds the last occurrence of some item, and then finds the time it takes to get there using the prefix sum table we built.
        # This is worst case O(n), but most cases just traverses a few times until it reaches.
        def locate_last(garbage: List[str], item: str) -> int:
            last = 0
            for i in range(len(garbage) - 1, -1, -1):
                if item in garbage[i]:
                    last = i
                    break

            return travel[last - 1] if last > 0 else 0

        return count + locate_last(garbage, 'P') + locate_last(garbage, "G") + locate_last(garbage, "M")

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        def locate_last(garbage: List[str], item: str) -> int:
            last = 0
            for i in range(len(garbage) - 1, -1, -1):
                if item in garbage[i]:
                    last = i
                    break

            return travel[last - 1] if last > 0 else 0

        count = 0
        for i, items in enumerate(garbage):
            if 0 < i < len(travel):
                travel[i] += travel[i - 1]

            count += len(items)
            
        return count + locate_last(garbage, 'P') + locate_last(garbage, "G") + locate_last(garbage, "M")

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Sub-optimal solution
        # Uses prefix-sum for travel array but nothing else.

        # Need to figure out a way to not visit every house.
        for k in range(1, len(travel)):
            travel[k] += travel[k - 1]

        paper_count, paper_time = 0, 0
        glass_count, glass_time = 0, 0
        metal_count, metal_time = 0, 0
        for i, items in enumerate(garbage):
            for item in items:
                if item == "P":
                    paper_count += 1
                    if i > 0:
                        paper_time = travel[i - 1]

                elif item == "G":
                    glass_count += 1
                    if i > 0:
                        glass_time = travel[i - 1]

                else:
                    metal_count += 1
                    if i > 0:
                        metal_time = travel[i - 1]

        return paper_count + paper_time + glass_count + glass_time + metal_count + metal_time

        # BUGS:

        # 1. Does not consider the case when a truck skips a location because it is not present.
        # 1 -> 2 -> 3. If nothing is present at 1,2, then we move to 3 and only add the travel distance from 1 -> 2, not 2 -> 3

        # 2. Adds the travel distance when we there are multiple of the same item at the same location.
        # "GG". The truck will increment from glass, but add travel distance for each instance of G. (overcounting)

        # SOLUTIONS:
        
        # 1. I think I can solve this by using a prefix sum table for the cumulative travel distance. We do not +=, just set equals to.
            

            
