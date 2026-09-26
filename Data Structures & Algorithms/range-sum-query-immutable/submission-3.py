class NumArray:

    def __init__(self, nums: List[int]):


        self.nums = nums

        
        

    def sumRange(self, left: int, right: int) -> int:


        # nums here is already saved as a list, so we can go ahead and use it right away 

        # [-2,0,3,-5,2,-1]

        # 1 example: [0,2],

        # 2 example: [2,5],

        # 3 example: [0,5]

        total = 0

        while left < right + 1: 

            total = total + self.nums[left]

            left = left + 1

        
        return total
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)