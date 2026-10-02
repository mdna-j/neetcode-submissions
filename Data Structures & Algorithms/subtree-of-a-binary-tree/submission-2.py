# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Step 1: Serialize both trees
        def serialize(node):
            if not node:
                return [",#"]
            # Delimit values with commas so '12' doesn't match '1' and '2'
            return [f",{node.val}"] + serialize(node.left) + serialize(node.right)
            
        r_str = "".join(serialize(root))
        s_str = "".join(serialize(subRoot))
        
        # Step 2: Implement KMP substring search
        return self.kmp_search(r_str, s_str)

    def kmp_search(self, text: str, pattern: str) -> bool:
        # Build KMP Longest Prefix Suffix (LPS) table
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        # Perform match
        t_idx = p_idx = 0
        while t_idx < len(text):
            if text[t_idx] == pattern[p_idx]:
                t_idx += 1
                p_idx += 1
                if p_idx == len(pattern):
                    return True
            else:
                if p_idx != 0:
                    p_idx = lps[p_idx - 1]
                else:
                    t_idx += 1
        return False
