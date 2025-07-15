from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        Matches players to trainers such that each player is matched to a trainer with
        at least as much capability. Returns the maximum number of matches possible.
        """
        players.sort()
        trainers.sort()
        matches = 0
        player_idx, trainer_idx = 0, 0

        while player_idx < len(players) and trainer_idx < len(trainers):
            if players[player_idx] <= trainers[trainer_idx]:
                matches += 1
                player_idx += 1
                trainer_idx += 1
            else:
                trainer_idx += 1

        return matches


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 10])
    )  # Expected output: 2
    print(
        solution.matchPlayersAndTrainers([1, 1, 1], [10, 12, 13])
    )  # Expected output: 3
    print(solution.matchPlayersAndTrainers([1, 2, 3], [3, 4]))  # Expected output: 2
    print(solution.matchPlayersAndTrainers([5, 6], [1, 2, 3]))  # Expected output: 0
