class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        

        g.sort() 

        s.sort()

        # we want to sort g, becasue that way if a kid doesnt take a copy we end right there, becase we cannot keep going 


        i = 0 

        j = 0 


        count = 0 


        while i < len(g) and j < len(s):


            if g[i] <= s[j]: 

                count += 1 


                i += 1 

                j += 1 

            else: 

                j += 1 

        return count 
    
