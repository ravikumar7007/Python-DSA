def searchMatrix(matrix, target: int) -> bool:
    l = 0
    n = len(matrix[0])
    r = len(matrix) * n - 1
    while l <= r:
        mid = (l + r) // 2
        x = mid // n
        y = mid % n
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            r = mid - 1
        else:
            l = mid + 1
    return False


# Example usage
matrix = [[1, 1]]
print(searchMatrix(matrix, 2))  # Output: True
