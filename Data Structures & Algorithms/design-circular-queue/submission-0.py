class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.next, self.prev = val, nxt, prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.qcount = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0,None, self.left)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = curr
        self.right.prev = curr
        self.qcount -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.qcount += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.next.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        if self.left.next == self.right:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.qcount == 0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()