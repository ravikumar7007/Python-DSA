# Title
Maximum Adjacent Distance in a Circular Array

# Tags
array, math, absolute difference, sliding window, python

# Intuition
To find the largest difference between any two adjacent elements in the array (including the circular pair between the last and first elements), we can simply check the absolute difference for each adjacent pair.

# Approach
Iterate through the array, for each index compute the absolute difference between the current element and the previous one (using negative indexing to wrap around for the circular case). Use a generator expression with `max()` to efficiently find the largest difference.

# Complexity
- Time complexity:  
  $$O(n)$$ (where \( n \) is the length of the array)
- Space complexity:  
  $$O(1)$$ (constant extra space)

# Code
```python3 []
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        return max(abs(nums[i] - nums[i - 1]) for i in range(len(nums)))
```