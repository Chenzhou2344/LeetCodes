# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while(head!=None and head.val == val ):
          head = head.next
        if head == None:
            return None

        prev = head
        nextnode = head.next
        while(prev.next!=None):
            if nextnode.val == val:
                prev.next = nextnode.next
                nextnode = prev.next
            else:
                prev = nextnode
                nextnode = nextnode.next
        return head
    
#虚拟头节点法
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next