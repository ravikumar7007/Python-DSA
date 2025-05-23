import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        lenq = len(queries)
        available_query = []
        used_query = []
        queries.sort(key=lambda x: x[0])
        query_pos = 0
        applied_count = 0
        used_count = 0

        for i in range(n):
            # Add all queries starting at i
            while query_pos < lenq and queries[query_pos][0] == i:
                heapq.heappush(available_query, -queries[query_pos][1])
                query_pos += 1

            # Remove expired used queries
            while used_query and used_query[0] == i - 1:
                heapq.heappop(used_query)
                used_count -= 1

            need = nums[i] - used_count

            # Apply available queries to meet the need
            while need > 0 and available_query and -available_query[0] >= i:
                end = -heapq.heappop(available_query)
                heapq.heappush(used_query, end)
                used_count += 1
                applied_count += 1
                need -= 1

            if need > 0:
                return -1

        return lenq - applied_count


# Example usage
if __name__ == "__main__":
    nums = [2, 0, 2]
    queries = [[0, 2], [0, 2], [1, 1]]
    solution = Solution()
    result = solution.maxRemoval(nums, queries)
    print(result)  # Output: [3, 2, 1]
