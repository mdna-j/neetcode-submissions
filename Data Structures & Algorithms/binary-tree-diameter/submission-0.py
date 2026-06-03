# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def dfs(node):
            if not node:
                return 0
            
            # Recursive call to get the height of the child node
            leftH = dfs(node.left)
            rightH = dfs(node.right)

            # Updates the global maximum diameter
            self.maxDiameter = max(self.maxDiameter, leftH + rightH)

            # Return height of the current node
            return 1 + max(leftH, rightH)

        dfs(root)
        return self.maxDiameter        