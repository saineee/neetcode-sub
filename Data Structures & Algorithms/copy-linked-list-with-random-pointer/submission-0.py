"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
       old = {}

       curr = head
       while curr:
        old[curr] = Node(curr.val)
        curr = curr.next

       curr = head
       while curr:
        old[curr].next = old.get(curr.next)
        old[curr].random = old.get(curr.random)
        curr = curr.next

       return old.get(head)