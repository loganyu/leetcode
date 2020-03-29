=begin
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
=end

class MedianFinder

=begin
    initialize your data structure here.
=end
    def initialize()
        @nums = []
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add_num(num)
        insert_index = @nums.bsearch_index{|val| val >= num}
        if insert_index.nil?
            @nums.push(num)
        else
            @nums.insert(insert_index, num)
        end
    end


=begin
    :rtype: Float
=end
    def find_median()
        l = @nums.length
        if l % 2 == 0
            return (@nums[l/2] + @nums[l/2 - 1])/2.0
        else
            return @nums[l/2]
        end
    end


end

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder.new()
# obj.add_num(num)
# param_2 = obj.find_median()

require './min_heap'
require './max_heap'

class MedianFinder

=begin
    initialize your data structure here.
=end
    def initialize()
        @lo = MaxHeap.new
        @hi = MinHeap.new
    end


=begin
    :type num: Integer
    :rtype: Void
=end
    def add_num(num)
        @lo.add(num)
        
        @hi.add(@lo.poll)
        
        if @lo.size < @hi.size
            @lo.add(@hi.poll)
        end
    end


=begin
    :rtype: Float
=end
    def find_median()
       if @lo.size > @hi.size
           @lo.peek
       else
           (@lo.peek + @hi.peek)/2.0
       end
    end


end
