class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        seen = set(nums1) 

        result = []

        another_set = set(nums2)

        for number in another_set:

            if number in seen: 

                result.append(number)

            else: 

                continue 

        return result 
