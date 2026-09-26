class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # for this question we must remember 2 things. the first is that 

        # return "".join(result) # this takes our list and makes into a fluent string in the list, which is what we want 

        # now the idea is simplpe. have 2 pointer tracking our question and we want to attach each one to result 

        result = []

        i = 0 
        j = 0 

        while i < len(word1) and j < len(word2): # while both of them are bigger than the current one we will keep on going
        # but if it does happen that eventually one of them is not longer we will stop and we will attach tehm at the end 

            result.append(word1[i]) 
            i += 1 

            result.append(word2[j])
            j += 1 

        
        result.append(word1[i:]) # this will append the rest, and if there is nothing there it will append nothing
        result.append(word2[j:]) # same idea here, it will append eveything at the end if something is left 

        return "".join(result)
        
        