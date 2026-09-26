class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
       
        hashmap = {}
       
        for i, char in enumerate(keyboard):

            hashmap[char] = i 

        # this will create our hashmap with the char as the key, and the index as the value 

        # now we have: 

        # hashmap = {a : 0, b : 1, c : 3 *** }

        current_position = 0

        total_position = 0 


        for char in word: 

            if char in hashmap: 

                distance = abs(current_position - hashmap[char])   # this will give us the index, for the current value 

                # 

                # pqrstuvwxyzabcdefghijklmno

                # current_position = 0 - 23 = 23 

                # total = 23 + 0 = 23 


                # now we are at which current position is 23 - 15 = 8 

                # current positio is no

                total_position = total_position + distance  

                current_position = hashmap[char]
        
        
        return total_position


