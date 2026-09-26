class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # create a hashmap for both words

        # if they are the same then return true 

        if len(t) != len(s):

            return False 
        
        
        hashmap = {}

        hashmap1 = {}
        
        
        
        for char in s:  

            hashmap[char] = hashmap.get(char, 0) + 1 


        for char1 in t: 

            hashmap1[char1] = hashmap1.get(char1, 0) + 1 


        
        if hashmap == hashmap1: 

            return True

        else: 

            return False 


        