# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #  0 -> 1 -> 2 -> 3 -> 4
        #  0 -> 4 -> 1 -> 3 -> 2

        # part 1 : find middle, split in 2 halves
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # part 2 : reverse second half
        middle = slow.next
        slow.next = None
        prev = None
        curr = middle
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # part 3 : merge 2 halves
        newhead = head
        while prev:
            temp1 = newhead.next
            temp2 = prev.next
            newhead.next = prev
            prev.next = temp1

            newhead = temp1
            prev = temp2

