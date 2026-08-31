# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
         # Edge case: If the tree is empty, return an empty list
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize queue with the root node
        
        while queue:
            level_length = len(queue)
            
            # Iterate through all nodes at the current level
            for i in range(level_length):
                node = queue.popleft()
                
                # If it's the last node in the current level, it's visible from the right
                if i == level_length - 1:
                    result.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return result