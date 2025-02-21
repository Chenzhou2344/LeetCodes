class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.dummy_head = ListNode()
        self.list_size = 0

    def get(self, index: int) -> int:
        idc = 0
        next_node = self.dummy_head.next
        if index >= self.list_size:
            return -1
        else:
            while idc < index:
                next_node = next_node.next
                idc += 1
            return next_node.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.list_size += 1

    def addAtTail(self, val: int) -> None:
        next_node = self.dummy_head
        while next_node.next:
            next_node = next_node.next
        next_node.next = ListNode(val)
        self.list_size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        idc = 0
        prev = self.dummy_head
        next_node = self.dummy_head.next
        if index == self.list_size:
            self.addAtTail(val)
        elif index < self.list_size:
            while idc < index:
                prev = next_node
                next_node = next_node.next
                idc += 1
            prev.next = ListNode(val, next_node)
            self.list_size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.list_size:
            idc = 0
            prev = self.dummy_head
            next_node = self.dummy_head.next
            if index < self.list_size:
                while idc < index:
                    prev = next_node
                    next_node = next_node.next
                    idc += 1
                prev.next = next_node.next
            self.list_size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)




#Carlos' solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy_head.next
        for i in range(index):
            current = current.next
            
        return current.val

    def addAtHead(self, val: int) -> None:
        self.dummy_head.next = ListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = ListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)