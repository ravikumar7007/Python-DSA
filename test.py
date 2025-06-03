from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0
        res = [1] * n
        # Forward pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                res[i] = res[i - 1] + 1
        # Backward pass
        total = res[-1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1] and res[i] <= res[i + 1]:
                res[i] = res[i + 1] + 1
            total += res[i]
        return total


if __name__ == "__main__":
    ratings = [1, 2, 87, 87, 87, 2, 1]
    solution = Solution()
    print(solution.candy(ratings))  # Output: 13
    ratings = [1, 0, 2]
    solution = Solution()
    print(solution.candy(ratings))  # Output: 5
    ratings = [1, 2, 2]
    print(solution.candy(ratings))  # Output: 4
    ratings = [1, 3, 2, 2, 1]
    print(solution.candy(ratings))  # Output: 9
