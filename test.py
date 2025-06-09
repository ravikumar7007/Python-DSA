class Solution:
    def step_count(self, n: int, curr: int, next: int) -> int:
        steps = 0
        while curr <= n:
            steps += min(n + 1, next) - curr
            curr *= 10
            next *= 10
        return steps

    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1  # Adjust k to be zero-indexed

        while k > 0:
            steps = self.step_count(n, curr, curr + 1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr


if __name__ == "__main__":
    sol = Solution()
    n = 13
    k = 2
    print(sol.findKthNumber(n, k))  # Output: 10
    n = 1
    k = 1
    print(sol.findKthNumber(n, k))  # Output: 1
    n = 1000
    k = 10
    print(sol.findKthNumber(n, k))  # Output: 10
