class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        

        hashmap = {} 


        for i, char in enumerate(keyboard): # here the order matter, the i will be the index, and the char will be the letter 

            hashmap[char] = i 


        # now we have all of the values in this hashmap... 



        current_value = 0 # this will keep charge of the current value 

        total_value = 0 # this will be the value added up


        for leter in word: 

            if leter in hashmap: 

                distance = abs(current_value - hashmap[leter]) # the current value - the leter that we are right now, will be the distance between those 2 


                total_value = total_value + distance 


                current_value = hashmap[leter] # the new current value will be the index, where we left off 



        
        return total_value

