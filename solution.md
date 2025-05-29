# Title
Difference Between Sum of Numbers and Twice the Sum of Multiples

# Tags
math, arithmetic progression, python, algorithm, constant time

# Intuition

To find the difference between the sum of all numbers from 1 to n and twice the sum of all multiples of m up to n, we can use mathematical formulas instead of iterating through each number.

# Approach

- Calculate the sum of all numbers from 1 to n using the arithmetic progression formula: `n * (n + 1) // 2`.
- Calculate the sum of all multiples of m up to n using the formula for the sum of the first k natural numbers, where k is the number of multiples: `m * count * (count + 1) // 2`, with `count = n // m`.
- Return the difference: total sum minus twice the multiples sum.

# Complexity

- Time complexity:  
  $$O(1)$$ (All calculations are done in constant time using formulas.)

- Space complexity:  
  $$O(1)$$ (Only a constant amount of extra space is used.)

# Code

```python3 []
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        total_sum = n * (n + 1) // 2
        # Sum of multiples of m up to n using arithmetic progression formula
        count = n // m
        multiples_sum = m * count * (count + 1) // 2
        return total_sum - 2 * multiples_sum
```