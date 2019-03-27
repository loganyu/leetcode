=begin
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
=end

# @param {Integer} n
# @return {String[]}
def generate_parenthesis(n)
    solutions = []
    backtrack('', n, 0, 0, solutions)
    
    return solutions
end

def backtrack(sol, n, left, right, solutions)
    if sol.length == 2*n
        solutions << sol
    end
    if left < n
      backtrack(sol + '(', n, left+1, right, solutions)
    end
    if right < left
        backtrack(sol + ')', n, left, right+1, solutions)
    end
end

puts generate_parenthesis(3).inspect