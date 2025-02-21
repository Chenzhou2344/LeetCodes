# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0,head)

        prev = dummy_node
        if prev.next==None or prev.next.next ==None:
            return head
        else:
            c1 = prev.next
            c2 = c1.next
        c1 = prev.next
        c2 = c1.next

        while(c2):
            c1.next = c2.next  
            c2.next = c1
            prev.next =  c2
            
            prev = c1
            if prev.next==None or prev.next.next ==None:
                break
            else:
                c1 = prev.next
                c2 = c1.next
        
        return dummy_node.next
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(next=head)
        current = dummy_head
        
        # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
        while current.next and current.next.next:
            temp = current.next # 防止节点修改
            temp1 = current.next.next.next
            
            current.next = current.next.next
            current.next.next = temp
            temp.next = temp1
            current = current.next.next
        return dummy_head.next
