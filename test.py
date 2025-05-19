from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = sorted(nums)
        if a + b <= c:
            return "none"
        s = set(nums)
        if len(s) == 1:
            return "equilateral"
        elif len(s) == 2:
            return "isosceles"
        else:
            return "scalene"


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, 5]
    print(s.triangleType(nums))  # Output: scalene
    nums = [2, 2, 2]
    print(s.triangleType(nums))  # Output: equilateral
    nums = [2, 2, 3]
    print(s.triangleType(nums))  # Output: isosceles
    nums = [1, 2, 3]
    print(s.triangleType(nums))  # Output: none
