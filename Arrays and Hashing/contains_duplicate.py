from typing import *

def hasDuplicate(nums: List[int]) -> bool:
    ## If number in set, break

    ## If number is not in set, add it to set

    ## Loop through entire list

    seen = set()
    for num in nums:
        if num in seen:
            return False
        
        seen.add(num)
    
    return True