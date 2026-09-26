# a prefix tree is use to store strings

# a prefix tree is very useful, becasue it can help you organize different keys, for example lets say we have
# cat, car, cal 

# we can store a letter of each string, and then they would share the same first 2 letters,
# which are c and a 

class PrefixTreeNode: # this will be for the variabels of the tree 

    def __init__(self):

        self.children = {} # we have to initialize the children, in here is where the kids of the words will be 
        self.is_end = False # in here we would have set true if the word is in it last char. 
       
class PrefixTree: 

    def __init__(self):
        self.root= PrefixTreeNode() # here we would have root, with the variabels of the calss treenode, in prefix tree, so that everytime we create a prefixtree it will create a new ndoe with the properties of prefix node


    def insert(self, word: str) -> None:

        node = self.root 

        for char in word: 

            if char not in node.children:
                node.children[char] = PrefixTreeNode() # if the char is not in the root, then create one for it 
            
            node = node.children[char] # if is there, then just save in node, and check it for the next one
            
        node.is_end = True # at the end of the word, save to true 



    def search(self, word: str) -> bool:

        node = self.root 

        for char in word: 
            if char not in node.children: 
                return False
            
            node = node.children[char]# even if is false for one.. keep on looking to see if you can find the next one 
        

        return node.is_end
        # if the we make it to the last part, then that would mean, and that part is true, it would mean that was the end of the word 



    def startsWith(self, prefix: str) -> bool:
        
        node = self.root 

        for char in prefix: 
            if char not in node.children: 
                return False
            
            node = node.children[char]# even if is false for one.. keep on looking to see if you can find the next one 
        

        return True # is just checking if the path exists, and if it does return true 
        

