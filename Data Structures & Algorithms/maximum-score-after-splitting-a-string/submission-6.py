class Solution:
    def maxScore(self, s: str) -> int:
        

        # wait for me the obvious answer would be to sort this, and then slpit it when it hits a 1. lol 


        # i was gonna turn the s into a int, and then sorted, but because i would then need to make a list, that would take to long, so instead of that im going to use s, and sort s, becasue it will still work, 


        # the reason on why it wouldnt work to make this an int and sorted is becasue it would become a whole number. like it wouldnt happen that each number had a different value, it would just be one number, becasue it would become s = 0111101 

        # which is just 1 number 

# ----------------------------------------------------------------------------------------------------------------------------# 

# this is a great explanation but i just realized this doesnt work, becasue i have to maintain the way s is lol.

# well the only way i can come up with an asnwer, is by checking every possibilty. 


# but there is a better way, and i needed a hint, but we got there. 

        

        total_amount_one = s.count("1")

        total_amount_zero = 0

        result = 0

        for char in s[:-1]: 

            if char == "0": 

                total_amount_zero += 1


            else: 
                total_amount_one -= 1


            result =  max(result, total_amount_one + total_amount_zero)




        return result 

        













