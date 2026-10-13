class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        # for this question we can use 2 pointer where we will start from the start, and the only way that the left one is actually advancing would be if they find a match, if they dont, the dont adcvance. but you never go back you only go foward, 

        # so if the node at the end has the same lenght as the size of s, it would then mean that is good to go and that we can return true, else we would retubnr false 


        i = 0 

        j = 0 

        while i < len(s) and j < len(t):

            if s[i] == t[j]: 

                i += 1


            j += 1 


        if i == len(s): 

            return True 


        else: 

            return False 
