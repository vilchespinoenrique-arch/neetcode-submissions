class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        

        # for this question we are going to check, and make a comparison to find the answer, because the other way is to advance 


        pointer = 0 

        save_index = 0

        for i in range(0, len(haystack)):

            keep_going = i

            pointer = 0


            if pointer < len(needle) and haystack[i]  == needle[pointer]:

                save_index = i
            
                while keep_going < len(haystack) and pointer < len(needle) and haystack[keep_going] == needle[pointer]: 

                    keep_going += 1 

                    pointer += 1 

                
                if pointer == len(needle): 
                    
                    we_got_it = save_index

                    return we_got_it

            
        return -1


                


            

            

