# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head) # we just made sure that the dummy next is the head

        # dummy -> 2 -> 1 -> 4 -> 1 -> 2 -> 3 


        # the dummy is poiting to the head 

        current = dummy 

        # we are going to have current 

        # now current is this 

        #dummy -> head -> 2 -> 1 -> 4 -> 1 -> 2 -> 3 
       #          ^
        # current |


        while current and current.next: 

            if current.next.val == val: 

                current.next = current.next.next # if we have a value that is val, just skip it, and connect current next, to the other value 

            else: 
                current = current.next 
                # if there are not equal, just keep on going 

            # so for example 

        #  #dummy -> head -> 2 -> 1 -> 4 -> 1 -> 2 -> 3 
        #          ^
        # current |


        # in here the 2  == 2 so we skip it. 

        # current.next = 1 -> 4 

        # as you can see we just ignore the value was equal

        
        
        return dummy.next 
        