# Title
Remove Characters Marked by Stars

# Intuition
When encountering a `*` in the string, we need to remove the smallest lexicographical character to its left that hasn't already been removed. My first thought was to keep track of the positions of each character so we can efficiently find and remove the correct one when a `*` is found.

# Approach
- Convert the string to a list for mutability.
- Use an array of stacks (`list_s`) to store the indices of each character (`a` to `z`) as we iterate.
- When a `*` is found, scan from `a` to `z` and pop the most recent index from the first non-empty stack, marking that character as removed.
- After processing, join and return all characters that are not `*`.

# Complexity
- Time complexity:  
  $$O(26n)$$ (for each `*`, in the worst case, we may scan up to 26 stacks, but in practice this is very fast and close to $$O(n)$$)
- Space complexity:  
  $$O(n)$$ (for the stacks and the mutable string list)

# Code
```python3 []
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        s = list(s)
        list_s = [[] for _ in range(26)]
        for i in range(n):
            ch = s[i]
            if ch == "*":
                for j in range(26):
                    if list_s[j]:
                        s[list_s[j].pop()] = "*"
                        break
            else:
                list_s[ord(ch) - 97].append(i)

        return "".join(c for c in s if c != "*")
```