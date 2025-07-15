class Solution:
    def isValid(self, word: str) -> bool:
        """
        Checks if the word is valid:
        - At least 3 characters long
        - Contains at least one vowel and one consonant
        - Only contains letters and digits
        """
        if len(word) < 3:
            return False

        has_vowel = False
        has_consonant = False
        vowels = set("aeiou")

        for c in word:
            if c.isalpha():
                if c.lower() in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isdigit():
                return False

        return has_vowel and has_consonant


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("234Adas"))  # True
    print(sol.isValid("a3$e"))  # True
    print(sol.isValid("b3"))  # False
    print(sol.isValid("rrdsUE"))  # False
    print(sol.isValid("eB3Aa0e53GAAaE0OB3C3"))  # False
