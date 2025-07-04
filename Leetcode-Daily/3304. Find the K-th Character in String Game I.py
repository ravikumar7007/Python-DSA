class Solution:
    def kthCharacter(self, k: int) -> str:
        """
        Returns the k-th character in the generated string sequence.
        The sequence starts with 'a', and each round appends the next letter (cycling from 'z' to 'a').
        """
        sequence = [1]  # 1 represents 'a'

        while len(sequence) < k:
            next_round = []
            for val in sequence:
                next_val = 1 if val == 26 else val + 1
                next_round.append(next_val)
            sequence.extend(next_round)

        # Convert the k-th value to its corresponding character
        return chr(sequence[k - 1] - 1 + ord("a"))


if __name__ == "__main__":
    solution = Solution()
    k = 10  # Example value for k
    result = solution.kthCharacter(k)
    print(result)  # Output the result
