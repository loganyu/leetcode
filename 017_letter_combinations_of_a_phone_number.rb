=begin
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
=end

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)    
    output = []
    if !digits.empty?
      backtrack("", digits, output)
    end

    return output
end
    
def backtrack(combination, next_digits, output)
    phone = {
        '2' => ['a','b','c'],
        '3' => ['d','e','f'], 
        '4' => ['g','h','i'], 
        '5' => ['j','k','l'], 
        '6' => ['m','n','o'], 
        '7' => ['p','q','r','s'],
        '8' => ['t','u','v'],
        '9' => ['w','x','y','z'],
    }
    if next_digits.length == 0
        output.push(combination)
    else
        phone[next_digits[0]].each do |letter|
            backtrack(combination + letter, next_digits[1..-1], output)
        end
    end
end

puts letter_combinations("23").inspect