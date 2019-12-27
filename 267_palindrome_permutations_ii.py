'''
Given a string s, return all the palindromic permutations (without duplicates) of it. Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
'''

class Solution(object):
    def generatePalindromes(self, s):
        freq = collections.Counter(s)
        middle = [char for char in freq if freq[char] % 2 == 1]
        if len(middle) > 1:
            return []
        
        if middle:
            freq[middle[0]] -= 1
            total = len(s) - 1
        else:
            total = len(s)
        path = []
        ans = []
        self.permute(total, middle, freq, path, ans)
        
        return ans
    
    def permute(self, total, middle, freq, path, ans):
        if total == 0:
            ans.append(''.join(path + middle + list(reversed(path))))
        for char in freq:
            if freq[char] <= 0:
                continue
            freq[char] -= 2
            path.append(char)
            self.permute(total - 2, middle, freq, path, ans)
            freq[char] += 2
            path.pop()
            
