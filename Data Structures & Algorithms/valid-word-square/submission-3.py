class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        # this quesiton might be confusing, but we can do it simple, so that we check for the rows and collum, we want to make sure that those are the same

        # there is a trick in the mind, that makes this problem much, much easier 

        # this about this. 

        # we know that (0,1) and (1,0) or that (0,2) and (2,0), this are the mirror of each other that we are looking for
        # and that can be solved by just changing the grids 


        # for example: 

        #  grid[r][c] == grid[c][r] 

        # if we flip them we would look for the mirror side of them 


        row = len(words)




        for r in range(row):
            for c in range(len(words[r])): 

                if c >= row: # if there are not symetrical, then you can go ahead and return false inmediately 

                    return False 

                    # it cannot happen that the collumns are more than the rows.. that would make it not symetrical and it would be wrong ! 

                # now we have to check for the other side, if the rows are bigger than the collumns, then it would aslo not be symetrical

                if r >= len(words[c]): # if they are bigger than the collumns, then it would not be symetrica 

                    return False 


                if words[r][c] != words[c][r]:

                    return False 

        return True 