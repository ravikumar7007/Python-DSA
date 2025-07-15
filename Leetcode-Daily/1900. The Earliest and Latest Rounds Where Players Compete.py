from functools import lru_cache
from typing import List, Tuple


class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        @lru_cache(None)
        def dp(num_players: int, first: int, second: int) -> Tuple[int, int]:
            # Base case: players meet
            if first + second == num_players + 1:
                return (1, 1)
            # Symmetry: always keep first < second
            if first + second > num_players + 1:
                return dp(num_players, num_players + 1 - second, num_players + 1 - first)

            earliest, latest = float("inf"), float("-inf")
            next_round_players = (num_players + 1) // 2

            # Case 1: both players in the first half
            if second <= next_round_players:
                for i in range(first):
                    for j in range(second - first):
                        e, l = dp(next_round_players, i + 1, i + j + 2)
                        earliest = min(earliest, e)
                        latest = max(latest, l)
            else:
                # Case 2: second player in the second half
                s_prime = num_players + 1 - second
                mid = (num_players - 2 * s_prime + 1) // 2
                for i in range(first):
                    for j in range(s_prime - first):
                        e, l = dp(next_round_players, i + 1, i + j + mid + 2)
                        earliest = min(earliest, e)
                        latest = max(latest, l)

            return (earliest + 1, latest + 1)

        # Ensure firstPlayer < secondPlayer for symmetry
        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer

        earliest, latest = dp(n, firstPlayer, secondPlayer)
        dp.cache_clear()
        return [earliest, latest]


if __name__ == "__main__":
    solution = Solution()
    print(solution.earliestAndLatest(11, 2, 4))  # Expected output: [2, 3]
    print(solution.earliestAndLatest(5, 1, 5))  # Expected output: [3, 4]
    print(solution.earliestAndLatest(4, 1, 2))  # Expected output: [2, 3]
    print(solution.earliestAndLatest(3, 1, 2))  # Expected output: [1, 2]
