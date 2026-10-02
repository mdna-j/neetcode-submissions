# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy placeholder node
        dummy = ListNode()
        current = dummy
    
        # 2. Loop until one list runs dry
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 3. Splice whatever remaining nodes are left
        current.next = list1 if list1 else list2
    
        # 4. Return the starting head of the merged list
        return dummy.next