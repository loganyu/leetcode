=begin

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
=end

# @param {String} s
# @return {String}
def reverse_vowels(s)
    l = 0
    r = s.length - 1
    vowels = %w(a e i o u A E I O U)
    while l < r
        while l < r && !vowels.include?(s[l])
            l += 1
        end
        while l < r && !vowels.include?(s[r])
            r -= 1
        end
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    end
    
    return s
end
