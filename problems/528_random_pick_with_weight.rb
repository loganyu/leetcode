=begin
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.
=end

class Solution

=begin
    :type w: Integer[]
=end
    def initialize(w)
        @psum = []
        @total = 0
        w.each do |i|
            @total += i
            @psum << @total
        end
    end


=begin
    :rtype: Integer
=end
    def pick_index()
        targ = rand(@total)
        lo = 0
        hi = @psum.length - 1
        while lo != hi
            mid = lo + (hi-lo)/2
            if targ >= @psum[mid]
                lo = mid + 1
            else
                hi = mid
            end
        end
        
        return lo
    end


end

# Your Solution object will be instantiated and called as such:
# obj = Solution.new(w)
# param_1 = obj.pick_index()

