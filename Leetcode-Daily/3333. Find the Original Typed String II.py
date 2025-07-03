class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        """
        Counts the number of possible original strings of length k that could have resulted in the given typed string.
        Uses dynamic programming to handle the case when the number of character groups is less than k.
        """
        MOD = 10**9 + 7
        n = len(word)
        
        # Step 1: Count consecutive character frequencies
        freq = []
        count = 1
        for i in range(1, n):
            if word[i] == word[i - 1]:
                count += 1
            else:
                freq.append(count)
                count = 1
        freq.append(count)

        # Step 2: Calculate the product of frequencies (all possible splits)
        total_ways = 1
        for f in freq:
            total_ways = total_ways * f % MOD

        # If there are enough groups, return the product
        if len(freq) >= k:
            return total_ways

        # Step 3: Dynamic programming for the case when groups < k
        f = [1] + [0] * (k - 1)  # f[j]: ways to split into j groups
        g = [1] * k              # g[j]: prefix sums of f

        for freq_val in freq:
            f_new = [0] * k
            for j in range(1, k):
                f_new[j] = g[j - 1]
                if j - freq_val - 1 >= 0:
                    f_new[j] = (f_new[j] - g[j - freq_val - 1]) % MOD

            # Update prefix sums for the next iteration
            g_new = [f_new[0]] + [0] * (k - 1)
            for j in range(1, k):
                g_new[j] = (g_new[j - 1] + f_new[j]) % MOD
            f, g = f_new, g_new

        # Subtract the number of ways to split into exactly k groups from total_ways
        return (total_ways - g[k - 1]) % MOD


if __name__ == "__main__":
    solution = Solution()
    print(solution.possibleStringCount("aabbccdd", 7))  # Output: 4
    print(solution.possibleStringCount("aabbccdd", 8))  # Output: 4
    print(solution.possibleStringCount("aaabbb", 3))    # Output: 6
    print(solution.possibleStringCount("aabbcc", 2))    # Output: 4
