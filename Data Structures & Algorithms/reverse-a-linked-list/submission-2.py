# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # i havent done a linked list in a minute,

        # but for memorization 

        # if we say current = head. current is pointing to the head of our linked list 


        # the visual would be like this 
#
 #       head ─┐
#               ▼
   #           [0] → [1] → [2] → [3] → None
    #           ▲
#       current ┘


# so once we incorporate the current that means that we will point to the head now of the node 



        current = head 

        prev = None 


        # for now we are going to create a value that is none. so nothing is in there yet. but we will use to reverse the linke list 

        while current:  # while current is still true, and is not none, we can keep going 

            # so everytime we get a value, we want to save the current value, and we want the next value to be held together by the previous value, for eample 

            # 0 we would save it.

            # we would also save the 0, which is 1. 

            # then using prev, which has nothing held but none, we would want to connect the 1 in front of 0. so it would look like this 

            # 1 -> 0 -> none  this is what we are trying to achieve 


            next_node = current.next # next node is holding the next value, which is 1 

            # before we invert anything we need to save the rest of the linked list, that is important 

            # so right now next_node is saving the entire linked list 

            # next _ node = 1 -> 2 -> 3 

            # so that means that the previous current, we can attach it to the prev. so that we can inver it 

            current.next = prev 


            # right now we are looking like this 

            # 0 -> null 

            # which is exactly what we want becasue is getting inverted. you will see 

            # now we need to make the new current, to be the one that we saved so that we can keep  on going 


            # we have integrated, however prev has not changed. so we need to change, the changes that we just amde 

            prev = current 

            # remener that we just changed current to be

            # 0 -> null 

            current = next_node 


        return prev 
