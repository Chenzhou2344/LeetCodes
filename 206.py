#偷懒改列表
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)
        current_node = dummy_node
        valls = []
        while current_node.next:
            current_node = current_node.next
            valls.append(current_node.val)

        current_node = dummy_node
        idx = 0
        while current_node.next:
            current_node = current_node.next
            current_node.val = valls[-1-idx]
            idx+=1
        
        return dummy_node.next
    
#正确做法、class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    current = head

    while(current):
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

    return prev
