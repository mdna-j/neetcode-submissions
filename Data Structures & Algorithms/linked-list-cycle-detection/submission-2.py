# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the head of the list
        slow = head
        fast = head
        
        # Traverse the list as long as the fast pointer can move two steps ahead
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If the pointers meet, a cycle exists
            if slow == fast:
                return True
                
        # If the fast pointer reaches the end, there is no cycle
        return False