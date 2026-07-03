from .node import Node
class SuffixTrie:

    def __init__(self) -> None:
        """
        Initialize an empty suffix trie.

        The trie stores all suffixes of a sequence starting from a root node.
        The root node itself does not store occurrence metadata.

        Output:
            Creates a SuffixTrie object with a root node.

        Time Complexity:
            O(1), excluding the fixed-size Node initialization.

        Space Complexity:
            O(1), excluding the fixed-size Node initialization.
        """
        
        self.root = Node() # root doesnt save anything at all 

    def insert(self, source_index, word):
        
        """
        Insert the suffix beginning at source_index into the suffix trie.

        The function traverses the suffix word[source_index:] character by
        character. For each non-terminal character, it follows an existing
        child link or creates a new node if the path does not yet exist.

        Each visited non-root node stores one metadata tuple:

            (character, source_index, end_index)

        where source_index is the starting index of the suffix and end_index
        is computed using the current traversal counter.

        Input:
            source_index:
                Starting index of the suffix being inserted.
            word:
                Full sequence with the terminal symbol "$" appended.

        Output:
            Updates the suffix trie by inserting the suffix from source_index
            to the end of word.

        Time Complexity:
            O(N), where N is the length of the suffix being inserted.

        Space Complexity:
            O(N) in the worst case when new nodes are created for the suffix.

        Note:
            Across the full trie construction, metadata storage is bounded by
            O(N^2), because each inserted suffix contributes one tuple per
            visited non-root node.
        """

        # this counter is used to keep track of how far in the suffix currently is
        counter = 0 

        # begin from the root
        current = self.root

        # go through the key one by one 
        # do it by list slicing 
        # This part will go through the word from 0 -> N, 1 -> N, 2 -> N, 3 -> N, ... N -> N
        # where N is the length of the word
        # hence contributing to the O(N) time complexity
        for char in word[source_index:]:

            # calculate index 
            # convert ascii to index 
            # $ = 0, A = 1, B = 2, C = 3, ... D = 4
            # since the ASCII value for A is 65, substraction of 65 will give the index of A
            # the addtion of 1 is to shift the index by 1, so that $ = 0, A = 1, B = 2, C = 3, D = 4    

            # incrementing counter by 1 for each chatracter in the word
            counter += 1 
            
            # if the still not at the terminal character $
            if char != "$":
                index = ord(char) - 65 + 1

                # if path exists
                if current.link[index] is not None:

                    # move to the next node
                    current = current.link[index]

                    # create a tuple with the character, source_index
                    # combine the character, source index and source_index+counter into a tuple                    
                    current_tuple = (char, source_index, source_index + counter)

                    # append the tuple to the children_tuple list of the current Node
                    # this is where the tuples are stored in all non-root/leaf nodes
                    # the number of tuples stored across the trie will be in the form of (N(N+1)/2)
                    current.children_tuple.append(current_tuple)
                    
                    #print(current_tuple)

                # if path doesn't exist 
                else:

                    #create a new node at the current position
                    current.link[index] = Node()

                    # move to the next node
                    current = current.link[index]

                    # create a tuple with the character, source index 
                    # combine the character, source index and source_index+counter into a tuple                    
                    current_tuple = (char, source_index, source_index + counter)

                    # append the tuple to the children_tuple list of the current Node
                    # this is where the tuples are stored in all non-root/leaf nodes
                    # the number of tuples stored across the trie will be in the form of (N(N+1)/2)
                    current.children_tuple.append(current_tuple)
                    
                    #print(current_tuple)

            # if have reached the terminal $
            if char == "$":  
            
                # go through the terminal $, index = 0 
                index = 0

                if current.link[index] is not None:
                    current = current.link[index]

                    # if path does'nt exist 
                else:
                    #create a new node at the current position 
                    current.link[index] = Node()
                    current = current.link[index]  

    def search(self, key):
        """
        Search for a key in the suffix trie.

        The function follows the trie path corresponding to the characters
        in key. If the path exists, it returns the metadata stored at the
        final node of the path. If the path does not exist, it returns an
        empty list.

        Input:
            key:
                Substring pattern to search for in the suffix trie.

        Output:
            The children_tuple stored at the final node of the search path,
            or an empty list if the key is not found.

        Time Complexity:
            O(M), where M is the length of key.

        Space Complexity:
            O(1), since no additional data structures are created.
        """

        # begin from the root
        current = self.root

        # go through the key one by one 
        for char in key:

            # calculate index 
            # convert ascii to index 
            # $ = 0, A = 1, B = 2, C = 3, D = 4
            index = ord(char) - 65 + 1

            # print(char)
            # if path exists
            # jump from node to its child node according to the index of the character 
            if current.link[index] is not None:
                current = current.link[index]

            # if path doesn't exist
            # hence no retireval of the key in the trie, no information is stored in the trie regading this key
            else:
                return []
        
        # return the children_tuple attribute store inside the last node of the given key
        # this attribute store the character, source index and end index (source_index+counter) of the suffix
        return current.children_tuple
        