class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: An odd length string can never be balanced
        if len(s) % 2 != 0:
            return False
        
    # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
    
        for char in s:
        # If it is a closing bracket
            if char in bracket_map:
            # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
            
            # If the mapping doesn't match the popped element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
            # It's an opening bracket, push it onto the stack
                stack.append(char)
            
    # The string is valid only if the stack is completely empty
        return len(stack) == 0