class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_len = n - numFriends + 1
        res = ""
        for i in range(n):
            wor = word[i : (i + max_len) or n]
            if wor > res:
                res = wor
        return res


if __name__ == "__main__":
    s = Solution()
    ans = s.answerString("aann", 2)
    print(ans)
    # Output: # "dbca", "bcad", "cadb", "adbc"
