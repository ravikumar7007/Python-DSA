# def lengthAfterTransformations(s: str, t: int, nums) -> int:
#     MOD = 10**9 + 7
#     freq = [0] * 26
#     for ch in s:
#         freq[ord(ch) - ord("a")] += 1

#     for _ in range(t):
#         new_freq = [0] * 26
#         for i in range(26):
#             if freq[i] == 0:
#                 continue
#             for j in range(i + 1, i + nums[i] + 1):
#                 new_freq[j % 26] += freq[i]

#         freq = new_freq

#     return sum(freq) % MOD


# def myPow(x: float, n: int) -> float:
#     res = 1
#     if n < 0:
#         x = 1 / x
#         n = -n
#     while n > 0:
#         if n % 2 == 1:
#             res *= x
#         x = x * x
#         n = n // 2
#     return res


# print(myPow(2.00000, -2))  # Output: 1024.00000

MOD = 10**9 + 7


def getTransformations(nums):
    res = [[0] * 26 for _ in range(26)]
    for i in range(26):
        for j in range(i + 1, i + nums[i] + 1):
            res[i][j % 26] += 1
    return res


def matrix_multiply(A, B, m):
    res = [[0] * 26 for _ in range(26)]
    for i in range(m):
        for k in range(26):
            if A[i][k] != 0:
                for j in range(26):
                    if B[k][j] != 0:
                        res[i][j] = (res[i][j] + A[i][k] * B[k][j]) % MOD
    return res


def lengthAfterTransformations(s: str, t: int, nums):
    freq = [[0] * 26]
    for ch in s:
        freq[0][ord(ch) - ord("a")] += 1
    trans = getTransformations(nums)
    mat_exp = [[0] * 26 for _ in range(26)]
    for i in range(26):
        mat_exp[i][i] = 1
    while t > 0:
        if t % 2 == 1:
            mat_exp = matrix_multiply(mat_exp, trans, 26)
        trans = matrix_multiply(trans, trans, 26)
        t //= 2
    res = matrix_multiply(freq, mat_exp, 1)
    return sum(res[0]) % MOD


print(
    lengthAfterTransformations(
        s="azbk",
        t=1,
        nums=[
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
            2,
        ],
    )
)  # Output: 6
