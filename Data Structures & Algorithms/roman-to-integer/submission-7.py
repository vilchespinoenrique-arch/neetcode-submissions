class Solution:
    def romanToInt(self, s: str) -> int:
        
        # for this question we can use a dccionary to map all of this. and what we do witht the subtractions? what we want to do is that if the letter has a smaller value than the next one, then we can subtract from them 



        dictionary = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C': 100, 'D' : 500, 'M' : 1000}

        total = 0

        for i in range(0, len(s)):


            if i == len(s) - 1 or dictionary[s[i]] >= dictionary[s[i + 1]]: 


                total = total + dictionary[s[i]]

            
            else: 

                total = total - dictionary[s[i]]


        return total 