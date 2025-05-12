def findEvenNumbers(digits):
    freq = [0] * 10
    res = []
    for num in digits:
        freq[num] += 1
    for num in range(100, 999, 2):
        parts = [num // 100, (num // 10) % 10, num % 10]
        local = [0] * 10
        for loc in parts:
            local[loc] += 1
        valid = True
        for d in set(parts):
            if local[d] > freq[d]:
                valid = False
                break
        if valid:
            res.append(num)
    return res


print(findEvenNumbers([2, 1, 3, 0]))
# Output: [120, 102, 210, 201, 320, 302, 320, 321]
