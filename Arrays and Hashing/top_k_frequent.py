from typing import *

## Goal: O(n) time and O(n) space

# Given an integer array and k, return most k frequent elements in the array


## Creating a frequency table and sorting by values in reverse order, then we just returned the first k (top k)
def topKFreqeunt(nums: List[int], k: int) -> List[int]:

    res = []
    # Create a frequency table
    freq = {}
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)
    
    # Sort by values in decreasing order (O(n log n))
    sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

   # Return top k
    for i, num in enumerate(sorted_freq):
        if i < k:
            res.append(num)
        else:
            break

    return res

## Bucket sort. Sort by count
def topKFrequent_2(nums: List[int], k: int) -> List[int]:
    freq = {}
    buckets = [[] for i in range(len(nums) + 1)]

    for num in nums:
        freq[num] = 1 + freq.get(num, 0)

    for num, count in buckets.items():
        buckets[count].append(num)
    
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)


