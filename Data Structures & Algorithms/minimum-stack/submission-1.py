class MinStack:

    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to store the minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val is smaller/equal to current min, push it
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # If the popped value is the current minimum, remove it from min_stack too
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top element of the min stack
        return self.min_stack[-1]