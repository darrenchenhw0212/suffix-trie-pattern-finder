from .suffix_trie import SuffixTrie
class PatternFinder:
    """
    Finds substrings that begin with a specified prefix and end with a
    specified suffix using a suffix trie.

    The input sequence is preprocessed into a suffix trie during
    initialization, allowing repeated pattern queries to be performed
    efficiently.
    """
    
    def __init__(self, genome):
        """
        Initialize a PatternFinder object.

        The input sequence is first appended with the terminal character '$'
        before constructing a suffix trie. Every suffix of the sequence is
        inserted into the trie, allowing subsequent pattern searches to be
        performed efficiently.

        Input:
            genome:
                Input sequence to be indexed.

        Output:
            Creates a PatternFinder object containing:
            - genome_with_terminal: the input sequence appended with '$'.
            - genome: a suffix trie built from every suffix of the sequence.

        Time Complexity:
            O(N²)

        Time Complexity Analysis:
            Building the suffix trie requires inserting N suffixes. Since each
            insertion takes O(N) in the worst case, trie construction requires
            O(N²) time.

            During construction, occurrence metadata is stored at every visited
            non-root node. The total number of stored tuples is bounded by
            O(N²), so the overall construction time remains O(N²).

        Space Complexity:
            O(N²)

        Space Complexity Analysis:
            The suffix trie may contain O(N²) nodes in the worst case, and the
            metadata stored across all non-root nodes is also bounded by O(N²).
            Therefore, the total space required is O(N²).
        """
        # Append the terminal symbol to simplify suffix insertion.
        self.genome_with_terminal = genome + "$"

        # Build the suffix trie used for pattern searching.
        self.genome = SuffixTrie()

        # Insert every suffix into the trie.
        for i in range(len(self.genome_with_terminal)):
            self.genome.insert(i, self.genome_with_terminal)
            
    def find(self, start, end):
        """
        Find all substrings that begin with a given prefix and end with a given
        suffix without overlapping.

        The function performs two suffix trie searches:
            1. Locate all occurrences of the start substring.
            2. Locate all occurrences of the end substring.

        Each search returns the metadata (children_tuple) stored at the terminal
        node of the search path. Every metadata tuple has the form:

            (character, source_index, end_index)

        where:
            - character: character stored at the current node.
            - source_index: starting index of the matched substring.
            - end_index: ending index (exclusive) of the matched substring.

        Every occurrence of the start substring is compared against every
        occurrence of the end substring. A valid substring satisfies:

            start_end_index - 1 < end_start_index

        This guarantees that the start and end substrings do not overlap.
        Whenever the condition holds, the corresponding substring is extracted
        from the original sequence and added to the output.

        Input:
            start:
                Prefix of the desired substring.

            end:
                Suffix of the desired substring.

        Output:
            A list of substrings that:
                - begin with start,
                - end with end,
                - and satisfy the non-overlapping constraint.

            Returns an empty list if either pattern does not exist or no valid
            substring can be formed.

        Time Complexity:

            Successful search:
                O(|start| + |end| + N³)

                where:
                - O(|start|) searches for the prefix.
                - O(|end|) searches for the suffix.
                - O(N³) is the worst-case cost of comparing all candidate
                occurrences and constructing the output substrings.

            Unsuccessful search:
                O(|start| + |end|)

        Space Complexity:

            O(N²)

            The output list dominates the additional space usage. In the worst
            case, the number of valid substrings is bounded by O(N²).
        """
        # Store substrings that satisfy the prefix, suffix, and non-overlap constraints.
        # In the worst case, the output can contain O(N²) substrings.
        output = []

        # Retrieve all occurrences of the start substring.
        first_half = self.genome.search(start)

        # Retrieve all occurrences of the end substring.
        second_half = self.genome.search(end)
        
        # No valid substring can be formed if either pattern does not exist.
        if second_half == [] or first_half == []:
            return []
        
        # Compare every occurrence of the start substring with every occurrence
        # of the end substring. A valid substring satisfies:
        #
        #     start_end_index - 1 < end_start_index
        #
        # The nested loop has a worst-case time complexity of O(N²). Since
        # extracting a substring via slicing is O(N), the overall worst-case
        # time complexity of this section is O(N³).
        for i in first_half:
            for j in second_half:
                if i[2] - 1 < j[1]:
                    output.append(self.genome_with_terminal[i[1]:j[2]])
        
        return output
    