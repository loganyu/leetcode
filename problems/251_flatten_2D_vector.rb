=begin
Design and implement an iterator to flatten a 2d vector. It should support the following operations: next and hasNext.

 

Example:

Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

iterator.next(); // return 1
iterator.next(); // return 2
iterator.next(); // return 3
iterator.hasNext(); // return true
iterator.hasNext(); // return true
iterator.next(); // return 4
iterator.hasNext(); // return false
 

Notes:

Please remember to RESET your class variables declared in Vector2D, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume that next() call will always be valid, that is, there will be at least a next element in the 2d vector when next() is called.
 

Follow up:

As an added challenge, try to code it using only iterators in C++ or iterators in Java.
=end

class Vector2D

=begin
    :type v: Integer[][]
=end
    def initialize(v)
        @v = v
        @i = 0
        @vi = 0
    end


=begin
    :rtype: Integer
=end
    def next()
        if has_next()
            val = @v[@vi][@i]
            @i += 1
            return val
        end
        
        return nil
    end


=begin
    :rtype: Boolean
=end
    def has_next()
        if @vi >= @v.length
            return false
        end
        if @i >= @v[@vi].length
            @i = 0
            @vi += 1
            return has_next()
        end
        return true
    end


end

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D.new(v)
# param_1 = obj.next()
# param_2 = obj.has_next()