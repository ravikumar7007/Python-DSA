class Solution:
    def precomputePrefixSum(self, prefixSum_i, prefixSum_j, s, n, i, j):
        prefixSum_i[0] = prefixSum_j[0] = 0
        # Use local variables for faster access
        pi, pj = prefixSum_i, prefixSum_j
        for idx in range(n):
            digit = int(s[idx])
            pi[idx + 1] = pi[idx] + (digit == i)
            pj[idx + 1] = pj[idx] + (digit == j)

    def calculateDifference(self, s: str, k: int, i: int, j: int) -> int:
        n = len(s)
        prefixSum_i = [0] * (n + 1)
        prefixSum_j = [0] * (n + 1)
        self.precomputePrefixSum(prefixSum_i, prefixSum_j, s, n, i, j)

        minVal = [float("inf")] * 4
        minidx = [-1] * 4
        minVal[0] = minidx[0] = 0

        maxDiff = float("-inf")
        pi, pj = prefixSum_i, prefixSum_j  # Localize for speed
        for end in range(k, n + 1):
            parityI = pi[end] & 1
            parityJ = pj[end] & 1
            parity = ((parityI ^ 1) << 1) + parityJ

            if minVal[parity] != float("inf"):
                if pj[minidx[parity]] != pj[end]:
                    maxDiff = max(maxDiff, pi[end] - pj[end] - minVal[parity])

            # Slide window to right
            start = end - k + 1
            parityI = pi[start] & 1
            parityJ = pj[start] & 1
            parity = (parityI << 1) + parityJ
            startDiff = pi[start] - pj[start]

            if startDiff < minVal[parity]:
                minVal[parity] = startDiff
                minidx[parity] = start

        return maxDiff

    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        maxDiff = -2 * n
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                diff = self.calculateDifference(s, k, i, j)
                maxDiff = max(maxDiff, diff)
        return maxDiff if maxDiff != float("-inf") else 0


# # Constraints:

# 3 <= s.length <= 3 * 104
# s consists only of digits '0' to '4'.
# The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.
# 1 <= k <= s.length

if __name__ == "__main__":
    s = "12233"
    k = 4
    solution = Solution()
    result = solution.maxDifference(s, k)
    print(f"Maximum difference: {result}")
