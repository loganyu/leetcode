'''
All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

0 <= s.length <= 105
s[i] is 'A', 'C', 'G', or 'T'.
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []
        
        a = 4
        aL = pow(a, L)
        
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int[char] for char in s]
        
        h = 0
        seen, output = set(), set()
        for start in range(n - L + 1):
            if start != 0:
                h = (h * a) - (nums[start-1] * aL) + nums[start+L-1]
            else:
                for i in range(L):
                    h = (h * a) + nums[i]
            if h in seen:
                output.add(s[start:start+L])
            else: 
                seen.add(h)
        
        return output
        
