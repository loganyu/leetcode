'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.mins = []
        

    def push(self, x: int) -> None:
        self.items.append(x)
        if len(self.mins) == 0 or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        top = self.items.pop()
        if top == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

