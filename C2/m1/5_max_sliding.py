from collections import deque


def max_sliding_window(nums, m):
    n = len(nums)
    if m == 0:
        return []
    result = []
    dq = deque()

    for i in range(n):
        while dq and dq[0] < i - m + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)

        if i >= m - 1:
            result.append(nums[dq[0]])
    return result


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    result = max_sliding_window(nums, m)
    print(" ".join(map(str, result)))  # Expected output: 3 3 5 5 6
