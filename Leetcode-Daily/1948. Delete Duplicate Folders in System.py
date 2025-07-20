from typing import List, Dict


class TrieNode:
    def __init__(self, folder: str):
        self.folder = folder
        self.remove = False
        self.children: Dict[str, TrieNode] = {}

    def add_child(self, folder: str) -> "TrieNode":
        if folder not in self.children:
            self.children[folder] = TrieNode(folder)
        return self.children[folder]


class Solution:
    def insert_path(self, root: TrieNode, path: List[str]) -> None:
        node = root
        for folder in path:
            node = node.add_child(folder)

    def mark_repeating_subfolders(
        self, node: TrieNode, visited: Dict[str, TrieNode]
    ) -> str:
        subfolders_repr = ""
        for child in node.children.values():
            subfolders_repr += self.mark_repeating_subfolders(child, visited)

        if subfolders_repr:
            if subfolders_repr in visited:
                visited[subfolders_repr].remove = True
                node.remove = True
            else:
                visited[subfolders_repr] = node

        return f"[{node.folder}{subfolders_repr}]"

    def collect_paths(
        self, node: TrieNode, current_path: List[str], result: List[List[str]]
    ) -> None:
        if node.remove:
            return

        current_path.append(node.folder)
        result.append(current_path.copy())

        for child in node.children.values():
            self.collect_paths(child, current_path, result)

        current_path.pop()

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode("/")
        for path in paths:
            self.insert_path(root, path)

        visited: Dict[str, TrieNode] = {}
        self.mark_repeating_subfolders(root, visited)

        result: List[List[str]] = []
        for child in root.children.values():
            self.collect_paths(child, [], result)

        return result


if __name__ == "__main__":
    sol = Solution()
    paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
    print(sol.deleteDuplicateFolder(paths))
    paths = [
        ["a"],
        ["c"],
        ["a", "b"],
        ["c", "b"],
        ["a", "b", "x"],
        ["a", "b", "x", "y"],
        ["w"],
        ["w", "y"],
    ]
    print(sol.deleteDuplicateFolder(paths))
    paths = [["a", "b"], ["c", "d"], ["c"], ["a"]]
    print(sol.deleteDuplicateFolder(paths))
