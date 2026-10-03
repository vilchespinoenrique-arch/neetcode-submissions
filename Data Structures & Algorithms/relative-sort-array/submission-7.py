class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        

        # my idea here is that im gonig to take arr1, and put it on a hashmap, i wil have the count of each element, once that is done i will go one by one and return the amount that it appears + 1 the one that is currently on, and return that number that amount 



        hashmap = {} 


        for ar in arr1: 


            hashmap[ar] = hashmap.get(ar, 0) + 1


        # now we will have a list like this: 



         # { 2: 3, 1 : 1, 4 : 1, 3 : 2}


        new_list = []

        for ar2 in arr2: 


            if ar2 in hashmap: 


                for key, value in hashmap.items(): 

                    if key == ar2: 
                    
                        for i in range(0, value): 

                            new_list.append(key)



        left = []

        for lol in arr1: 

            if lol not in arr2: 

                left.append(lol)




        # whats left is now  a set do 

        # whats left now can be included, but we have to sort it 


        bro = sorted(left)

        
        

        for yea in bro: 

            new_list.append(yea)


        return new_list

        




        


                    


