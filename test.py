def hammingDistance(s1, s2):
    dis = 0
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            dis += 1
    return dis


def getWordsInLongestSubsequence(words, groups):
    n = len(words)
    dp = [1] * n
    parent = [-1] * n
    ls_end = 0
    ls_len = 1
    for i in range(1, n):
        len_i = len(words[i])
        word_i = words[i]
        gr_i = groups[i]
        for j in range(i):
            if gr_i != groups[j] and dp[i] <= dp[j]:
                if len_i == len(words[j]):
                    if hammingDistance(word_i, words[j]) == 1:
                        dp[i] = dp[j] + 1
                        parent[i] = j
                        if dp[i] > ls_len:
                            ls_len = dp[i]
                            ls_end = i
    res = []
    while ls_end != -1:
        res.insert(0, words[ls_end])
        ls_end = parent[ls_end]
    return res


print(
    getWordsInLongestSubsequence(
        ["abbbb"],
        [1],
    )
)
