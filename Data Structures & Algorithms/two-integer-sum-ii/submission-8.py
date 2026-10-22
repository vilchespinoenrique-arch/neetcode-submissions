class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # so since this quesiton is 0(1) in space it means that we cannot use a map or a set. how we did we the original 2 sum. however one thing
        # that we can do because the element are organize. is go increase either left or right depending on if we need a higher number of a 
        # smaller number 

        left = 0
        right = len(numbers) - 1

        while left < right: 
            
            if target == numbers[left] + numbers[right]:
                return [left + 1, right + 1]

            if target > numbers[left] + numbers[right]:
                left += 1 

            if target < numbers[left] + numbers[right]:
                right -= 1 
        
        return [-1, -1] 