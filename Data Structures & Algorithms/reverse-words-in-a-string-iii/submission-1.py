class Solution:
    def reverseWords(self, s: str) -> str:
        pass


         # the first thing i want to do is make to split the words into a list so that is not a whole string with senteces 


        words = s.split(" ") # now we have this for this example: 


        # s = "ab cd"


        # is now : 

        # word = [ab, cd] 

        result = []


        for word in words: 


            # so here is the thing and i didnt know it, but you cannot swap letter in a string, so i cannot swap "ab"

            # as word[0], word[1] = word[1], word[0], there is this rule that becasue the letter are together i cant just separate them and do what i want, so for this reason i need to do something else lol! i need to get those words and make them a list of letter so it would be like this 


            # ab = [a,b ] and then compare, which i think is dumb, but is just how it workds



            new_word = list(word)


            # now new_word hold this:

            # new_word = ["a", "b"]


            left = 0 

            right = len(new_word) - 1 



            while left <= right: 


                new_word[left], new_word[right] = new_word[right], new_word[left] 


                left += 1 


                right -= 1 


            
            final = "".join(new_word)

            # after the fact join them back again 

            result.append(final)


            final_1 = " ".join(result)

    
        return final_1 
        
        


            
