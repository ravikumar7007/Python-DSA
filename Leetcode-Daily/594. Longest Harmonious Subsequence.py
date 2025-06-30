from collections import Counter
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_length = 0
        for num in count:
            if (num + 1) in count:
                max_length = max(max_length, count[num] + count[num + 1])
        return max_length


if __name__ == "__main__":
    solution = Solution()
    result = solution.findLHS([1, 3, 2, 2, 5, 4, 3, 3])
    print(result)  # Expected output: 5 (the longest harmonious subsequence is [3, 2, 2, 3])