def sumOfTwoNumbers(a: int, b: int) -> int:
    """
    This function takes two integers a and b, and returns their sum.

    :param a: First integer
    :param b: Second integer
    :return: Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    # Example usage
    arr = input().split()
    a = int(arr[0])
    b = int(arr[1])
    print(sumOfTwoNumbers(a, b))
