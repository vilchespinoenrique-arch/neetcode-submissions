class Solution:
    def countSeniors(self, details: List[str]) -> int:
        


        # for this question since we know that there are exactly 15 character we can do someting really simple called slicing

        count = 0

        for d in details: 

            age = int(d[11:13]) # this will give us the age of the value, that is on the 11 - 13 slice, 

            # so 11 and 12 , which are 7 and 5, so 75 


            if age > 60:

                count += 1 

        return count 
