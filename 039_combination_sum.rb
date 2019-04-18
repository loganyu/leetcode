=begin
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
=end

# @param {Integer[]} candidates
# @param {Integer} target
# @return {Integer[][]}
def combination_sum(candidates, target)
    answers = []
    candidates = candidates.sort
    search(candidates, target, answers, [], 0)
    
    return answers
end

def search(candidates, target, answers, combo, i)
    i.upto(candidates.length - 1).each do |i|
        if target - candidates[i] == 0
            combo << candidates[i]
            answers << combo.dup
            combo.pop
        elsif target - candidates[i] > 0
            combo << candidates[i]
            search(candidates, target - candidates[i], answers, combo, i)
            combo.pop
        end
    end
end