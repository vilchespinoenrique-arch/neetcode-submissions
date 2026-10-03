class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        


        # for this quesiton what i want to do is, i want to create  a hasmap witht the indexes and saved those letter and everytime i see them again, count the difference between them 



        hashmap = { }

        longest = 0

        for i in range(0, len(s)): 

            if s[i] in hashmap:  
                    
                    diff = i - hashmap[s[i]] 

                    longest = max(longest, diff - 1)


            else:

                hashmap[s[i]] = i


            new_set = set(s)

            
            if len(new_set) == len(s): 

                return -1 



        return longest