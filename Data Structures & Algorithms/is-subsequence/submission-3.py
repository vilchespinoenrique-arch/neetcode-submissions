class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # for this question we can use 2 pointers 

        # where the i pointer will stay with the letter s, and point j will stay with the letter t 

        # and we will move i to the right if we finda  comparison, and we will move j to the right all the times 




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


        # this wokrs because we can go throuh s, and check for each one in t. if s doesnt finish it means that they were not a subsequence 