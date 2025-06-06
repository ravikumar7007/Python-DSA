from typing import List


class Solution:
    def smallest_char(self, dic: List[int]) -> str:
        for i in range(26):
            if dic[i] > 0:
                return chr(i + 97)
        return "z"

    def robotWithString(self, s: str) -> str:
        n = len(s)
        dic = [0] * 26
        for c in s:
            dic[ord(c) - 97] += 1

        t = []
        res = []
        pos = 0

        while pos < n:
            t.append(s[pos])
            dic[ord(s[pos]) - 97] -= 1
            smallest = ord(self.smallest_char(dic))
            while t and ord(t[-1]) <= smallest:
                res.append(t.pop())
            pos += 1

        return "".join(res)


if __name__ == "__main__":
    s = "cba"
    print(Solution().robotWithString(s))  # Output: "abc"

    s = "leetcode"
    print(Solution().robotWithString(s))  # Output: "cdelotee"

    s = "aaaabbbbcccc"
    print(Solution().robotWithString(s))  # Output: "aaaabbbbcccc"
