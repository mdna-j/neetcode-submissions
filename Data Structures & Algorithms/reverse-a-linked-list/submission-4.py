# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head
        prev = None
        curr = head

        # we need to reverse the list
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # reutnr the new beginning of the list
        return prev
        