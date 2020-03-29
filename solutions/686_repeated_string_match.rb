=begin
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
=end

# @param {String} a
# @param {String} b
# @return {Integer}
def repeated_string_match(a, b)
    count = 0
    s = ""
    while s.length < b.length
        s += a
        count += 1
    end
    if s.include?(b)
        return count
    end
    s += a
    count += 1
    if s.include?(b)
        return count
    end
    
    return -1
end

