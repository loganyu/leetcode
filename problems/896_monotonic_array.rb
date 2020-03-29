=begin
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.
=end

# @param {Integer[]} a
# @return {Boolean}
def is_monotonic(a)
    increasing = decreasing = true
    (0...a.length - 1).each do |i|
        if a[i] > a[i+1]
            increasing = false
        elsif a[i] < a[i+1]
            decreasing = false
        end
        if !increasing && !decreasing
            return false
        end
    end
    
    return true
end