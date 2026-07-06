class Solution:
    def isValid(self, s: str) -> bool:
        # Match each closing bracket to its opening bracket
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack, or use '#' if the stack is empty
                top_element = stack.pop() if stack else '#'
                
                # If the popped opening bracket doesn't match the current closing bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were closed correctly!
        return not stack