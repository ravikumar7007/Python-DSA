def merge(A, B):
    c = []
    i, j = 0, 0
    inv_count = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            inv_count += len(A) - i  # Count inversions
            j += 1

    # Append remaining elements from both subarrays
    c.extend(A[i:])
    c.extend(B[j:])

    return c, inv_count


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, left_inv = merge_sort(arr[:mid])
    right_half, right_inv = merge_sort(arr[mid:])
    merged, split_inv = merge(left_half, right_half)

    return merged, left_inv + right_inv + split_inv


def count_inversions(arr):
    _, inv_count = merge_sort(arr)
    return inv_count


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_inversions(arr))
