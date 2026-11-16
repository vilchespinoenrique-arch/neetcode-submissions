class TrieNode: 

    def __init__(self):


        self.children = {}

        self.is_true = False 


def insert(word, root): 


    node = root 


    for ch in word: 

        if ch not in node.children: 

            node.children[ch] = TrieNode() 
        
        node = node.children[ch]

    node.is_true = True 




class Solution:

    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:


        root = TrieNode()

        for w in words: 

            insert(w, root)  # now we have created the trie holding all words 

    
        res = [] 

        for i in range(len(text)): 

            node = root  # so that at the we start in the head of the pointers 

            for j in range(i, len(text)): 

                ch = text[j]

                if ch not in node.children: 

                    break 

                node = node.children[ch] # we will set node to that one letter 

                if node.is_true:  # if this is true it means that we have reach the end of it 

                    res.append([i,j])

        return res 
        
