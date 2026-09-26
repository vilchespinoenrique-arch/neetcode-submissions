class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 

        hashmap = {}
        hashmap1 = {}
         
        for c in s: 
            hashmap[c] = hashmap.get(c, 0) + 1

        for y in t: 
            hashmap1[y] = hashmap1.get(y, 0) + 1 

        if hashmap == hashmap1: 
            return True 
        else:
            return False 