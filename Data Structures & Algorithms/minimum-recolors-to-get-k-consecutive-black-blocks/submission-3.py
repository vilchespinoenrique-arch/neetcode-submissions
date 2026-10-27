class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        

        # the idea that i have for this question is that we use

        # while i < k: 

        # we keep on going and moving the other pointer, however if we find a W, we are allowed to change it. and then we see which iterations tooks the least amount to do 

        

        i = 0 
        least = 10000

        for j in range(0, len(blocks) - k + 1): 
             

              
            i = j 
            count = k

        

            counter_to_black = 0


            
            while i < j + k: 


                if blocks[i] == "B":

                    count -= 1

                
                elif blocks[i] == "W":

                    count -= 1 

                    counter_to_black += 1 
                    
                i += 1


            least = min(least, counter_to_black) 

        return least 

