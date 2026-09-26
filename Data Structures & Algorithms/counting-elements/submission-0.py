class Solution:
    def countElements(self, arr: List[int]) -> int:


        my_set = set() 

        count = 0

        for ar in arr: 

            my_set.add(ar) 

            # go ahead an add all the unique values. we want all the unique values, that way when we will have the ones that dont repeat in the set
            # however if we then see a duplicate that is looking for the + 1 value, we can just go ahead and find it that wau 


        # we dont duplicates becasue then we would be able to succesfuly found the + 1.. it would honestly just become a mest 

        
        for yep in arr: 

            if yep + 1 in my_set: 
                
                count = count + 1 


        return count 

        
        