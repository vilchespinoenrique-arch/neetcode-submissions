class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # for this question we want to have 3 pointers: 

        # one pointing to the biggest of nums1, 

        # anothe pointing to last element of num 2, 

        # and another poiting to the first nums 


        i = m + n - 1 # this represents the index we are going to replace

        j = m - 1 

        k = n - 1


        while k >= 0: 

            if j >= 0 and nums1[j] > nums2[k]:

                nums1[i] = nums1[j] 
                j -= 1 
            
            else: 
                nums1[i] = nums2[k]

                k -= 1 
            
            i -=1 


