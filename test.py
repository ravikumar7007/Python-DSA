from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_even = float("inf")
        map_s = Counter(s)
        for key in map_s:
            val = map_s[key]
            if val % 2 != 0:
                max_odd = max(val, max_odd)
            else:
                min_even = min(val, min_even)

        return max_odd - min_even


if __name__ == "__main__":
    s = "abcabcab"
    solution = Solution()
    print(solution.maxDifference(s))
    # Expected output: Counter({'a': 2, 'b': 2, 'c': 2})
