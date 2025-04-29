def multiply(A, B, m, n):
    prod = [0] * (m + n - 1)
    # Multiply two polynomials term by term

    # Take ever term of first polynomial
    for i in range(m):
        # Multiply the current term of first
        # polynomial with every term of
        # second polynomial.
        for j in range(n):
            prod[i + j] += A[i] * B[j]

    return prod


# A utility function to print a polynomial
def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end="")
        if i != 0:
            print("x^", i, end="")
        if i != n - 1:
            print(" + ", end="")


# Driver Code

# # The following array represents
# # polynomial 5 + 10x^2 + 6x^3
# A = [5, 0, 10, 6]
# # The following array represents
# # polynomial 1 + 2x + 4x^2
# B = [1, 2, 4]
# m = len(A)
# n = len(B)
# print("First polynomial is ")
# printPoly(A, m)
# print("\nSecond polynomial is ")
# printPoly(B, n)
# prod = multiply(A, B, m, n)
# print("\nProduct polynomial is ")
# printPoly(prod, m + n - 1)


def multiply_poly_divide_and_conquer(A, B):
    def multiply_recursive(A, B):
        m, n = len(A), len(B)
        if m == 1:  # Base case: single coefficient
            return [A[0] * b for b in B]
        if n == 1:  # Base case: single coefficient
            return [B[0] * a for a in A]

        mid_A, mid_B = m // 2, n // 2

        # Divide the polynomials into two halves
        A_low, A_high = A[:mid_A], A[mid_A:]
        B_low, B_high = B[:mid_B], B[mid_B:]

        # Recursively calculate the four products
        P1 = multiply_recursive(A_low, B_low)
        P2 = multiply_recursive(A_high, B_high)
        P3 = multiply_recursive([a + b for a, b in zip(A_low, A_high)], 
                                [c + d for c, d in zip(B_low, B_high)])

        # Combine the results
        result = [0] * (m + n - 1)
        for i in range(len(P1)):
            result[i] += P1[i]
        for i in range(len(P2)):
            result[i + m] += P2[i]
        for i in range(len(P3)):
            result[i + mid_A] += P3[i] - P1[i] - P2[i]

        return result

    return multiply_recursive(A, B)


# Example usage
A = [5, 0, 10, 6]  # Polynomial 5 + 10x^2 + 6x^3
B = [1, 2, 4]      # Polynomial 1 + 2x + 4x^2
result = multiply_poly_divide_and_conquer(A, B)
result