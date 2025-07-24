class Solution:
    def getMaxScore(
        self,
        s: str,
        first_char: str,
        second_char: str,
        first_score: int,
        second_score: int,
    ) -> int:
        """
        Calculate maximum score by greedily removing character pairs.

        Args:
            s (str): Input string
            first_char (str): First character to prioritize ('a' or 'b')
            second_char (str): Second character ('b' or 'a')
            first_score (int): Score for removing first_char + second_char pair
            second_score (int): Score for removing second_char + first_char pair

        Returns:
            int: Maximum score achievable
        """
        first_char_count = 0
        second_char_count = 0
        total_score = 0

        # Add terminator to process remaining characters at the end
        s += "c"

        for current_char in s:
            if current_char == first_char:
                first_char_count += 1

            elif current_char == second_char:
                if first_char_count == 0:
                    # No first_char available to pair with, so count second_char
                    second_char_count += 1
                else:
                    # Pair with available first_char for higher score
                    total_score += first_score
                    first_char_count -= 1

            else:
                # Non-target character encountered, process remaining pairs
                total_score += second_score * min(first_char_count, second_char_count)
                first_char_count = 0
                second_char_count = 0

        return total_score

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Find maximum score by removing 'ab' and 'ba' substrings optimally.

        Args:
            s (str): Input string containing 'a' and 'b' characters
            x (int): Points for removing 'ab' substring
            y (int): Points for removing 'ba' substring

        Returns:
            int: Maximum possible score
        """
        # Prioritize the higher scoring pair first for greedy optimization
        if x >= y:
            # Remove 'ab' pairs first (higher priority), then 'ba' pairs
            return self.getMaxScore(s, "a", "b", x, y)
        else:
            # Remove 'ba' pairs first (higher priority), then 'ab' pairs
            return self.getMaxScore(s, "b", "a", y, x)


if __name__ == "__main__":
    sol = Solution()

    # Test cases with expected outputs
    print(sol.maximumGain("cdbcbbaaabab", 4, 5))  # Expected: 19
    print(sol.maximumGain("aabbaaxybbaabb", 5, 4))  # Expected: 20
    print(sol.maximumGain("aabba", 5, 4))  # Expected: 9
    print(sol.maximumGain("aababbab", 2, 3))  # Expected: 7
