class Solution(object):
    mod = 10**9 + 7

    def __init__(self):
        self.state_mem = [[-1] * 1024 for _ in range(1002)]

    def colorTheGrid(self, m, n):
        return self.countways(m, n, 0, 0, 0, 0)

    def countways(self, m, n, r, c, curr, prev):
        if c == n:
            return 1
        if r == m:
            return self.countways(m, n, 0, c + 1, 0, curr)
        if r == 0 and self.state_mem[c][prev] != -1:
            return self.state_mem[c][prev]

        up_color = curr & 3 if r > 0 else 0

        shift = 2 * (m - r - 1)

        left_color = (prev >> shift) & 3

        ways_to_color = 0

        for color in range(1, 4):
            if color != up_color and color != left_color:
                new_state = curr << 2 | color
                ways_to_color = (
                    ways_to_color + self.countways(m, n, r + 1, c, new_state, prev)
                ) % self.mod

        if r == 0:
            self.state_mem[c][prev] = ways_to_color
        return ways_to_color


# Example usage
if __name__ == "__main__":
    sol = Solution()
    m = 5
    n = 5
    result = sol.colorTheGrid(m, n)
    print(f"The number of ways to color the grid is: {result}")
