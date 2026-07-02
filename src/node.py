class Node:

    """
    Represents a node in the suffix trie.

    Each node stores:
    - `link`: references to child nodes for the supported characters
      ($, A, B, C, and D).
    - `children_tuple`: metadata describing every suffix that passes
      through this node.

    During trie construction, one tuple is appended to every visited
    non-root node for each inserted suffix. Since suffix lengths are
    N, N-1, ..., 1, the total stored metadata is bounded by O(N²).
    This implementation does not store tuples in the root node,
    reducing the constant factor while preserving the O(N²) space
    complexity.
    """
    
    def __init__(self,  size = 5):
        """
        Initialize a trie node.

        Args:
            size: Number of possible child links.
                  Default is 5 for {$, A, B, C, D}.

        Attributes:
            link: List of child node references.
            children_tuple: Metadata associated with suffixes passing
                            through this node.

        Time Complexity:
            O(size)

        Space Complexity:
            O(size)
        """

        # Terminal '$' occupies index 0, followed by A-D.
    
        self.link = [None] * size

         # Stores metadata for suffixes passing through this node.
        self.children_tuple = []