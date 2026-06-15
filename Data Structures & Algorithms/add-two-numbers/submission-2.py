# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ''
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        num2 = ''
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        sum = int(num1) + int(num2)
        sum_str = str(sum)
        head = ListNode(0)
        dummy = head
        for i in range(len(str(sum))-1,-1,-1):
            new_node = ListNode(str(sum)[i])
            head.next = new_node
            head = head.next
        return dummy.next
