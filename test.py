import re
from typing import List


# Constraints:
# 1 <= num <= 10^8
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


if __name__ == "__main__":
    solution = Solution()
    print(solution.minMaxDifference(11891))
    print(solution.minMaxDifference(90))  # Example usage
    print(solution.minMaxDifference(123456789))  # Example usage
    print(solution.minMaxDifference(10000000))  # Another example
    print(solution.minMaxDifference(987654321))  # Edge case
    print(solution.minMaxDifference(0))  # Edge case
    print(solution.minMaxDifference(9))  # Edge case
