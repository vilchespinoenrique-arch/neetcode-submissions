# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # in order to get the middle of a linked list 

        # there is a smart way of doing this, and that way is having a slow and fast pointer. look at this example 

        # slow = slow.next 

        # fast = fast.next.next


        # 1,2,3,4,5 ->

        # slow will go 1
        # fast will go 2 


        # slow will go 2 
        # fast will go 4 

        # slow will go 3
        # fast will go 5 -> next which is none, so this ends here 


        # so the mid will be in slow 


        slow = head 

        fast = head 


        while fast and fast.next: 

            slow = slow.next 

            fast = fast.next.next 

        
        return slow 



        