class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        

        # the wat this question is explained is a litle bit weird if you ask me. but what they want me to do is to 

        # look at the abbr 

        # for example "a3e" -> here is sating that we should start after a. 

        # for apple -> we would start at p, and then count the nuber after it, which in this case is 3. 


        # so we would count p -> p -> l, and we woudl land in the e. so that would make it true !! 


        # is that for all of them 



        # first thing i want to do is i want to find the number. once i find the number ill look at the left and right side 


        if word == abbr: 

            return True 


        # lets go one by one and find the matches between abr, and word using a pointer for each 



        i = 0 # for the word  

        j = 0  # for the abbr 


        while i < len(word) and j < len(abbr): 
            
            if abbr[j].isdigit():
           
                if abbr[j] == '0': 

                    return False 
                
                num = 0

                while j < len(abbr) and abbr[j].isdigit(): 

                    num = num * 10 + int(abbr[j])

                    j += 1 

                    
                i += num 

            else:

                if word[i] != abbr[j]: 

                    return False 
                
                i += 1 

                j += 1 

        
        return i == len(word) and j ==len(abbr) 


            




            

        


        