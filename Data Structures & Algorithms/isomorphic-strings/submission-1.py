class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

    # for this quesiton what we want to do, is we want to create 2 hashamps, we are going to be checking if the first character of e is already the key of the first character of the seonc one and so on and on


    # first check: 


    # is s the key of a value a? 


    # is s:a?   

    # if there is nothing there, add something, but first check if that is true. if for some reason the key of s maps to something else that it not that add

    # then we return false inmediately, else we keep going 



    # then we do the same thing with a 

    # is a the key of e? becasue it can be either or 


    # is e:a?  if it is not them we can go ahead and return false, but if it is, we can keep going 



        from_s_to_t = {} 

        from_t_to_s = {} 



        for char_s, char_t in zip(s,t): 


        # creatubg a zip is useful because it matches everything with everything 


        # for example we will have
        
        
        # s = "egg"  and t = "add" 

        # a zip puts them like this 


        # zip = [(e,a), (g,d), (g,d)] and so on if they were more characters 


        


        # first thing lets check if s is a key for t 
        
            if char_s in from_s_to_t: 

                if from_s_to_t[char_s] != char_t:

                    return False 

            # if they are equal leave it like that, dont do anything, it means that they are correct 

            else:

                from_s_to_t[char_s] = char_t 




            if char_t in from_t_to_s: 

                if from_t_to_s[char_t] != char_s:

                    return False 

            from_t_to_s[char_t] = char_s 




        return True  


















