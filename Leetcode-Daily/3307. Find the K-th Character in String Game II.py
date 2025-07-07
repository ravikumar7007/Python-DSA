import math
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        count_ops = 0
        val = k

        while val > 1:
            jumps = math.ceil(math.log2(val))
            val -= pow(2, jumps - 1)
            count_ops += operations[jumps - 1]

        return chr(ord("a") + (count_ops % 26))


if __name__ == "__main__":
    solution = Solution()
    print(solution.kthCharacter(k=10, operations=[0, 1, 0, 1]))  # Example usage
    print(solution.kthCharacter(k=5, operations=[0, 0, 0]))  # Example usage
    print(solution.kthCharacter(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Example usage
