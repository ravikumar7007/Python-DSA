from typing import List


class Solution:
    def dfs(
        self,
        curr: int,
        graph: List[List[int]],
        colors: str,
        longest_path: List[List[int]],
        visited: List[int],
    ) -> int:
        if visited[curr] == 1:
            return float("inf")
        if visited[curr] == 0:
            visited[curr] = 1
            for val in graph[curr]:
                res = self.dfs(val, graph, colors, longest_path, visited)
                if res == float("inf"):
                    return float("inf")

                for i in range(26):
                    longest_path[i][curr] = max(
                        longest_path[i][curr], longest_path[i][val]
                    )
            # order of 'a' is 97 in ASCII
            longest_path[ord(colors[curr]) - 97][curr] += 1

            visited[curr] = 2
        return longest_path[ord(colors[curr]) - 97][curr]

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])

        longest_path = [[0] * n for _ in range(26)]
        max_color_len = 0
        visited = [0] * n

        for i in range(n):
            res = self.dfs(i, graph, colors, longest_path, visited)
            if res == float("inf"):
                return -1
            max_color_len = max(max_color_len, res)
        return max_color_len


if __name__ == "__main__":
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    solution = Solution()
    result = solution.largestPathValue(colors, edges)
    print(result)  # Expected output: 3
