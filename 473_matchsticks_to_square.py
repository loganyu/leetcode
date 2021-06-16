'''
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
 

Constraints:

1 <= matchsticks.length <= 15
0 <= matchsticks[i] <= 109
'''

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False
        L = len(matchsticks)
        perimeter = sum(matchsticks)
        possible_side = perimeter // 4
        if possible_side * 4 != perimeter:
            return False
        matchsticks.sort(reverse=True)
        sums = [0 for _ in range(4)]
        
        def dfs(index):
            if index == L:
                return sums[0] == sums[1] == sums[2] == possible_side
            for i in range(4):
                if sums[i] + matchsticks[index] <= possible_side:
                    sums[i] += matchsticks[index]
                    if dfs(index + 1):
                        return True
                    sums[i] -= matchsticks[index]
            return False
        
        return dfs(0)
        
