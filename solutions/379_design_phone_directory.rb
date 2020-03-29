=begin
Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.
Example:

// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
=end

class PhoneDirectory

=begin
    Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
    :type max_numbers: Integer
=end
    def initialize(max_numbers)
        @directory = Set.new(0...max_numbers)
        @stack = (0...max_numbers).to_a
    end


=begin
    Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
    :rtype: Integer
=end
    def get()
        if @directory.empty?
            return -1
        end
        number = @stack.pop
        @directory.delete(number)
        
        return number
    end


=begin
    Check if a number is available or not.
    :type number: Integer
    :rtype: Boolean
=end
    def check(number)
        @directory.include?(number)
    end


=begin
    Recycle or release a number.
    :type number: Integer
    :rtype: Void
=end
    def release(number)
        if !@directory.include?(number)
            @directory.add(number)
            @stack.push(number)
        end
    end


end

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory.new(max_numbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

