import random

def maximumPairwiseProduct(arr,n):
    """
    This function takes a list of integers and returns the maximum pairwise product.
    
    :param arr: List of integers
    :return: Maximum pairwise product
    """
    max_product = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    
    return max_product

def maximumPairwiseProductFast(arr,n):
    """
    This function takes a list of integers and returns the maximum pairwise product using a more efficient approach.
    
    :param arr: List of integers
    :return: Maximum pairwise product
    """
    max_index1 = -1
    max_index2=-1

    for i in range(n):
        if max_index1 == -1 or arr[i] > arr[max_index1]:
            max_index2 = max_index1
            max_index1 = i
        elif max_index2 == -1 or arr[i] > arr[max_index2]:
            max_index2 = i
  
    return arr[max_index1] * arr[max_index2]

if __name__ == "__main__":
  n = int(input())
  arr = list(map(int, input().split()))
  print(maximumPairwiseProductFast(arr, n)) 
  # stress test for this program using random numbers in random range
  # while True:
  #   n = random.randint(2, 10000)
  #   arr = [random.randint(2, 10000) for i in range(1, n+1)]
  #   print(n, "/n", arr)
  #   print(maximumPairwiseProductFast(arr, n)) 
  #   print(maximumPairwiseProduct(arr, n))
  #   if maximumPairwiseProductFast(arr, n) == maximumPairwiseProduct(arr, n):
  #     print("Test passed")
  #   else:
  #     print("Test failed")
  #     break
