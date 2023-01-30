=begin
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
=end

class MovingAverage

=begin
    Initialize your data structure here.
    :type size: Integer
=end
    def initialize(size)
        @size = size
        @ints = []
        @sum = 0
    end


=begin
    :type val: Integer
    :rtype: Float
=end
    def next(val)
        @ints << val
        @sum += val
        if @ints.count > @size
            @sum -= @ints.shift
        end
        
        @sum.to_f / @ints.count
    end


end

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage.new(size)
# param_1 = obj.next(val)

