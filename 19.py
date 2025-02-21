# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        idx = 1
        dummy_node = ListNode(0,head)
        low = dummy_node
        fast = dummy_node

        for i in range(n+1):
            fast = fast.next       

        while fast:
            low = low.next
            fast = fast.next

        low.next = low.next.next

        return dummy_node.next                                                                                             