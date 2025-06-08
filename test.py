from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1

        for _ in range(n):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            else:
                while curr % 10 == 9 or curr + 1 > n:
                    curr //= 10
                curr += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    n = 13
    print(sol.lexicalOrder(n))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 20
    print(
        sol.lexicalOrder(n)
    )  # Output: [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]
