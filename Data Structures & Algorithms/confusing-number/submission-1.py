class Solution:
    def confusingNumber(self, n: int) -> bool:
        

        # there are a lot of factoes goin on in this question. however it can be solved 


        # first of all we will want to use a map 

        # the reason why we want to use a map, is becasue we want to inmediatly have a map for the numbers that can be rotated, those numbers are 


        # 0, 1, 6, 8, 9 , and the rest cannot be rotated, so if we see them we will return fasle 



        map = { '0': '0', '1':'1', '6': '9', '8':'8', '9': '6'} # if we give them the key of 9, 6 etc we will return the value, which in the case of the 6 for example is the 9, and the case of 9 is the 6

        # and so on with the rest of the code 

        string = str(n) # we want to make the numbers string that way i can handle them 

        current_char = [] 


        for char in reversed(string): # here we will have the string reversed, becasue that way we will be able to compare the last number with the current number

        # i will show why that makes sense in a minute 
            if char not in map: 

                return False 

                # if not of the values are in char, you can go ahead and return false inmediately, becasue it means that they cannot be rotated
        
            current_char.append(map[char] ) # this will appedn the flip char 

            # so we will have for example for 89 

            # we will get, current_char = [6, 8] 

            # but now we have to join them 
        
        rotated_numbers = "".join(current_char)



        if rotated_numbers == string: 

            return False 
        else: 
            
            return True 