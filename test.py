def lengthAfterTransformations(s: str, t: int) -> int:
    MOD = 10**9 + 7
    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord("a")] += 1

    for _ in range(t):
        new_freq = [0] * 26
        for i in range(25):  # 'a' to 'y'
            new_freq[i + 1] = freq[i]
        # Special case: 'z' → 'a' + 'b'
        new_freq[0] = (new_freq[0] + freq[25]) % MOD
        new_freq[1] = (new_freq[1] + freq[25]) % MOD
        freq = new_freq

    return sum(freq) % MOD



print(lengthAfterTransformations(s="abcyy", t=2))  # Output: 6
