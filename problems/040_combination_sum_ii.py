'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''

class Solution:
    def combinationSum2(self, candidates, target):
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return
        if target == 0:
            answer.append(path)
            return
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                answer,
            )

