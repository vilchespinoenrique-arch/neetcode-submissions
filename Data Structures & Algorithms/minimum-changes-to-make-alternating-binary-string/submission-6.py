class Solution:
    def minOperations(self, s: str) -> int:
    
    # so this question is more complicated than previously thought the reason for this is becasue
    # we have 2 options on what could happen. 

    # we have the first patter: 

    # patter 1- is the values we have, and then changinf whatever we can change.

    # patter 2- starting with the complete opposiete


    # so it would look like this 

    # patter 1 - 0101 -> notive how we only change 1 number! 

    # patter 2, we dont even have to do it, becasue if we do the exact opposite of pattern 1

    # it will be 3 changes right aways! becasue the only one that didnt change was the last one, and remeber this 2 will be complete opposoties

    # so we would have to change 3 of them and the one that we changed for them, should remain the same

    # so patern 2 =  3, which is the same 1 - n = 3 n being the total of the character and 1 being the changes we did. 


        smaller = 0
        count = 0
    
        for i in range(len(s)): 

            if i % 2 == 0:

                if s[i] != '0':
                
                    count += 1
            
            elif i % 2 == 1: 

                if s[i] != '1': 

                    count += 1

        pattern2 = len(s) - count

        smaller = min(count, pattern2)

        return smaller 
