from typing import *


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    
    # 1. 
    # Loop through strings, check if the sorted(str) is in the results array.
    # If not, add it into the results
    # Return results array

    ## Make the results a dict with key: freq_count and value: arr of words that match that freq count

    ## O(m * n) space??


    res = {}
    for str in strs:
        
        ## Build the frequency table
        freq = {}
        for letter in str:
            freq[letter] = 1 + freq.get(letter, 0)
        
        freq = tuple(freq)
        
        if freq in res:
            res[freq].append(str)
        else:
            res[freq] = [str]
    
    return list(res.values())