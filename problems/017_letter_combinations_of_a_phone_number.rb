=begin
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
=end

PHONE = {
    '2' => %w(a b c),
    '3' => %w(d e f),
    '4' => %w(g h i),
    '5' => %w(j k l),
    '6' => %w(m n o),
    '7' => %w(p q r s),
    '8' => %w(t u v),
    '9' => %w(w x y z),
}
# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
    @output = []
    if !digits.empty?
        backtrack("", digits)
    end
    
    return @output
end

def backtrack(combo, next_digits)
    if next_digits.length == 0
        @output.push(combo)
    else
        PHONE[next_digits[0]].each do |letter|
            backtrack(combo + letter, next_digits[1..-1])
        end
    end
end

