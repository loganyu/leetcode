=begin
155. Min Stack
Easy

1683

178

Favorite

Share
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
=end

class MinStack

=begin
    initialize your data structure here.
=end
    def initialize()
        @min = []
        @stack = []
    end


=begin
    :type x: Integer
    :rtype: Void
=end
    def push(x)
        @stack.push(x)
        if @min.empty? || x <= @min[-1]
            @min.push(x)
        end
    end


=begin
    :rtype: Void
=end
    def pop()
        if @stack[-1] == @min[-1]
            @min.pop()
        end
        @stack.pop()
    end


=begin
    :rtype: Integer
=end
    def top()
        @stack[-1]
    end


=begin
    :rtype: Integer
=end
    def get_min()
        @min[-1]
    end


end

# Your MinStack object will be instantiated and called as such:
# obj = MinStack.new()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()