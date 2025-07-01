class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Counts the number of possible original strings based on consecutive repeated characters.
        For each consecutive repeated character, increment the result by 1.
        """

        possible_count = 1  # At least one possible original string
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                possible_count += 1
        return possible_count


if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleStringCount("abbcccc"))  # Output: 4
    print(solution.possibleStringCount("abcabc"))  # Output: 4
