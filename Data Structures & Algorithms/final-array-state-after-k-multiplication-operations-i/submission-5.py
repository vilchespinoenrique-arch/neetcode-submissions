import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        

        heap = [] 

        for i, x in enumerate(nums): 


            heapq.heappush(heap, (x,i))



        
        for _ in range(k):


            smallest_value, index = heapq.heappop(heap)


            new_value = smallest_value * multiplier


            heapq.heappush(heap, (new_value, index))


        
        for value, index in heap: 


            nums[index] = value 


        return nums 