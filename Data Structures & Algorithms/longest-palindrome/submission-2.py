class Solution:
    def longestPalindrome(self, s: str) -> int:


        # for this question what im thinking of doing is to see each elemenet and put them in a hashamp, and try to find them pairs, and put the rest in the middle one time or 


        count = {}

        total = 0 
        


        for word in s: 


            count[word] = count.get(word, 0) + 1 

        
        # now we have this: 


        # { a: 1, b: 1, c: 4, d:2}

        # now with this, lets see what we can create 


        for coun in count.values(): 

        

            total = total + (coun // 2) * 2


        if total == len(s):

            return total 

        else: 

            return total + 1


        