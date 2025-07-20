from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Removes subfolders from the given list of folder paths.
        Only top-level folders are kept; subfolders are excluded.
        """
        folder.sort()
        result = [folder[0]]

        for i in range(1, len(folder)):
            parent_folder = result[-1] + "/"
            if not folder[i].startswith(parent_folder):
                result.append(folder[i])

        return result


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])
    )  # ['/a', '/c/d', '/c/f']
    print(solution.removeSubfolders(["/a", "/a/b/c", "/a/b/d"]))  # ['/a']
    print(
        solution.removeSubfolders(["/a/b/c", "/a/b/d", "/a/b/c/e"])
    )  # ['/a/b/c', '/a/b/d']
    print(
        solution.removeSubfolders(["/a/b/c", "/a/b/d", "/a/b/c/e", "/a/b/c/e/f"])
    )  # ['/a/b/c', '/a/b/d']
