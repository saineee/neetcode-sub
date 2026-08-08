class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy

        while True:
            scout = prev_group_tail
            for _ in range(k):
                scout = scout.next
                if not scout:
                    return dummy.next
            
            next_group_head = scout.next
            curr = prev_group_tail.next
            prev = next_group_head

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            old_group_head = prev_group_tail.next
            prev_group_tail.next = prev
            prev_group_tail = old_group_head