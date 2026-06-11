# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        while curr:
        # Both nodes are smaller, move left
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
        # Both nodes are larger, move right
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
        # LCA found! Paths have split
            else:
                return curr
        return None
        