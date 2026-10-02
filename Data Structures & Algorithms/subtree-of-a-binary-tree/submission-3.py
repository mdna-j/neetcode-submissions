# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def dfs(self, root, tree):
        if not root:
            tree.append(None)
            return tree
        
        tree.append(root.val)
        left = self.dfs(root.left, tree)
        right = self.dfs(root.right, tree)



        return tree  

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        main = self.dfs(root, [])
        if str(self.dfs(subRoot, []))[1:-1] in str(main)[1:-1]:
            return True
        return False
        