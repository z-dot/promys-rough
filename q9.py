from typing import Optional, List, Tuple, Set, Union

class Node:
    MAX_DEPTH = 15
    all_grids = set()

    def __init__(self, trees: Union[set, frozenset] = {(0,0),}, depth=0, parent=None):
        self.parent = parent
        self.depth = depth
        self.trees = frozenset(trees)
        if self.depth != Node.MAX_DEPTH and self.trees not in Node.all_grids:
            self.children = self.make_children()
            Node.all_grids.add(self.trees)
        else:
            self.children = []

    def get_options(self) -> List[Tuple[int, int]]:
        output = []
        for tree in self.trees:
            if (tree[0] + 1, tree[1]) not in self.trees and (
                tree[0],
                tree[1] + 1,
            ) not in self.trees:
                output.append(tree)
        return output

    def make_children(self) -> List["Node"]:
        children = []
        for tree in self.get_options():
            temp_set = set(self.trees)
            temp_set.remove(tree)
            temp_set.add((tree[0] + 1, tree[1]))
            temp_set.add((tree[0], tree[1] + 1))
            children.append(Node(temp_set, self.depth + 1, parent=self))
        return children


def count_children(a_node: Node) -> int:
    return len(a_node.children) + sum(
        [count_children(child) for child in a_node.children]
    )


def find_diagonals(a_node: Node, k) -> Optional[Node]:
    for tree in a_node.trees:
        if tree[0] + tree[1] + 1 <= k:
            break
    else:
        return a_node
    for child in a_node.children:
        if (c := find_diagonals(child, k)):
            return c
    return None


if __name__ == "__main__":
    q = Node()
    print(f"Distinct tree grids up to depth {Node.MAX_DEPTH}: {len(Node.all_grids)}")
    for k in range(1, 10):
        print(f"Is there a grid where the first {k} diagonals are empty: {bool(find_diagonals(q, k))}")
    
