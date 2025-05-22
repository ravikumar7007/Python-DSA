from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # Check if first row needs to be zeroed
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break

        # Check if first column needs to be zeroed
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        # Use first row and column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set cells to zero based on markers in first row/column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


# Example usage
if __name__ == "__main__":
    matrix = [[1, 0, 3]]
    Solution().setZeroes(matrix)
    print(matrix)
