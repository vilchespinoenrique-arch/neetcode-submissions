class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        


        # my idea for this question is to get the 2 smalles and the 2 biggest and then subtract them and that should give the answer. however i believe that i could use a heap for this, but i havent use heap in a minute so i wont use it right now 


        # but since i havent done heap in a while, i rather just use a easier approach and that is to sort the algorithgm 


        sort_nums = sorted(nums) 

        biggest_number = sort_nums[-1]


        second_biggest_number = sort_nums[-2]


        smalles_number = sort_nums[0]


        second_smalles_numbers = sort_nums[1]




        
        a = biggest_number * second_biggest_number 

        b =  smalles_number * second_smalles_numbers


        return a - b