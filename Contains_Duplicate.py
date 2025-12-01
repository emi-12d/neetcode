from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
print(Solution().hasDuplicate([1, 2, 3, 3]))