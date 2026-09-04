# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases easily
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Move both fast and slow until fast reaches the last node
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
            
        # Remove the target node
        slow.next = slow.next.next
        
        return dummy.next