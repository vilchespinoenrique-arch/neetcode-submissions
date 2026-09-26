class NumArray:

    def __init__(self, nums: List[int]):
        

        # if we want to make this efficient a way of doing it, is by sum of eveything that we have seen. the reason why we want to do that, is becasue we dont have to sum up them up, and when they tell 2 indexes, we just use those indexes to find the asnwer ill show you how in a second


        self.nums = nums # nums is where we will save our numbers coming from num 


        self.running_sums = [None] * len(nums)

        # this is going to give us a list with the same amount as nums  

        total = 0

        for i in range(0, len(nums)): 

            total = total + nums[i] 

            self.running_sums[i] = total


    def sumRange(self, left: int, right: int) -> int:

        # now self.running_sums will always have the add one of what we already did, and we can use that to our advantage 

        if left == 0: 

            return self.running_sums[right]  
        
        else :

            return self.running_sums[right] - self.running_sums[left - 1] 
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)