class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        

        hashmap = {} 



        for mag in magazine: 

            hashmap[mag] = hashmap.get(mag, 0) + 1




        # this will give us the list of each number and their frequency 


        # hashmap = {a : 2, b : 1} 


        for ran in ransomNote:

            if ran in  hashmap: 

                hashmap[ran] = hashmap[ran] - 1

                if hashmap[ran] == 0: 

                    del hashmap[ran]

            else: 

                return False

        return True 


