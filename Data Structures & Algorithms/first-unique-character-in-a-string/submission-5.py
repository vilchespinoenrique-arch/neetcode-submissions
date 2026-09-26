class Solution:
    def firstUniqChar(self, s: str) -> int:
        

        # for this question i think it would be really useful to use enumerate. that way i can have the index, the frequency as the value, and the letter as the key 


        hashmap = {}

        result = []
        

        for index, char in enumerate(s): 
            

            hashmap[char] = (hashmap.get(char, (0, 0))[0] + 1, index )

            # and know this might look really confusing. but hear me out. 

            # we are doing
             
            
            # n : and then we do hashmap.get(char) -> so if we see the char, now we have a problme becasue our hashmap is 


            # n : (frequency, index) -> becasue of this when we get the char, the hashmap doesnt know which value we are taling about, 

            # becasue of that we add the [0] at the end. so that it can understand that we want the first value, which is frequency and we want that value 


            # we also use (0,0), becasue that is the 0 of our tuple, remeber that we have 2 values in ther 



            # at the end we will have this 


            # hashmap = { n: (1,0), e:(3,1)}

        
            # and so on and on


        for freq, index in hashmap.values(): 

            if freq == 1: 

                result.append((freq, index))


        if result: 
            return result[0][1]

        else: 
            return -1