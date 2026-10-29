# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        


        current = head 

        # now current is poiting to the star of the list link 


        while current and current.next: 

            next_link = current.next 


            if next_link.val == current.val:

                current.next = next_link.next  


            else: 
                
                current = current.next 

        
        return head 