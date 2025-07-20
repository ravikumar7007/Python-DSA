from typing import List, Dict


class TrieNode:
    def __init__(self, folder: str):
        self.folder = folder
        self.remove = False
        self.children: Dict[str, TrieNode] = {}


class Solution:
    def insert_path(self, root: TrieNode, path: List[str]) -> None:
        """Insert a folder path into the trie."""
        node = root
        for folder in path:
            if folder not in node.children:
                node.children[folder] = TrieNode(folder)
            node = node.children[folder]

    def serialize(self, node: TrieNode, lookup: Dict[str, List[TrieNode]]) -> str:
        """Serialize the subtree rooted at node and populate lookup for duplicate detection."""
        if not node.children:
            return f"[{node.folder}]"
        subfolders_serial = "".join(
            self.serialize(node.children[child], lookup)
            for child in sorted(node.children.keys())
        )
        serial = f"[{node.folder}{subfolders_serial}]"
        lookup.setdefault(subfolders_serial, []).append(node)
        return serial

    def mark_removals(self, lookup: Dict[str, List[TrieNode]]) -> None:
        """Mark nodes for removal if their subtree serialization appears more than once."""
        for nodes_with_same_serial in lookup.values():
            if len(nodes_with_same_serial) > 1:
                for node in nodes_with_same_serial:
                    node.remove = True

    def collect_paths(
        self, node: TrieNode, path: List[str], result: List[List[str]]
    ) -> None:
        """Collect all valid folder paths from the trie, skipping removed subtrees."""
        for folder, child in node.children.items():
            if not child.remove:
                path.append(folder)
                result.append(path.copy())
                self.collect_paths(child, path, result)
                path.pop()

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        """Main method to delete duplicate folders and return remaining paths."""
        root = TrieNode("")
        for path in paths:
            self.insert_path(root, path)

        lookup: Dict[str, List[TrieNode]] = {}
        self.serialize(root, lookup)
        self.mark_removals(lookup)

        result: List[List[str]] = []
        self.collect_paths(root, [], result)
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
