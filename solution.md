# Title
Maximum Difference Between Odd and Even Character Frequencies

# Intuition
The problem asks for the difference between the highest odd frequency and the lowest even frequency of characters in a string. My first thought was to count the frequency of each character and then separate them into odd and even counts to find the required values.

# Approach
- Use `Counter` to count the frequency of each character in the string.
- Iterate through the frequency values:
  - If the count is odd, update `max_odd` if it's larger.
  - If the count is even, update `min_even` if it's smaller.
- Return the difference between `max_odd` and `min_even`.

# Complexity
- Time complexity:  
  $$O(n)$$ (where \( n \) is the length of the string, for counting and iterating frequencies)
- Space complexity:  
  $$O(1)$$ (since there are at most 26 lowercase letters, the space for the counter is constant)

# Code
```python3 []
from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_even = float("inf")
        map_s = Counter(s)
        for val in map_s.values():
            if val % 2 != 0:
                max_odd = max(val, max_odd)
            else:
                min_even = min(val, min_even)

        return max_odd - min_even
```
