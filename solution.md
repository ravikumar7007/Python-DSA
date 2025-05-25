# Title
Find Indices of Words Containing a Given Character

# Tags
Array, String, List Comprehension, Python

# Intuition
The problem asks for the indices of all words in a list that contain a specific character. My first thought was to iterate through the list, check if the character exists in each word, and collect the indices where it does.

# Approach
Iterate through the list of words using their indices. For each word, check if the given character is present. If it is, append the index to the result list. This can be efficiently done using a list comprehension with `enumerate` for cleaner code.

# Complexity
- Time complexity:  
  $$O(n \cdot m)$$, where \( n \) is the number of words and \( m \) is the average length of each word (since `in` checks each character in the word).

- Space complexity:  
  $$O(k)$$, where \( k \) is the number of words containing the character (for the result list).