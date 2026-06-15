# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next # saving next location in a variable so it is not lost
            curr.next = prev # reversing current node's direction to prev
            prev = curr # direction reversed, moving to node
            curr = temp # direction reversed, moving to node
        return prev