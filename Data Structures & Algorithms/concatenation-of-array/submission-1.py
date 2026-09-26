class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # for this question we are being asked to do a dupplicate of this, there are 2 maing ways to do this
        ans = []

        for num in nums:
            ans.append(num)
        
        for num in nums:
            ans.append(num)
        
        return ans

        