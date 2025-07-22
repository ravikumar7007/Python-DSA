class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        Removes characters from the string so that no three consecutive characters are the same.
        Args:
            s (str): Input string.
        Returns:
            str: Modified string with no three consecutive identical characters.
        """
        result = []
        consecutive_count = 1

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count < 3:
                result.append(s[i])

        return "".join(result)


if __name__ == "__main__":
    sol = Solution()
    print(sol.makeFancyString("leeetcode"))  # Output: "leetcode"
    print(sol.makeFancyString("aaabaaaa"))  # Output: "aabaaa"
    print(sol.makeFancyString("aab"))  # Output: "aab"
    print(sol.makeFancyString("aaa"))  # Output: "aa"
