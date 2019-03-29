=begin
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
=end

# @param {Integer} n
# @return {String}
def count_and_say(n)
    counts = [[nil], [1]]
    1.upto(n) do |i|
        count = []
        n_cur = nil
        n_count = 0

        counts[i].each do |num|
            if n_cur.nil? || n_cur != num
                if !n_cur.nil?
                    count << n_count
                    count << n_cur
                end
                n_cur = num
                n_count = 1
            else
                n_count += 1
            end
        end
        count << n_count
        count << n_cur
        counts << count
    end
    
    counts[n].join
end

puts count_and_say(10).inspect