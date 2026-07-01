class Node:
    """A node in a suffix trie.

    Each node stores links to child nodes for supported characters and
    metadata for suffix occurrences that pass through the node.
    """

    def __init__(self, size: int = 5):
        self.link = [None] * size
        self.children_tuple = []