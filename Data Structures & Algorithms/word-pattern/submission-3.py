class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        

        # we want to solve this question using steps 


        # step 1. split the s,

        # step 2. zip them together 

        # step 3. create a hashmpa for pattern to s 

        # step 4. create a hashmap for s to pattern 

        # step 5. if we see that we have the same letter for different values return false 

       
       
       #  "ab" ->  # "dog dog" 

       # a -> dog 

       # b -> dog 


       # dog -> a 

       # dog -> b, which would be wrong becasue we have the same key twice it would replace the old value, but we would do an if that we wont allow 




        from_p_to_s = {} 

        from_s_to_p= {}


        new_s = s.split() 


        if len(new_s) != len(pattern): 

            return False 

        # s looks like this: 

        # there is now a comma in between spaces 


        # s = {dog, cat, cat, dog}

        for char_p, char_s in zip(pattern,new_s): 

            # right now the zip looks like this 

            if char_p in from_p_to_s and char_s != from_p_to_s[char_p]:
            
                return False 

            if char_s in from_s_to_p and char_p != from_s_to_p[char_s]: 

                return False    

        

            from_p_to_s[char_p] = char_s
            from_s_to_p[char_s] = char_p

        
         
        return True



        
        

