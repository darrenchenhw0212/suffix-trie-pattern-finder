import bisect

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

class Trie:

    def __init__(self) -> None:
        """
        Function description: 
        
        This is the init function of Trie class. It initializes a Trie object which is used to store the sequence.
        A trie object will only have one attribute, which are the root.

        Output, return or postcondition: Create a Trie object with the root attribute.

        Time complexity: O(N)

        Time complexity analysis: 

        0(N) because a single Node object AKA as the root has been created in this init function. This O(N) is 
        inherited from the Node class init function.|

        Space complexity: O(N)

        Space complexity analysis: 

        0(N) because a single Node object AKA as the root has been created in this init function. This O(N) is 
        inherited from the Node class init function.
        """

        self.root = Node() # root doesnt save anything at all 

    def insert(self, source_index, word):
        """
        Function description: This is the function used to insert a suffix into the suffix trie, by manipulating the indices of the 
        genome sequence (word) given, and inserting the suffix into the trie.

        Approach description (if main function): 

        First create a variable named counter, this counter is used to keep track of how far in the suffix currently is. Then create
        another variable named current, which initially points to the root of the trie. Then for each character in the suffix, do a list 
        slicing from the current starting index from 0 -> N, 1 -> N, 2 -> N, 3 -> N, ... N -> N, where N is the length of the word. 
        Increment the counter by 1. If the character is not the terminal character $, then calculate the index of the character, and if
        current.link[index] is not None, meaning that the path exist, then move to the next node. Following by appending in the current_tuple 
        into the current Node's children_tuple. If the path doesn't exist, then create a new node at the current position. Move to the next Node
        and followed by adding the current_tuple into the children_tuple. If the character is the terminal character $, if the Node exist then 
        move to the node, if not, create a new node at the current position for terminal $.

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
        both tries store 45 tuples. The sum of tuples in the children nodes of the root always equals the genome sequence length, ensuring the total number 
        of tuples is (N(N+1)/2), where (N) is the length. For both sequences of length 10(9 from the sequence itself + 1 for terminal $), the total tuples are 
        (10(11)/2 = 55). The reason why the tuples calculated has a total of 45 rather than 55 is because we dont store anything in the root node, not even the
        children_tuple. Hence deducting the number of tuples that the root node will store, which is 10 (also can generalize as N), the total number of tuples store
        will have 45. By not storing information in the root node, we can reduce the space complexity of the trie. but it is still bounded by O(N^2).

        So we can see that the time complexity contributed by storing all the tuples across the trie will be in the form of (N(N+1)/2), by 
        big-O we can see it as O(N^2). Likewise, we can also see that the space complexity contributed by storing all the tuples across the trie
        will also be in the form of (N(N+1)/2), by big-O we can see it as O(N^2).

        <<<This explanation might appear in other functions' description due to the overlapping nature of storing information across the trie>>>
        <<<but its complexity should only be accounted for once in the entire program>>>
    
        Input: source_index, word, where source_index will be 0 all the way to the length of the word, N and word is the genome sequence.

        Output, return or postcondition: The Trie object now will have the suffix from source_index to the end of the word inserted into the trie.
        for example, genome sequence of AAAA will now have suffixes of A$, AA$, AAA$, AAAA$, $ inserted into the trie.

        Time complexity: 
        
        O(N) from the for loop.

        O(N^2) from storing tuples in all non-root/leaf nodes.

        Time complexity analysis: 

        O(N) is contributed from the for loop. Because the worst case happens when the source_index is 0, meaning that the function will go through
        the word from 0 -> N, 1 -> N, 2 -> N, 3 -> N, ... N -> N, where N is the length of the word. Hence the time complexity is O(N).

        O(N^2) is contributed by storing tuples in all non-root/leaf nodes. The time complexity contributed by storing all the tuples across the 
        trie will be in the form of (N(N+1)/2), by big O, we can see it as O(N^2).

        Space complexity: 
        
        O(N) from creating the suffixes.

        O(N^2) from storing tuples in all non-root/leaf nodes.

        Space complexity analysis: 

        O(N) space complexity is contributed by the creation of the suffix, worst case is when the suffix is exactly the word itself, hence it requires 
        to traverse N times from nodes to nodes to create the suffix. Hence the space complexity is O(N).  

        O(N^2) space complexity is contributed by storing tuples in all non-root/leaf nodes. The space complexity contributed by storing all the tuples, 
        although each tuple has exacly 3 elements, the total number of tuples stored across the trie will be in the form of 3(N(N+1)/2), by big O, 
        we can see it as O(3N^2), then ingoring the constant 3, the space complexity is O(N^2).
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
        Function description: 
        
        This is the function used to search for a suffix in the suffix trie, by manipulating the indices of the genome
        sequence (word) given, and searching for the suffix in the trie.

        Approach description (if main function):

        The approach of this function is similar to what is done in the insert function. The way that this function jump from
        one node to its child node. The only difference is that this function do not modify the trie, it only search for the
        key in the trie, if the given key is indeed a suffix inside the trie, then return the children_tuple attribute store 
        inside the last node of the given key. The function will return an empty list if the key is not found in the trie, hence
        the word is not a suffix of the genome sequence.

        Input: a key, a substring of the genome sequence. for example, the genome sequence "AAABBBCCC", "AAA" is a substring, and "BB" is a substring.

        Output, return or postcondition: 
        
        Return the children_tuple attribute store inside the last node of the given key. If the key is not found in the trie, 
        return an empty list. The children_tuple attribute store the character, the sorce_index and end index of the suffix, it allows us to 
        see what suffixes this current node is branching to without travesing from the root to the leaf, which is inefficient. 

        Time complexity: 

        O(N) where the N is the length of the key.

        Time complexity analysis: 

        O(N) is contributed from the worst case scenario where the key is the entire genome sequence, hence the function will go through
        the root and traverse all the way down to the leaf of this suffix. Hence the time complexity is O(N).

        Space complexity:   0(1) constant space complexity.

        Space complexity analysis: 

        O(1), because the function does not create any new objects, it only returns the children_tuple attribute store inside the last node of the given key.
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
        
class OrfFinder:
    """
    The class OrfFinder is used to find the open reading frame in the genome sequence. I am using a trie to store the genome sequence,
    more specifically a suffix trie. 
    """
    def __init__(self, genome):
        """
        Function description: 
        
        This is the init function of class OrfFinder. It initializes a OrfFinder object which is used to find the open 
        reading frame in the genome sequence. This OrfFinder object will have two attributes, genome_with_terminal and genome. The genome_with_terminal
        is just appending the terminal $ at the end of the ggenome sequence given. While the attribute genome will be modeled as a Trie object, by calling 
        the init function of the Trie class.

        Approach description (if main function): 

        First append the terminal $ at the end of the genome sequence given. Then create a Trie object based on the genome sequence given.
        Then loop for 0 -> N times to insert the suffixes into the trie, where N is the length of the genome sequence. For example, the genome
        sequence is "AAABBBCCC$", the first suffix inserted will be "AAABBBCCC$", the second suffix inserted will be "AABBBCCC$", the third suffix
        will be "ABBBCCC$", and so on. We can see that every time it loops, the source_index will be incremented by 1, until it reaches the end of the
        genome sequence.

        Input: a genome sequence, for example, "AAABBBCCC"

        Output, return or postcondition: 
        
        An OrfFinder object will be created, with the genome_with_terminal attribute and the genome attribute. The main focus will be on the 
        attribute genome, since it is the suffix trie of the genome sequence given.

        Time complexity: 

        1) O(N^2) from building the trie by looping the insert function N times. 

        2) O(N^2) from storing tuples in all non-root/leaf nodes. 

        Final answer: O(N^2) + O(N^2) = O(2N^2), by big-O we can see it as O(N^2).

        Time complexity analysis: 

        1) O(N^2) is contributed by building the trie by looping the insert function N times. From earlier we know the complexity from the insert function 
        will be O(N), now we loop the insert function N times, hence the time complexity is O(N^2).

        2) O(N^2) is contributed by storing tuples in all non-root/leaf nodes. The time complexity contributed by storing all the tuples across the trie, the
        total number of tuples stored across the trie will be in the form of (N(N+1)/2), since the number of tuples stored will be bounded by O(N^2), hence the
        time complexity is O(N^2).

        Final answer: O(N^2) + O(N^2) = O(2N^2), by big-O we can see it as O(N^2).

        Space complexity: 

        1) O(N^2) from building the trie by looping the insert function to insert the suffixes.

        2) O(N^2) from storing tuples in all non-root/leaf nodes.

        Space complexity analysis: 

        1) O(N^2) from building the trie by looping the insert function to insert the suffixes, since the worst case happens when the suffix that is being 
        inserted is the entire genome sequence itself, for instance the genome sequence is "AAABBBCCC" and the suffix that is inserting is "AAABBBCCC$", if 
        all nodes requires by this suffix is not yet created, then the function will create all the nodes required to store this suffix, which it will then go
        through the root and traverse all the way down to the leaf of this suffix, via N nodes. And there exist N suffixes. Hence the space complexity is O(N^2).

        2) O(N^2) is contributed by storing tuples in all non-root/leaf nodes. The space complexity contributed by storing all the tuples across the trie, the
        total number of tuples stored across the trie will be in the form of (N(N+1)/2), since the number of tuples stored will be bounded by O(N^2), hence the
        time complexity is O(N^2).

        Final answer: O(N^2) + O(N^2) = O(2N^2), by big-O we can see it as O(N^2).
        """

        # this is where I append the terminal $ at the end of the genome sequence given
        self.genome_with_terminal = genome + "$"

        # this is where I create a Trie object based on the genome sequence given, assigning it to the attribute genome
        self.genome = Trie()

        # this is where the insert function is called to insert the suffixes into the trie
        # the source_index will be incremented by 1, until it reaches the end of the genome sequence
        for i in range(len(self.genome_with_terminal)):
            self.genome.insert(i, self.genome_with_terminal)  

    def find(self, start, end):
        """
        Function description: 
        
        This find function is used to find the open reading frame in the genome sequence. The function will search for the
        the start and end substring in the genome sequence, and if the start and end substring is found in the genome sequence,
        and they do not overlap, then the function will return the substring between the start and end substring.

        Approach description (if main function): 
        
        This find function will run the search function twice, once for the start substring and once for the end substring. 
        The search function will help to find the start and end substring in the genome sequence. If the start and end substring does 
        exist in the trie, then retrieve the payload of the ending node of each start and end. For example the genome sequence is 
        "AAABBBCCC", and the start substring is "AB" and the end substring is "B". Since the start and end substring exist in the trie,
        by calling search function on "AB", it will traverse following the suffix "AB" is stored. So for instance, the search function will
        traverse following "AB", from root to node A, then to node B, and the payload of node B will be retrieved, namely the children_tuple.
        The same goes for the end, from root to node B, and the payload of node B will be retrieved. Now that we have the payload of the start
        and the end, we can check if the start and end do not overlap, if they do not overlap, then we can return the substring between the start
        and end.

        The information stored in the children_tuple attribute of the node is the the tuple  of (character, source index and end index (source_index+counter)). 
        For instance the children_tuple retrieved by searching for "AB" will have the value of [(B, 2, 4)], only one tuple in the list children_tuple,
        hence we can confrim that at this node, it only lead to one suffix. To interpret the tuple, index[0] is telling us that this node has the 
        value of B, index[1] is telling us that the source index of this suffix is from genome[2], which is the third A of the genome. Lastly the 4 in index[2] 
        is telling us that for this suffix "AB", is ending at genome[4] (not-inclusive). So with the value of source_index being genome[2] and the end_index being genome[4],
        we know the substring "AB" is obtained by printing out the characters of the genome sequence at range[2, 4). Note, the start index is inclusive but 
        the end index is not inclusive, so the index slicing that form substring "AB" will be genome[2] + genome[3]. 
        
        The same goes for the end substring, the children_tuple retrieved by searching "B" will have the value of [(B, 3, 4), (B, 4, 5), (B, 5, 6)]. From this children_tuple list,
        we can see that it has three tuples stored in it, hence we can know that this node is branching out to three suffixes. index[0] is telling us that this node has the B character,
        for (B, 3, 4), index[1] is telling us that the source index of this suffix is from genome[3], which is the first B of the genome. Lastly the 4 in index[2] is telling us that for 
        this suffix "B", is ending at genome[4] (not-inclusive). So with the value of source_index being genome[3] and the end_index being genome[4], we know the substring "B" is obtained by
        printing out the characters of the genome sequence at range[3, 4). Where the substring will be "B". The same goes for the other two tuples, (B, 4, 5) and (B, 5, 6). Where tuple (B, 4, 5)
        will give the substring "B" and tuple (B, 5, 6) will give the substring "B".

        Now that we know the substring of the start and end, we can check if the start and end do not overlap, if they do not overlap, then we can return the substring between the start and the end.
        One important property is that the last last index of start substring must be less than the first index of the end substring. Searching "AB" will have a result of (B, 2, 4), and searching "B" 
        will have a result of [(B, 3, 4), (B, 4, 5), (B, 5, 6)]. Now we have to do is to compare the last index of the start substring(s) with the first index of the end substring(s). Since the end index 
        is not inclusive, then we have to compare the index before the end index of the start substring to the start index of all end substring. In this example, the index before the end index of the start
        substring is 4, 4 - 1 will be 3 so it is telling us the start substring is ending at genome[3], as for the end substring, since it has three tuples, so we have to compare the value 3 to the start index
        of all these three tuples. Hence the value 3 is being compared with value 3, 4 and 5. 

        1) Comparing 3 (end index - 1 for start substring) with 3 (start index of end substring):

            Since 3 < 3 is not True, hence for this combo (3,3), the start and end overlap. Not a valid substring.

        2) Comparing 3 (end index - 1 for start substring) with 4 (start index of end substring):
            
            Since 3 < 4 is True, hence for this combo (3,4), the start and end do not overlap. A valid substring.
        
        3) Comparing 3 (end index - 1 for start substring) with 5 (start index of end substring):
                
            Since 3 < 5 is True, hence for this combo (3,5), the start and end do not overlap. A valid substring.

        Since the tuples stored might be more than one for both start substring and end substring, a double for loops is used to do the comparison.

        So we can see that based on the above three comparison, only two of them are valid, hence the substrings based on these two valid comparison will be returned.
        For instand, 2) will return substring from genome[2](inclusive) to genome[5](exclusive) and 3) will return substring from genome[2](inclusive) to genome[6](exclusive).
        
        Input: non-empty start and end substring of the genome sequence.

        Output, return or postcondition: 
        
        1) if both the start and end exist:
            1a) if the start and end do not overlap, return the substring between the start and end.
            1b) if the start and end overlap, return an empty list.

        2) if either the start or end does not exist:
            2a) return an empty list.

        Time complexity: 

        1) If both the start and end exist:

            >> O(|start|) + O(|end|) + O(N^3) + O(N^2)
            >> O(|start|) + O(|end|) + O(N^3)
        
        2) If either the start or end does not exist:

            >> O(|start) + O(|end|) + O(1)
            >> O(|start) + O(|end|)

        Time complexity analysis: 

         1) If both the start and end exist: 

            Whether the substrings start and end exist or not, we will still require to call the search function twice to validate if both 
            start and end substring exist. Inherited from the time complexity of the search function, O(N) where N is the length of the key
            that is being searched. Hence the timpe complexity for searching the start substring will be O(|start|) where |start| is the length'
            of the start, likewise the time complexity for searching the end substring will be O(|end|) where |end| is the length of the end. 
            But one thing to mention is that for valid substrings, |start| and |end| should be added up to N, where N is the length if the genome.
            hence the time complexity of the search function is O(N), where N is the length of the genome sequence. to match with the assignment 
            specification, I will just conclude that the time complexity for searching start will be O(|start|) and the time complexity for searching
            end will be O(|end|).

            The time complexity for the double for loop is O(N^3), where N is the length of the genome sequence. The worst case time complexity for
            the double for loop is O(N^3) when the genome sequence is only one repeating character, for example genome is "AAAAAAAAA", and the start
            and end are both single "A". hence the chidren_tuple of the start will have 9 tuples, and the children_tuple of the end will have 9 tuples,
            then in this double for loop it will require to run 9 * 9 times, until now the time complexity will be O(N^2). In the double for loop, there
            will be list slicing, which is O(N) time complexity, hence the worst case time complexity is O(N^3) for the double for loop.

            for the output [], the time complexity to build it given when both start and end exist will be in the formula of (N(N+1)/2) - N, where N is the length
            so it is bounded by O(N^2). Hence the time complexity for the output is O(N^2).


            >> O(|start|) + O(|end|) + O(N^3) + O(N^2)
            >> O(|start|) + O(|end|) + O(N^3)
        
        2) If either the start or end does not exist:

            Whether the substrings start and end exist or not, we will still require to call the search function twice to validate if both
            start and end substring exist. Inherited from the time complexity of the search function, O(N) where N is the length of the key
            that is being searched. Hence the timpe complexity for searching the start substring will be O(|start|) where |start| is the length
            of the start, likewise the time complexity for searching the end substring will be O(|end|) where |end| is the length of the end.
            But one thing to mention is that for valid substrings, |start| and |end| should be added up to N, where N is the length if the genome.
            hence the time complexity of the search function is O(N), where N is the length of the genome sequence. to match with the assignment
            specification, I will just conclude that the time complexity for searching start will be O(|start|) and the time complexity for searching
            end will be O(|end|).

            if either of the children_tuple for start and end is an empty list, then the output will be an empty list, hence the time complexity
            will be constant, O(1).

            >> O(1) + O(|start) + O(|end|) 
            >> O(|start) + O(|end|)

        Space complexity: O(N^2) from the output list.

        Space complexity analysis: 

        The space complexity of the output has the worst case of O(N^2). From eariler we have seen that the number of the possible substrings
        will be following the formula of (N(N+1)/2) - N, where N is the length of the genome sequence. Which in other word, this formula is bounded by
        N^2. Hence the space complexity of the output is O(N^2).

        Only the output will contribute to space complexity in this find function. 

        """

        # this is used to store the final substring(s) between the start and end
        # the space complexity of this output has the worst case of O(N^2)
        # for example, the genome sequence is "AAAAAAAAA", and the start and the end are both "A"
        # the output will be['AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAAA', 'AAAAAAA', 'AAAAAAAA', 'AAAAAAAAA', 
        # 'AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAAA', 'AAAAAAA', 'AAAAAAAA', 'AA', 'AAA', 'AAAA', 'AAAAA', 
        # 'AAAAAA', 'AAAAAAA', 'AA', 'AAA', 'AAAA', 'AAAAA', 'AAAAAA', 'AA', 'AAA', 'AAAA', 'AAAAA', 'AA', 
        # 'AAA', 'AAAA', 'AA', 'AAA', 'AA'], which is 36 substrings, hence we can see the highest space complexity of the output is O(N^2)
        # because the number of output is following the formula of (N(N+1)/2) - N, where N is the length of the genome sequence, in this case
        # hence the formula will be (9(10)/2 = 45) - 9 = 36. The reason for the - N is because the start and the end cannot be overlapping, 
        # this - N is to account for the single character substrings, where for "AAAAAAAAA", there exists 9 single substring "A", where their 
        # source_index is also their end_index, which is not a valid substring according to the specification. Nonetheless, since the formula is 
        # (N(N+1)/2) - N, the space complexity of the output is still bounded by O(N^2). 
        # the worst time complexity is also O(N^2) for generating this output.

        # time complexity will be constant if either start and end does not exist in the trie, hence the output will be an empty list.
        output = []

        # run search on the start
        # if this subtring exists, store the children_tuple of the last node of the start into first_half
        # inherited time complexity from the search function is O(|start|), |start| is the length of the start substring
        # inherited space complexity from the search function is O(1), constant.
        first_half = self.genome.search(start)

        # run search on the end
        # if this subtring exists, store the children_tuple of the last node of the end into second_half
        # inherited time complexity from the search function is O(|end|), |end| is the length of the end substring
        # inherited space complexity from the search function is O(1), constant.
        second_half = self.genome.search(end)
        
        # terminate earlier if either the start or end does not exist in the trie
        # if either the start or end does not exist, return an empty list
        if second_half == [] or first_half == []:
            return []
        
        # check if the start and end overlap
        # using a double for loop here due to the possibility of multiple tuples in the children_tuple in both start and end
        # the worst case time complexity is O(N^2) for this double for loop, this worst case time complexity when the genome
        # sequence is only one repeating character, for example genome is "AAAAAAAAA", and the start and end are both single "A".
        # hence the chidren_tuple of the start will have 9 tuples, and the children_tuple of the end will have 9 tuples, a double for
        # loop for running 9 * 9 times, hence the worst case time complexity is O(N^2).

        # in the double for loop, there will be list slicing, which is O(N) time complexity
        # hence the worst case time complexity is O(N^3) for the double for loop

        for i in first_half:
            for j in second_half:
                if i[2] - 1 < j[1]:
                    output.append(self.genome_with_terminal[i[1]:j[2]])
        
        return output
    