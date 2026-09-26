class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        # this question actually is really smart. is you think about it, a palindrome that can be move everywehre can only be a palindorme if it has 1 or 0 numbers that are not paired.. lets me show u the examples 


        # aab 

        # a  a  this 2 cancel each other, leaving one of the others to stay in the middle. 


        # look at another one 


        # aaab 

        # this one has a   a those 2 cancel each other, but then we have 2 that are not equal... 

        # a ab   a   since this 2 are not equal, and we have more than 2 ones that are not equal, this can never be a palidnrome 



        match_pair = set() 


        for char in s: 

            

            if char not in match_pair:
                match_pair.add(char) 

            else: # if the  char is in the char, already it means that we can 
                match_pair.remove(char) # if we see it again, go ahead and remove it from the set 

            
        # if we end up with more than 1 number on the set, that means that we didnt find a match for 2 of them 


        if len(match_pair) == 1 or len(match_pair) == 0: 

            return True
        
        else: 
            return False 