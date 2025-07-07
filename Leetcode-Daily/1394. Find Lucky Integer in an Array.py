from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """
        Finds the largest lucky integer in the array.
        A lucky integer is one whose value is equal to its frequency in the array.
        Returns the largest lucky integer, or -1 if none exists.
        """
        freq = Counter(arr)
        lucky_numbers = [num for num, count in freq.items() if num == count]
        return max(lucky_numbers) if lucky_numbers else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.findLucky([2, 2, 3, 4]))  # Output: 2
    print(solution.findLucky([1, 2, 2, 3, 3, 3]))  # Output: 3
    print(solution.findLucky([2, 2, 2, 3, 3]))  # Output: -1
