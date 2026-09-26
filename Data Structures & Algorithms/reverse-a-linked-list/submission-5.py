# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        current = head 

        # make sure that you have a pointer to the head 


        prev = None # prev is going to be the one that will hold the new linked list 


        while current: 


            next_node = current.next # save the next node, becasue we are going to use the current one 


            current.next = prev # we just set the current next pointer to the prev, whihc for now is null 


            prev = current # we make sure to save the properties of prev, becasue this is where the reversed linked list will be saved 

            current = next_node # make sure that the next node is current so that we can keep on going 



        return prev 
        