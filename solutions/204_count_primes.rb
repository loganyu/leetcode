=begin
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
=end

# @param {Integer} n
# @return {Integer}
def count_primes(n)
    if n < 3
        return 0
    end
    
    count = 1
    upper = Math.sqrt(n)
    passed = Array.new(n, false)
    (3...n).step(2).each do |i|
        if passed[i]
            next
        end
        count += 1
        if i > upper
            next
        end
        j = i*i
        while j < n
            passed[j] = true
            j += 2*i
        end
    end
    
    return count
end

