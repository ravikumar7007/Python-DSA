class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        hasVowel = False
        hasConsonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    hasVowel = True
                else:
                    hasConsonant = True
            elif not c.isdigit():
                return False
        return hasVowel and hasConsonant


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("234Adas"))  # True
    print(sol.isValid("a3$e"))  # True
    print(sol.isValid("b3"))  # False
    print(sol.isValid("rrdsUE"))  # False
    print(sol.isValid("eB3Aa0e53GAAaE0OB3C3"))  # False
