# Title
Maximum Difference by Digit Replacement

# Tags
math, string, greedy, digit-manipulation, python

# Intuition
The problem asks for the maximum difference you can get by replacing all occurrences of a single digit in a number with either 9 (to maximize) or 0 (to minimize). My first thought was to try replacing digits greedily: for the maximum, replace the first non-9 digit with 9; for the minimum, replace the first digit with 0.

# Approach
- Convert the number to a string for easy digit manipulation.
- For the maximum value, find the first digit that is not 9 and replace all its occurrences with 9.
- For the minimum value, replace all occurrences of the first digit with 0.
- Convert the resulting strings back to integers and return their difference.

# Complexity
- Time complexity:  
  $$O(n)$$, where \( n \) is the number of digits in the input number (since each digit is processed at most twice).
- Space complexity:  
  $$O(n)$$, for the string and list representations of the number.

# Code
```python3 []
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_arr = list(str(num))
        num_s = 0
        for i in range(len(num_arr)):
            if num_arr[i] != "9":
                num_s = num_arr[i]
                break
        for i in range(len(num_arr)):
            if num_arr[i] == num_s:
                num_arr[i] = "9"

        max_num = int("".join(num_arr))
        num_arr = list(str(num))
        num_s = num_arr[0]
        for j in range(len(num_arr)):
            if num_arr[j] == num_s:
                num_arr[j] = "0"

        min_num = int("".join(num_arr))
        return max_num - min_num
