class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        placeholder_head = ListNode(0)
        merged_tail = placeholder_head

        boundary_heap = []

        for original_list_idx, list_head_node in enumerate(lists):
            if list_head_node:
                heapq.heappush(
                    boundary_heap,
                    (list_head_node.val, original_list_idx, list_head_node)
                )

        while boundary_heap:
            node_val, source_list_idx, curr_smallest = heapq.heappop(boundary_heap)
            merged_tail.next = curr_smallest
            merged_tail = merged_tail.next

            if curr_smallest.next:
                next_node = curr_smallest.next
                heapq.heappush(
                    boundary_heap,
                    (next_node.val, source_list_idx, next_node)
                )
        return placeholder_head.next