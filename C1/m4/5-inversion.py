def merge(A, B):
    c = [0] * (len(A) + len(B))
    i, j = 0, 0
    inv_count = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c[i + j] = A[i]
            i += 1
        else:
            c[i + j] = B[j]
            inv_count += len(A) - i  # Count inversions
            j += 1

    while i < len(A):
        c[i + j] = A[i]
        i += 1

    while j < len(B):
        c[i + j] = B[j]
        j += 1

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


# Example usage
arr = [2, 3, 9, 2, 9]
result = count_inversions(arr)
print(result)  # Output: 2
