class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        


        hashmap = {} 



        for name, height in zip(names, heights): 

            hashmap[height] = name

        # now our hashmap will look like this: 



        # hashmap = { mary : 180, john: 165, emma: 170}



        # now we sorted them to organized them in descendin order 


        new_hashmap = dict(sorted(hashmap.items(), key=lambda pair : -pair[0]))


        # now the new hashmap has officially been updated so that is in increasing order based on the height. 



        new_list = []

        for key, value in new_hashmap.items(): 

            new_list.append(value)
            

            


        return new_list



