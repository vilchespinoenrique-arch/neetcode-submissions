class Solution:
    def maxDifference(self, s: str) -> int:


        hashmap = {} 


        for char in s: 


            hashmap[char] = hashmap.get(char, 0) + 1       # this will give us a number for each one 


        # at the end it wil look like this: 


        # hashmap = { a : 5, b : 2, c: 1} 


        
        
        
        # once we have the hashmap what we want to do is we want to set a for loop looking at their values, and we want to findh the biggest 



        # now we want the biggers odd 

        # and we want the smallest event 


        # that way we can have the maximum difference between the 2 

        

        bigger_odd = 0 

        min_even = 100000000


        for frequency in hashmap.values(): 


            if (frequency % 2) == 0:  # this would mean that the number is even 

                if frequency < min_even: # if the current frquency is smaller than the min_even from the previous then save min evene as such 

                    min_even = frequency 

                else: # if it isnt 

                    continue  




            else: # is odd 

                if frequency > bigger_odd: 

                    bigger_odd = frequency 

                else: 

                    continue 

        
        diff = bigger_odd - min_even 


        return diff 



        






    








        