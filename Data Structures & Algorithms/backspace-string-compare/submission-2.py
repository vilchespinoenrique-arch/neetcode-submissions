class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        pass


        # this quesiton is on the 2 pointer becasue you can run this question at the same time looking at both s and t at the same time, which is pretty cool if you ask me 


        # and then we do it backwards becasue it makes it easier as so if # is there it means we get to make 2 skips 



        i = len(s) - 1 


        j = len(t) - 1 



        # we have to add a skip one as well becasue if we see # we need to skip, and if there are more than one we keep adding # skips, then we would use a elif statement so that if there is a a skip we will skip, but if there is another #, we will added again 


        skip_s = 0 


        skip_t = 0 


        while i >= 0  or j >= 0: # if one of them rouns out we stop inmediately  


            while i >= 0: 
            
            
                if s[i] == "#": 

                    skip_s += 1 

                    i -= 1  


                elif skip_s > 0: # meaning if there is a skip 

                    i -= 1

                    skip_s -= 1 


                else:


                    break 

            
            while j >= 0: 
            
            
                if t[j] == "#": 

                    skip_t += 1 

                    j -= 1  


                elif skip_t > 0: # meaning if there is a skip 

                    j -= 1

                    skip_t -= 1 


                else:


                    break 

            
            if i >= 0 and j >= 0:

                if s[i] != t[j]: 

                    return False 

            elif i >= 0 or j >= 0: 

                # one letter ran out, so it will be falser 

                return False 

                
            i -= 1 

            j -= 1




        return True 






        

        return True 






 
        