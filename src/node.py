class Node:

    """
    <<< The following is the explanation of the time and space complexity of saving the tuples in all non-root nodes>>>

    To build a suffix trie and store child node information efficiently, we use a `current_tuple` to keep track of each node's children, 
    avoiding the need to traverse from the root to the leaves to retrieve information. The `current_tuple` consists of three elements: 
    the character, the source index of the suffix, and a combination of the source index and the counter (the end index). This tuple is appended to the 
    `children_tuple` of the current node. Every node, except the root and leaf nodes, will have at least one tuple in its `children_tuple`, 
    because every non-root/leaf node branches out to at least one suffix. 

    For simplicity, the root node does not store any tuples. For example, with the genome sequence "AAABBBCCC", the root node has three children 
    (A, B, and C), and the A node stores three tuples in its `children_tuple`, representing three suffixes branching from it. Similarly, the B and C 
    nodes each store three tuples. In total, there are 45 tuples across all nodes. In contrast, for the sequence "AAAAAAAAA", the trie is simpler, 
    with the root node having one child (A), and the A node storing 9 tuples, as it branches out 9 times for nine suffixes. Despite structural differences, 
    both tries store 45 tuples. The sum of tuples in the children nodes of the root always equals the genome sequence length, ensuring the total  
    of tuples is (N(N+1)/2), where (N) is the length. For both sequences of length 10(9 from the sequence itself + 1 for terminal $), the total tuples are 
    (10(11)/2 = 55). The reason why the tuples calculated has a total of 45 rather than 55 is because we dont store anything in the root node, not even the
    children_tuple. Hence deducting the number of tuples that the root node will store, which is 10 (also can generalize as N), the total number of tuples store
    will have 45. By not storing information in the root node, we can reduce the space complexity of the trie. but it is still bounded by O(N^2).

    So we can see that the time complexity contributed by storing all the tuples across the trie will be in the form of (N(N+1)/2), by 
    big-O we can see it as O(N^2). Likewise, we can also see that the space complexity contributed by storing all the tuples across the trie
    will also be in the form of (N(N+1)/2), by big-O we can see it as O(N^2).

    <<<This explanation might appear in other functions' description due to the overlapping nature of storing information across the trie>>>
    <<<but its complexity should only be accounted for once in the entire program>>>

    """
    def __init__(self,  size = 5):
        """
        Function description: 

        This is the init function of the class Node. It initializes a Node object which are used as the members of 
        the Trie class.

        Input: 
        
        A character (char) which will be one of the [A,B,C,D and $], and a size (size) which is set to 5 by default.
        The size is the number of children that a node can have. The size is set to 5 because there are 5 possible children,
        which are [A,B,C,D and $]. $ is the terminal character.

        Output, return or postcondition: 
        
        A Node object will be created, with self.link as a list of size 5, and self.children_tuple as an empty list.

        Time complexity: O(N)

        Time complexity analysis: 
        
        O(N) where N is the size of the unique characters in the input string. Which is [A,B,C,D and $]
        Initialization of the list of size 5 is O(N) where N is the size of the unique characters in the input string.
    
        Space complexity: O(N)

        Space complexity analysis: 

        O(N) space complexity occurs when a Node object is created. Because self.link of the Node object is a list of size N.
        Hence requiring O(N) space complexity.
        """

        # terminal $ is at index 0, index 1 to index 4 is A...D
        # when the Node object is first created, the link of size N is set to all None
    
        self.link = [None] * size

        # data payload
        # children_tuple is empty when the Node object is first created
        self.children_tuple = []