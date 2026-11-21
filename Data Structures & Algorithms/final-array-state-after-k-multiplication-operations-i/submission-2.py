import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        

        heap = []

        for i, x in enumerate(nums):  # we are going to add index so that we can follow along


            heapq.heappush(heap,(x, i))



        # now we have the min heap 


        for _ in range(k): 

            smallest_value, index = heapq.heappop(heap) # this will return the smalles value at the moment and the index


            new_value = smallest_value * multiplier


            heapq.heappush(heap, (new_value, index))


        for value, index in heap: 

            nums[index] = value
        
        return nums